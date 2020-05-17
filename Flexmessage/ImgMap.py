from flask import request

def Create_ImgMap_ChooseProvider():
    
  base_url = "https://{}/ImgMap/chooseProvider".format(request.host)
    
  imagemap_json = {
  "type": "imagemap",
  "baseUrl": base_url,
  "altText": "This is an imagemap",
  "baseSize": {
    "width": 1040,
    "height": 1040
  },
  "actions": [
    {
      "type": "message",
      "area": {
        "x": 16,
        "y": 181,
        "width": 1012,
        "height": 243
      },
      "text": "1"
    },
    {
      "type": "message",
      "area": {
        "x": 20,
        "y": 451,
        "width": 1004,
        "height": 259
      },
      "text": "2"
    },
    {
      "type": "message",
      "area": {
        "x": 27,
        "y": 746,
        "width": 993,
        "height": 278
      },
      "text": "3"
    }
  ]
}
  
  return imagemap_json
  

def Create_ImgMap_AllProvider():
      
  base_url = "https://{}/ImgMap/chooseProvider".format(request.host)
  
  imagemap_json = {
  "type": "imagemap",
  "baseUrl": base_url,
  "altText": "This is an imagemap",
  "baseSize": {
    "width": 1040,
    "height": 1040
  },
  "actions": [
    {
      "type": "uri",
      "area": {
        "x": 742,
        "y": 4,
        "width": 290,
        "height": 161
      },
      "linkUri": "https://www.facebook.com/Pybott/"
    },
    {
      "type": "message",
      "area": {
        "x": 16,
        "y": 188,
        "width": 1008,
        "height": 836
      },
      "text": "https://www.facebook.com/Pybott/"
    }
  ]
}
  return imagemap_json