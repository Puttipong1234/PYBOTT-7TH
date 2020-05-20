## Source Code Pybott ติดตามสถานะพัสดุ
รวมไฟล์ รูปภาพ + UI Design และ source Code ต่างๆมากมาย เหมาะสำหรับผู้สนใจสร้าง APP แบบ Solo คนเดียว
ด้วย Python

### แชทบอทจากการอบรมครั้งที่ 7 

แอดเข้าไปทดลองเล่นๆ จิ้มๆ ได้เลย
https://line.me/R/ti/p/@304ycdwm
มีจุดประสงค์ให้ผู้เรียนได้นำ concept ไปพัฒนาต่อยอด Function อาจมีไม่ครบนะครับ

### สนใจเข้าร่วมการอบรม zero - master chatbot 
วันที่ 16-17 พค. 2020 ที่ผ่านมา สนใจสอบถามได้ที่ 
ส่งข้อความหน้าเพจ https://www.facebook.com/Pybott
(ลงทะเบียนครั้งเดียวเข้าเรียนได้ทุกครั้ง ย้อนดูได้ตลอดชีพ)

![ScreenShot](https://scontent.fbkk22-3.fna.fbcdn.net/v/t1.0-9/98166112_577365766487772_3486300897774927872_n.png?_nc_cat=110&_nc_sid=8024bb&_nc_eui2=AeH2YUlrGujJOqW4-6DYG5ACyx6d0cHWGUbLHp3RwdYZRqg844k6K0pnCXuRKwObsek&_nc_oc=AQlNL7mxgFZwDpw8drk_WD9Ku0Sxef0LmhswwBYJDHqfvw7t14S5NuyEGVR7AncnJ2k&_nc_ht=scontent.fbkk22-3.fna&oh=232a2b41adf2f2ab82e9441d4cd9f559&oe=5EEB9EA5)

## วิธีการใช้งานเบื้องต้น (กรุณาศึกษา framework ก่อนเริ่มใช้งาน)
1. cmd > git clone https://github.com/Puttipong1234/PYBOTT-7TH.git
2. สร้าง virtual env 
```
python -m venv venv (use python 3.6.8 - 3.6.10)
```
3. activate virtual evironment 
```
(window : venv\Scripts\activate / mac : source venv\bin\activate)
```
3. pip install -r requirements.txt
4. python app.py (รันแอพ)
5. deploy to heroku พร้อมตั้งค่า config local variable ต่างๆ

## หลักการ
 - แก้ไขไฟล์ config.py นำค่ามาใส่
 - ทำการ run app เพื่อเทสพร้อม ngrok
 - ผู้ใช้งานควรมีความเข้าใจในการพัฒนาเว็บด้วย Flask + Firebase

#### ฝากติดตาม กดไลค์ กดแชร์ คอนเทน เพื่อเป็นกำลังใจแก่ทีมงานด้วยนะครับขอบพระคุณอย่างสูง