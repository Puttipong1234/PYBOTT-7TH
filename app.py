from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import requests
from firebase import firebase
from datetime import datetime
from test_fuzzy import match_tracking_menu
from Flexmessage.TrackingMessage import create_message

app = Flask(__name__)
from config import channel_access_token , channel_secret , DATABASE_URL
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
firebase = firebase.FirebaseApplication(DATABASE_URL, None)
DATABASE_NAME = "TRACKING_HISTORY"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    REPLY_TOKEN = event.reply_token #เก็บ reply token
    MESSAGE_FROM_USER = event.message.text #เก็บ ข้อความที่ user ส่งมา
    UID = event.source.user_id #เก็บ user id
    
    #check user เคยเข้ามารึยัง
    user = firebase.get("/{}".format(UID),None)
    if not user:
        data = {"session" : "none"}
        res = firebase.patch(UID+"/",data)
    
    #Get session จาก user ว่าคุยกับบอทถึงไหนแล้ว
    user_session = firebase.get("/{}/session".format(UID),None)
    
    if MESSAGE_FROM_USER == "ออกจากคำสั่ง":
        # update database
        data = {"session" : "none"}
        res = firebase.patch(UID+"/",data)
        text = TextSendMessage("ท่านได้ออกจากคำสั่งเรียบร้อยแล้ว มีอะไรให้ดิฉันรับใช่เพิ่มไหมคะ")
        line_bot_api.reply_message(REPLY_TOKEN , text) #ส่งข้อความ response data
    
    if user_session == "none": #check session
        if match_tracking_menu(TEXT_FROM_USER=MESSAGE_FROM_USER): # validate input
            # update database
            data = {"session" : "บริการตรวจสอบพัสดุ"}
            res = firebase.patch(UID+"/",data)
            text = TextSendMessage("ท่านได้เข้าสู่บริการตรวจสอบหมายเลขพัสดุ กรุณาเลือกผู้จัดส่งคะ \n\n THAIPOST(1) KERRY(2) DHL(3)")
            line_bot_api.reply_message(REPLY_TOKEN , text) #ส่งข้อความ response data
        
        else :
            qbtn = QuickReplyButton(image_url="https://i0.wp.com/marketeeronline.co/wp-content/uploads/2018/07/Post_Web-1.jpg?fit=816%2C455&ssl=1"
                                    ,action=MessageAction(
                                        label="บริการตรวจสอบพัสดุ"
                                        ,text="บริการตรวจสอบพัสดุ")
                                    )
            
            qbtn2 = QuickReplyButton(image_url="https://i0.wp.com/marketeeronline.co/wp-content/uploads/2018/07/Post_Web-1.jpg?fit=816%2C455&ssl=1"
                                    ,action=MessageAction(
                                        label="รองรับเจ้าไหนบ้าง?"
                                        ,text="รองรับเจ้าไหนบ้าง?")
                                    )
            
            qreply = QuickReply(items=[qbtn,qbtn2])
            
            text = TextSendMessage("ไม่มีบริการดังกล่าวค่ะ กรุณาเลือกใช้บริการที่เรามีดังนี้นะคะ",quick_reply=qreply)
            line_bot_api.reply_message(REPLY_TOKEN , text) #ส่งข้อความ response data
    
    elif user_session == "บริการตรวจสอบพัสดุ": #check session
        if MESSAGE_FROM_USER in ["1","2","3"]:
            # update database
            data = {"session" : "ใส่หมายเลข"}
            res = firebase.patch(UID+"/",data)
            text = TextSendMessage("กรุณาใส่หมายเลขพัสดุที่ต้องการตรวจสอบคะ")
            line_bot_api.reply_message(REPLY_TOKEN , text) #ส่งข้อความ response data
    
    elif user_session == "ใส่หมายเลข": #check session
        tracking_num = MESSAGE_FROM_USER
        r = requests.get('https://kerryapi.herokuapp.com/api/kerry/?tracking_number='+str(tracking_num)).json()
        #create json dict flex message from r
        print(r)
        #กรณีที่ไม่เจอพัสดุ
        if isinstance(r,str):
            text = TextSendMessage("ไม่พบหมายเลขพัสดุ กรุณาใส่เลขใหม่อีกครั้งคะ")
            line_bot_api.reply_message(REPLY_TOKEN , text) #ส่งข้อความ response data
        
        #กรณีที่เจอพัสดุ
        else :
            result = firebase.get("{}/{}/{}".format(UID,DATABASE_NAME,MESSAGE_FROM_USER),None)
            flex_message = create_message(requests_data=r,tracking_number=MESSAGE_FROM_USER) #สร้าง dict ที่ถูกแทนที่ด้วย data จากการ request api
            tracking_bubble_message = Base.get_or_new_from_json_dict(flex_message,FlexSendMessage) #เปลี่ยน dict ให้กลายเป็น message Object
            if not result:
                data = {"การค้นหาล่าสุด" : str(datetime.now())}
                res = firebase.patch(UID+"/"+DATABASE_NAME+"/"+MESSAGE_FROM_USER,data)
                # text1 = TextSendMessage(str(r))
                text2 = TextSendMessage("กรุณากดปุ่ม หรือ พิมพ์ 'ออกจากคำสั่ง' เพื่อออกจากการค้นหา")
                line_bot_api.reply_message(REPLY_TOKEN , messages=[tracking_bubble_message,text2]) #ส่งข้อความ response data

if __name__ == "__main__":
    app.run(port=8080,debug=True)