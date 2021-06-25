import pandas as pd
import requests

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314'
r = requests.get(url)
dict = r.json()

# city
dict["records"]["locations"][0]["location"][0]["locationName"]

# weather elements
dict["records"]["locations"][0]["location"][0]["weatherElement"]

# 資料類型
# 0     PoP12h                  12小時降雨機率
# 1     T                       平均溫度
# 2     RH                      平均相對濕度
# 3     MinCI                   最小舒適度指數
# 4     WS                      最大風速
# 5     MaxAT                   最高體感溫度
# 6     Wx                      天氣現象
# 7     MaxCI                   最大舒適度指數
# 8     MinT                    最低溫度
# 9     UVI                     紫外線指數
# 10    WeatherDescription      天氣預報綜合描述
# 11    MinAT                   最低體感溫度
# 12    MaxT                    最高溫度
# 13    WD                      風向
# 14    Td                      平均露點溫度

# 正式版
df = pd.DataFrame(columns=["Location Name", "Weather Element", "Start Time", "End Time", "Value"])
city_level = dict["records"]["locations"][0]["location"]
for i in city_level:
    # print(i["locationName"])
    city_name = i["locationName"]
    weatherElement_level = i["weatherElement"]
    for s in weatherElement_level:
        # print(s["description"])
        weather_element = s["description"]
        time_level = s["time"]
        for m in time_level:
            start_time = m["startTime"]
            end_time = m["endTime"]
            value_for_data = m["elementValue"][0]["value"]
            df.loc[len(df)] = [city_name, weather_element, start_time, end_time, value_for_data]

            
















