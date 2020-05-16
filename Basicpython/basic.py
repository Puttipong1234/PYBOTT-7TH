# Variable
# x = 2
# y = 3
# x + y = ??

# x = "PY"
# y = "BOTT"
# x + y = "PYBOTT"

# x = 2.5
# y = 3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(y%x)

# x = "PY"
# y = "BOTT"
# b = 1
# c = 4
# a = b+c #5
# result = x + y + str(a)
# print(result)
# PYBOTT5

# ชื่อ = input("กรุณากรอกชื่อ : ")
# นามสกุล = input("ชื่อของท่านคือ {} \n กรุณากรอกนามสกุล : ".format(ชื่อ))
# ชื่อ - นามสกุล ของท่าน : Mr.john Doe
# วิธีที่ 1
# Format = "ชื่อ - นามสกุล ของท่าน : Mr."
# print(Format+ชื่อ+" "+นามสกุล)

#วิธีที่ 2
# print("ชื่อ - นามสกุล ของท่าน : Mr.{} {}".format(ชื่อ,นามสกุล))

#List      0         1         2        3       4
#List      -3       -2        -1
# ผลไม้ = ["apple", "banana", "cherry","orange","grape"]

#Access สมาชิคในตัวแปร
# print(ผลไม้[0]) #apple
# print(ผลไม้[2]) #cherry
# print(ผลไม้[-1]) #cherry

# print(ผลไม้[1:])

#add or delete member
# fruit = "watermelon"
# ผลไม้.append(fruit) # add water melon
# print(ผลไม้)
# ผลไม้.remove("apple")
# print(ผลไม้)

# for แต่ละชิ้น in ผลไม้:
#     print("เรามี {} อยู่ในตระกร้า".format(แต่ละชิ้น))

# char = "abcde"
# for ตัวอักษร in char:
#     print(ตัวอักษร)

# dictionary
#          key     value
# dict_a = {
#     "response": {
#         "items": {
#             "EV834283594TH": [
#                 {
#                     "barcode": "EV834283594TH",
#                     "status": "103",
#                     "status_description": "รับฝาก",
#                     "status_date": "11/02/2563 16:52:21+07:00",
#                     "location": "สระแก้ว",
#                     "postcode": "27000",
#                     "delivery_status": "null",
#                     "delivery_description": "null",
#                     "delivery_datetime": "null",
#                     "receiver_name": "null",
#                     "signature": "null"
#                 },
#                 {
#                     "barcode": "EV834283594TH",
#                     "status": "201",
#                     "status_description": "อยู่ระหว่างการขนส่ง",
#                     "status_date": "11/02/2563 17:07:00+07:00",
#                     "location": "สระแก้ว",
#                     "postcode": "27000",
#                     "delivery_status": "null",
#                     "delivery_description": "null",
#                     "delivery_datetime": "null",
#                     "receiver_name": "null",
#                     "signature": "null"
#                 },
#                 {
#                     "barcode": "EV834283594TH",
#                     "status": "201",
#                     "status_description": "อยู่ระหว่างการขนส่ง",
#                     "status_date": "11/02/2563 23:09:35+07:00",
#                     "location": "ศป.กบินทร์บุรี",
#                     "postcode": "25010",
#                     "delivery_status": "null",
#                     "delivery_description": "null",
#                     "delivery_datetime": "null",
#                     "receiver_name": "null",
#                     "signature": "null"
#                 },
#                 {
#                     "barcode": "EV834283594TH",
#                     "status": "301",
#                     "status_description": "อยู่ระหว่างการนำจ่าย",
#                     "status_date": "12/02/2563 14:09:43+07:00",
#                     "location": "หลักสี่",
#                     "postcode": "10210",
#                     "delivery_status": "null",
#                     "delivery_description": "null",
#                     "delivery_datetime": "null",
#                     "receiver_name": "null",
#                     "signature": "null"
#                 },
#                 {
#                     "barcode": "EV834283594TH",
#                     "status": "501",
#                     "status_description": "นำจ่ายสำเร็จ",
#                     "status_date": "12/02/2563 14:41:49+07:00",
#                     "location": "หลักสี่",
#                     "postcode": "10210",
#                     "delivery_status": "S",
#                     "delivery_description": "ผู้รับได้รับสิ่งของเรียบร้อยแล้ว",
#                     "delivery_datetime": "12/02/2563 14:41:49+07:00",
#                     "receiver_name": "พุฒิพงศ์/ผู้รับรับเอง",
#                     "signature": "https://trackimage.thailandpost.co.th/f/signature/QDgzNTk0YjVzMGx1VDMz/QGI1c0VWMGx1VDMx/QGI1czBsVEh1VDM0/QGI1czBsdTgzNDJUMzI="
#                 }
#             ]
#         },
#         "track_count": {
#             "track_date": "27/04/2563",
#             "count_number": 1,
#             "track_count_limit": 1000
#         }
#     },
#     "message": "successful",
#     "status": True
# }
# # print(dict_a["cat"]) #แมว

# print(dict_a["response"]["items"]["EV834283594TH"][-1]["status_description"])

# ถูก / ผิด 
# a = "กำลังนำส่ง"
# if a == "นำจ่ายสำเร็จ":
#     print("success")
#     # process update database
# else :
#     print("not success")
#     # process update database

# a = 0 #override
# while a == 0:
#     print("continue while loop")
#     a = int(input("Please input 0 to continue"))


# while add เลขพัสดุ 
# หาก user พิมพ์ตัว "x" ให้แสดงผล "สรุปเลขพัสดุทั้งหมดที่ท่านได้ทำการ add ทั้งหมดมีดังนี้ .... เลขพัสดุทั้งหมด"
# hint. ใช้ while loop > input > if else > list append 



# from ชื่อไฟล์ import ชื่อฟังก์ชั่น
# from learn_func import run_program


# if input("run program ?? (y/n)") == "y":
#     result = run_program()
#     print(result)
# else :
#     print("Program is not running ")