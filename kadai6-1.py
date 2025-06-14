import requests
import json


APP_ID = "7eb772fd10c0734447ad7c5b32c0e2f471b0a27b"
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData" #エンドポイント


params = {
    "appId": APP_ID,
    "statsDataId": "0003212969",  # 人口推計以外のデータという条件があるため、家計調査に変更
    "metaGetFlg": "Y",
    "cntGetFlg": "N",
    "explanationGetFlg": "Y",
    "annotationGetFlg": "Y",
    "sectionHeaderFlg": "1",
    "replaceSpChars": "0",
    "lang": "J"  
}


response = requests.get(API_URL, params=params)
data = response.json()
print(data)