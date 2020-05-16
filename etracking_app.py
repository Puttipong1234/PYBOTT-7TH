# 1 step User select parcel provider
#1. ThaiPost 2. Kerry 3. DHL
import requests
from firebase import firebase
from datetime import datetime
firebase = firebase.FirebaseApplication('https://pybott-7th.firebaseio.com/', None)
DATABASE_NAME = "TRACKING_HISTORY"
while True:
    User_Id = input("กรุณาระบุชื่อผู้ใช้งาน") #input_User_Id
    Provider_in = input("กรุณาเลือกบริษัทขนส่งคะ THAIPOST(1) KERRY(2) DHL(3) or Exit(x)") #input_Provider_in
    if Provider_in == "2":
        Tracking_Number = input("กรุณาระบุเลขพัสดุที่ต้องการค้นหาคะ")
        r = requests.get('https://kerryapi.herokuapp.com/api/kerry/?tracking_number={}'.format(Tracking_Number)).json()
        # check ว่ามีเลขอยู่แล้วหรือไม่
        # ถ้าไม่มี
            # save เลขพัสดุลงในฐานข้อมูล (ประวัติการค้นหา)
        result = firebase.get("{}/{}/{}".format(User_Id,DATABASE_NAME,Tracking_Number),None)
        print(r)
        print(type(r))
        #PYBOTT/TRACKING_HISTORY/KED00374036156  
        # ถ้ายังไม่มี เลขอยู่ในฐานข้อมุล จะทำการเพิ่มลงไป
        if not result: # if not none ==> True
            data = {"การค้นหาล่าสุด" : str(datetime.now())}
            res = firebase.patch(User_Id+"/"+DATABASE_NAME+"/"+Tracking_Number,data)
    else :
        print("ขอบพระคุณที่ใช้บริการ")
        break