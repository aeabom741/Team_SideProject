import requests

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314'
r = requests.get(url)
dict = r.json()

city_dict = {"新竹縣":0, "金門縣":1, "苗栗縣":2, "新北市":3, "宜蘭縣":4, "雲林縣":5, "臺南市":6, "高雄市":7, "彰化縣":8, "臺北市":9, "南投縣":10, "澎湖縣":11, "基隆市":12, "桃園市":13, \
            "花蓮縣":14, "連江縣":15, "臺東縣":16, "嘉義市":17, "嘉義縣":18, "屏東縣":19, "臺中市":20, "新竹市":21}
weatherElement_dict = {"12小時降雨機率":0, "平均溫度":1, "平均相對濕度":2, "最小舒適度指數":3, "最大風速":4, "最高體感溫度":5, "天氣現象":6, "最大舒適度指數":7, "最低溫度":8, "紫外線指數":9, \
                        "天氣預報綜合描述":10, "最低體感溫度":11, "最高溫度":12, "風向":13, "平均露點溫度":14}
measure_dict = {"百分比":"%", "攝氏度":"˚C", "自定義 CI 文字":"", "公尺/秒":"m/s", "蒲福風級":" 蒲福風級", "自定義 Wx 文字":"", "NA ":"", "紫外線指數":"", "曝曬級數":"", "NA":"", "8方位":""}

# 輸入要查詢的縣市及天氣資料
Counties = input("請輸入縣市名 : ")
weather_data = input("請輸入要查詢的天氣資料: ")

data = dict["records"]["locations"][0]["location"][city_dict[Counties]]["weatherElement"][weatherElement_dict[weather_data]]["time"]
for i in data:
    if weather_data in ["最小舒適度指數", "最大風速", "最大舒適度指數", "紫外線指數"]:
        print(i["startTime"], i["endTime"], i["elementValue"][1]["value"]+measure_dict[i["elementValue"][1]["measures"]])
    else:
        print(i["startTime"], i["endTime"], i["elementValue"][0]["value"]+measure_dict[i["elementValue"][0]["measures"]])