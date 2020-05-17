from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# text = "บริการตรวจสอบพัสดุ"

# sample_1 = "ช่วยตรวจสอบพัสดุให้ทีคะ"
# sample_2 = "ตรวจสอบพัสดุครับ"
# sample_3 = "ห้องน้ำอยู่ที่ไหน"


# result1 = fuzz.ratio(text,sample_1)
# result2 = fuzz.ratio(text,sample_2)
# result3 = fuzz.ratio(text,sample_3)
# print("result1 : " + str(result1))
# print("result2 : " + str(result2))
# print("result3 : " + str(result3))

def match_tracking_menu(TEXT_FOR_MATCHING,TEXT_FROM_USER):
    # result = fuzz.ratio("บริการตรวจสอบพัสดุ",TEXT_FROM_USER)
    result = fuzz.ratio(TEXT_FOR_MATCHING,TEXT_FROM_USER)
    if result >= 55:
        return True
    else:
        return False