import requests
import json

# 気象庁のオープンデータ（天気予報）を利用して、千葉県の天気を表示するプログラム

# 千葉県の天気予報APIエンドポイント
API_URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/120000.json"

# APIリクエスト送信
response = requests.get(API_URL)

# レスポンス処理
if response.status_code == 200:
    data = response.json()

    # 今日の天気データを取得
    area = data[0]["timeSeries"][0]["areas"][0]  # 地域別天気（県全体）
    weather = area["weathers"][0]                # 今日の天気
    date = data[0]["reportDatetime"]             # 発表日時
    pops = data[0]["timeSeries"][1]["areas"][0]["pops"]  # 降水確率

    print("【千葉県の天気予報】")
    print(f"発表日時: {date}")
    print(f"今日の天気: {weather}")
    print(f"降水確率: {pops}")
else:
    print(f"エラー: HTTP {response.status_code}")
