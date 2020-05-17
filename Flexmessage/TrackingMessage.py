# sample_r = {
#    "info":[
#       {
#          "date":"Date 28 ก.พ. 2563",
#          "description":"ปลายทางได้รับเรียบร้อยแล้ว",
#          "location":"กัน - นนทบุรี",
#          "time":" 11:37"
#       },
#       {
#          "date":"Date 28 ก.พ. 2563",
#          "description":"กำลังจัดส่ง",
#          "location":"กัน - นนทบุรี",
#          "time":" 07:58"
#       },
#       {
#          "date":"Date 28 ก.พ. 2563",
#          "description":"พัสดุถึงศูนย์คัดแยก",
#          "location":"กัน - นนทบุรี",
#          "time":" 01:02"
#       },
#       {
#          "date":"Date 27 ก.พ. 2563",
#          "description":"พัสดุถึงศูนย์คัดแยก",
#          "location":"KMLC - กรุงเทพมหานคร",
#          "time":" 20:05"
#       },
#       {
#          "date":"Date 27 ก.พ. 2563",
#          "description":"เคอรี่เข้ารับพัสดุแล้ว",
#          "location":"มีนบุรี - กรุงเทพมหานคร",
#          "time":" 16:09"
#       }
#    ],
#    "คาดว่าจะถึงวันที่":"28 ก.พ. 2563",
#    "ผู้รับ":"พุฒิพงศ์ ลิมสถายุรัตน์",
#    "ผู้ส่ง":"ENDLESS INTERTRADE"
# }

# # a = [1,2,3] ==> len(a) = 3 
# num = len(sample_r["info"])
# print(num)

# print(sample_r["คาดว่าจะถึงวันที่"])

# for แต่ละแถว in sample_r["info"]:
#     print(แต่ละแถว["date"])
#     print(แต่ละแถว["description"])


# 1. copy from linebot designer
# 2. เปลี่ยนข้อมูล true > True , false > False




location = "กัน - นนทบุรี"
description = "ปลายทางได้รับเรียบร้อยแล้ว"
date = "Date 28 ก.พ. 2563"
time = " 11:37"

# func สำหรับการสร้าง box
def create_row(location,description,date,time):
    
    color_status = "#2200fb"
    
    if description == "ปลายทางได้รับเรียบร้อยแล้ว":
          color_status = "#09ff00"
    
    elif description == "กำลังจัดส่ง":
          color_status = "#FFA500"

    elif description == "พัสดุถึงศูนย์คัดแยก":
          color_status = "#656464"
    
    elif description == "พัสดุพร้อมนำส่งให้เคอรี่ เอ็กซ์เพรส":
          color_status = "#2200fb"
          
    elif description == "ไม่สามารถติดต่อเลขหมายปลายทางได้":
          color_status = "#ff0000"
      
      
    sample_box = [
        { # seperator
          "type": "separator",
          "margin": "md"
        },
        { # box
          "type": "box",
          "layout": "vertical",
          "margin": "xxl",
          "contents": [
            {
              "type": "box",
              "layout": "horizontal",
              "margin": "xxl",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "flex": 1,
                  "contents": [
                    {
                      "type": "icon",
                      "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/placeholder.png?alt=media&token=9a803d42-042c-4631-b293-5dccc18236de"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "flex": 5,
                  "margin": "sm",
                  "contents": [
                    {
                      "type": "text",
                      "text": location,
                      "size": "xs",
                      "align": "start",
                      "gravity": "center",
                      "weight": "bold"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "flex": 7,
                  "contents": [
                    {
                      "type": "text",
                      "text": description,
                      "size": "xs",
                      "align": "center",
                      "gravity": "center",
                      "weight": "bold",
                      "color": color_status,
                      "wrap": False
                    }
                  ]
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "spacer",
                  "size": "xxl"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "วันที่",
                      "size": "xs"
                    },
                    {
                      "type": "text",
                      "text": date,
                      "size": "xs",
                      "color": "#0D0CB5"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "margin": "none",
                  "contents": [
                    {
                      "type": "text",
                      "text": "เวลา",
                      "size": "xs"
                    },
                    {
                      "type": "text",
                      "text": time,
                      "size": "xs",
                      "color": "#0D0CB5"
                    }
                  ]
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "margin": "md",
              "contents": [
                {
                  "type": "spacer",
                  "size": "xxl"
                }
              ]
            }
          ]
        }]
    
    return sample_box #list ที่ที seperator & box

# func สำหรับการสร้าง flex message
def create_message(requests_data,tracking_number):
    
    sample_flex = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "flex": 5,
          "contents": [
            {
              "type": "image",
              "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzLG7CiPIszm77VnDiz3AEOieJHO34fIY74u3R1i-WBI8RxDxt&usqp=CAU",
              "margin": "none",
              "align": "center",
              "size": "md",
              "aspectMode": "fit"
            },
            {
              "type": "text",
              "text": "TRACKING NUMBER",
              "margin": "lg",
              "size": "sm",
              "align": "center",
              "weight": "bold",
              "color": "#000000"
            },
            {
              "type": "text",
              "text": tracking_number,
              "margin": "none",
              "size": "lg",
              "align": "center",
              "weight": "bold",
              "color": "#ED6D02"
            },
            {
              "type": "text",
              "text": "( PAGE 1 OF 1 )",
              "margin": "none",
              "size": "xxs",
              "align": "center",
              "color": "#B9B9B9"
            }
          ]
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "margin": "none",
      "contents": [
        {
          "type": "separator"
        },
        {
          "type": "box",
          "layout": "horizontal",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "flex": 1,
              "contents": [
                {
                  "type": "filler"
                }
              ]
            },
            {
              "type": "box",
              "layout": "vertical",
              "flex": 5,
              "contents": [
                {
                  "type": "text",
                  "text": "Location",
                  "size": "xs",
                  "weight": "bold"
                }
              ]
            },
            {
              "type": "box",
              "layout": "vertical",
              "flex": 7,
              "contents": [
                {
                  "type": "text",
                  "text": "Status",
                  "size": "xs",
                  "align": "center",
                  "weight": "bold"
                }
              ]
            }
          ]
        }
         ## << จุดที่เราจะนำ box กลับมาใส่
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "flex": 2,
              "contents": [
                {
                  "type": "image",
                  "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/PYBOTT%20COVID-19%20SELF%20TRACKER%20(2).png?alt=media&token=2ae72bb4-4421-4191-859c-263df6bad3b2",
                  "margin": "md",
                  "align": "center",
                  "gravity": "center",
                  "size": "xxs"
                }
              ]
            },
            {
              "type": "box",
              "layout": "vertical",
              "flex": 7,
              "margin": "md",
              "contents": [
                {
                  "type": "spacer",
                  "size": "xs"
                },
                {
                  "type": "text",
                  "text": "ติดตามเราได้ที่ FB: PYBOTT",
                  "margin": "sm",
                  "size": "xs",
                  "align": "start",
                  "gravity": "center",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "https://www.facebook.com/Pybott/",
                  "margin": "none",
                  "size": "xxs",
                  "align": "start",
                  "gravity": "center",
                  "weight": "bold"
                }
              ]
            }
          ]
        }
      ]
    },
    "styles": {
      "footer": {
        "backgroundColor": "#F0F0F0",
        "separatorColor": "#000000"
      }
    }
  }
}
    
    end_spacer = {
          "type": "spacer",
          "size": "xl"
        }
    
    print(requests_data["info"])
    for each in requests_data["info"][0:4]: #ลดเหลือแค่ 5 box เพราะ flex ยาวเกิน ถ้าจะทำเพิ่มให้ใช้ carousel ช่วย
        row = create_row(location=each["location"],
                   description=each["description"],
                   date=each["date"],
                   time=each["time"])
        
        sample_flex["contents"]["body"]["contents"].append(row[0]) #seperator
        sample_flex["contents"]["body"]["contents"].append(row[1]) #box with content
    
    
    sample_flex["contents"]["body"]["contents"].append(end_spacer)
    
    return sample_flex
    