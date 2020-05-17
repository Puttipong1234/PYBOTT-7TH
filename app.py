from flask import Flask, request, abort , send_from_directory

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
from Flexmessage.ImgMap import Create_ImgMap_AllProvider , Create_ImgMap_ChooseProvider

app = Flask(__name__)
from config import channel_access_token , channel_secret , DATABASE_URL , RICHMENU_ID
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
firebase = firebase.FirebaseApplication(DATABASE_URL, None)
DATABASE_NAME = "TRACKING_HISTORY"

import os
@app.route("/ImgMap/<picname>/1040")
def serve_imagemap_chooseprovider(picname):
    current_file_folder = os.path.dirname(os.path.realpath(__file__)) #get directory path ของไฟล์นี้
    print(current_file_folder)
    image_folder = os.path.join(current_file_folder,"Flexmessage")
    print(image_folder)
    return send_from_directory(image_folder,picname)
    


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
        if match_tracking_menu(TEXT_FOR_MATCHING="บริการตรวจสอบพัสดุ",TEXT_FROM_USER=MESSAGE_FROM_USER): # validate input
            # update database
            data = {"session" : "บริการตรวจสอบพัสดุ"}
            res = firebase.patch(UID+"/",data)
            # text = TextSendMessage("ท่านได้เข้าสู่บริการตรวจสอบหมายเลขพัสดุ กรุณาเลือกผู้จัดส่งคะ \n\n THAIPOST(1) KERRY(2) DHL(3)")
            image_map_message = Base.get_or_new_from_json_dict(Create_ImgMap_ChooseProvider(),ImagemapSendMessage)
            line_bot_api.reply_message(REPLY_TOKEN , image_map_message) #ส่งข้อความ response data
        
        elif match_tracking_menu(TEXT_FOR_MATCHING="รองรับเจ้าไหนบ้าง?",TEXT_FROM_USER=MESSAGE_FROM_USER):
            image_map_message = Base.get_or_new_from_json_dict(Create_ImgMap_AllProvider(),ImagemapSendMessage)
            
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
            
            qbtn3 = QuickReplyButton(image_url="https://i0.wp.com/marketeeronline.co/wp-content/uploads/2018/07/Post_Web-1.jpg?fit=816%2C455&ssl=1"
                                    ,action=MessageAction(
                                        label="ประวัติการค้นหาพัสดุ"
                                        ,text="ประวัติการค้นหาพัสดุ")
                                    )
            
            qreply = QuickReply(items=[qbtn,qbtn2,qbtn3])
            
            text = TextSendMessage("กรุณาเลือกตำสั่ง เพื่อเริ่มต้นใช้งานได้เลยคะ",quick_reply=qreply)
            
            line_bot_api.reply_message(REPLY_TOKEN , messages=[image_map_message,text]) #ส่งข้อความ response data
        
        elif match_tracking_menu(TEXT_FOR_MATCHING="ประวัติการค้นหา",TEXT_FROM_USER=MESSAGE_FROM_USER):
            การค้นหาพัสดุทั้งหมด = firebase.get("/{}/TRACKING_HISTORY".format(UID),None)
            # print(การค้นหาพัสดุทั้งหมด)
            plain_text = "📌 ข้อมูลการค้นหาล่าสุด....\n"
            for เลขพัสดุ,ข้อมูล in การค้นหาพัสดุทั้งหมด.items():
                # print(เลขพัสดุ)
                # print(ข้อมูล["สถานะล่าสุดของพัสดุ"])
                plain_text = plain_text + "\n" + "📍" + เลขพัสดุ + "\n\tสถานะปัจจุบัน : " + ข้อมูล["สถานะล่าสุดของพัสดุ"] + "\n"
            
            plain_text = plain_text + "\n" + "▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️"
            
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
            
            qbtn3 = QuickReplyButton(image_url="https://i0.wp.com/marketeeronline.co/wp-content/uploads/2018/07/Post_Web-1.jpg?fit=816%2C455&ssl=1"
                                    ,action=MessageAction(
                                        label="ประวัติการค้นหาพัสดุ"
                                        ,text="ประวัติการค้นหาพัสดุ")
                                    )
            
            qreply = QuickReply(items=[qbtn,qbtn2,qbtn3])
            
            text = TextSendMessage(text=plain_text,quick_reply=qreply)
            line_bot_api.reply_message(reply_token=REPLY_TOKEN , messages=[text])
                
        
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
            
            qbtn3 = QuickReplyButton(image_url="https://i0.wp.com/marketeeronline.co/wp-content/uploads/2018/07/Post_Web-1.jpg?fit=816%2C455&ssl=1"
                                    ,action=MessageAction(
                                        label="ประวัติการค้นหาพัสดุ"
                                        ,text="ประวัติการค้นหาพัสดุ")
                                    )
            
            qreply = QuickReply(items=[qbtn,qbtn2,qbtn3])
            
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
        #กรณีที่ไม่เจอพัสดุ
        if isinstance(r,str):
            text = TextSendMessage("ไม่พบหมายเลขพัสดุ กรุณาใส่เลขใหม่อีกครั้งคะ")
            line_bot_api.reply_message(REPLY_TOKEN , text) #ส่งข้อความ response data
        
        #กรณีที่เจอพัสดุ
        else :
            # result = firebase.get("{}/{}/{}".format(UID,DATABASE_NAME,MESSAGE_FROM_USER),None)
            flex_message = create_message(requests_data=r,tracking_number=MESSAGE_FROM_USER) #สร้าง dict ที่ถูกแทนที่ด้วย data จากการ request api
            tracking_bubble_message = Base.get_or_new_from_json_dict(flex_message,FlexSendMessage) #เปลี่ยน dict ให้กลายเป็น message Object
            data = {"การค้นหาล่าสุด" : str(datetime.now()),"สถานะล่าสุดของพัสดุ" : str(r["info"][0]["description"])} #เก็บข้อมูล สถานะของพัสดุ
            res = firebase.patch(UID+"/"+DATABASE_NAME+"/"+MESSAGE_FROM_USER,data)
            # text1 = TextSendMessage(str(r))
            text2 = TextSendMessage("กรุณากดปุ่ม หรือ พิมพ์ 'ออกจากคำสั่ง' เพื่อออกจากการค้นหา")
            line_bot_api.reply_message(REPLY_TOKEN , messages=[tracking_bubble_message,text2]) #ส่งข้อความ response data


@handler.add(FollowEvent)
def Register(event):
    REPLY_TOKEN = event.reply_token #เก็บ reply token
    UID = event.source.user_id #เก็บ user id
    
    line_bot_api.link_rich_menu_to_user(user_id=UID,rich_menu_id=RICHMENU_ID)
    
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
    
    qbtn3 = QuickReplyButton(image_url="https://i0.wp.com/marketeeronline.co/wp-content/uploads/2018/07/Post_Web-1.jpg?fit=816%2C455&ssl=1"
                                    ,action=MessageAction(
                                        label="ประวัติการค้นหาพัสดุ"
                                        ,text="ประวัติการค้นหาพัสดุ")
                                    )
            
    qreply = QuickReply(items=[qbtn,qbtn2,qbtn3])
    
    image_message = ImageSendMessage(original_content_url="https://en.pimg.jp/042/301/008/1/42301008.jpg",
                                     preview_image_url="https://en.pimg.jp/042/301/008/1/42301008.jpg"
                                     )
    
    text_message = TextSendMessage(text="ยินต้อนรับเข้าสู่บริการตรวจสอบสถานะพัสดุฟรี! กรุณากดปุ่ม หรือไปที่แถบช่วยเหลือ เพื่อเริ่มใช้งานคะ",quick_reply=qreply)
    
    line_bot_api.reply_message(reply_token=REPLY_TOKEN , messages=[image_message,text_message])
    

if __name__ == "__main__":
    app.run(port=8080,debug=True)