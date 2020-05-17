
richdata = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": True,
  "name": "PYBOTT-7TH",
  "chatBarText": ">แถบช่วยเหลือ<",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 9,
        "width": 1660,
        "height": 812
      },
      "action": {
        "type": "message",
        "text": "บริการตรวจสอบพัสดุ"
      }
    },
    {
      "bounds": {
        "x": 1716,
        "y": 9,
        "width": 765,
        "height": 821
      },
      "action": {
        "type": "message",
        "text": "รองรับเจ้าไหนบ้าง?"
      }
    },
    {
      "bounds": {
        "x": 9,
        "y": 840,
        "width": 1642,
        "height": 792
      },
      "action": {
        "type": "message",
        "text": "ประวัติการค้นหา"
      }
    },
    {
      "bounds": {
        "x": 1707,
        "y": 868,
        "width": 765,
        "height": 746
      },
      "action": {
        "type": "uri",
        "uri": "https://www.facebook.com/Pybott/"
      }
    }
  ]
}


from config import channel_access_token #
# channel_access_token = channel_access_token
Image_File_Path = "Richmenu.png"
import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):


    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())


CreateRichMenu(ImageFilePath=Image_File_Path,Rich_json=richdata,channel_access_token=channel_access_token)

