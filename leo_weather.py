from time import time
import pandas as pd
import requests

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314'
r = requests.get(url)
dict = r.json()

city_level = dict["records"]["locations"][0]["location"]
df = pd.DataFrame(columns=["Location Name","description","Value","Measure","Start Time","End Time" ])



model_selection = int(input("Chose youe model:"))
'''
Select you want data type
model_selection = 1 (download you want to know city data)
model_selection = 2 (All city data download)
'''

#model_selection = 1
if model_selection == 1:
    print("Model 1 Start")
    print("Enter City Name:")
    selection = input("Search city:")

    """
    city:
    
    ("新竹縣"), ("金門縣"), ("苗栗縣"), ("新北市"), ("宜蘭縣"), 
    ("雲林縣"), ("臺南市"), ("高雄市"), ("彰化縣"), ("臺北市"), 
    ("南投縣"), ("澎湖縣"), ("基隆市"), ("桃園市"), ("花蓮縣"), 
    ("連江縣"), ("臺東縣"), ("嘉義市"), ("嘉義縣"), ("屏東縣"), 
    ("臺中市"), ("新竹市")
    """

    for i in city_level:
        city_name = i["locationName"]
        if selection == i['locationName']:
            weatherElement = i["weatherElement"]        
            for j in weatherElement:
                element_name = j["elementName"]
                description = j["description"]
                value_time = j["time"]
                for k in value_time:
                    start_time = k["startTime"]
                    end_time = k["endTime"]
                    element_value = k["elementValue"]
                    for v in element_value:
                        element_value = v["value"]
                        measure = v["measures"]
                        df.loc[len(df)] = [city_name,description,element_value,measure,start_time,end_time]
                        export = df[(df["Location Name"] == city_name) & (df["description"] == description)]
                        export.to_excel(f"/Users/lvjiawei/Documents/weather/{city_name}/{description}.xlsx",index=False)
                        print("Complete!")

#model_selection = 2
elif model_selection == 2:
    print("Model 2 Start")
    for i in city_level:
        city_name = i["locationName"]
        weatherElement = i["weatherElement"]
        for j in weatherElement:
            element_name = j["elementName"]
            description = j["description"]
            value_time = j["time"]
            for k in value_time:
                start_time = k["startTime"]
                end_time = k["endTime"]
                element_value = k["elementValue"]
                for v in element_value:
                    value = v["value"]
                    measure = v["measures"]
                    df.loc[len(df)] = [city_name,description,value,measure,start_time,end_time]


    citys = [("新竹縣"), ("金門縣"), ("苗栗縣"), ("新北市"), ("宜蘭縣"), ("雲林縣"), ("臺南市"), ("高雄市"), ("彰化縣"), ("臺北市"), ("南投縣"), ("澎湖縣"), ("基隆市"), ("桃園市"), ("花蓮縣"), \
             ("連江縣"), ("臺東縣"), ("嘉義市"), ("嘉義縣"), ("屏東縣"), ("臺中市"), ("新竹市")]

    descriptions = [("12小時降雨機率"), ("平均溫度"), ("平均相對濕度"), ("最小舒適度指數"), ("最大風速"), ("最高體感溫度"), ("天氣現象"), ("最大舒適度指數"), ("最低溫度"), ("紫外線指數"), \
                    ("天氣預報綜合描述"), ("最低體感溫度"), ("最高溫度"), ("風向"), ("平均露點溫度")]
    for city in citys:
        for description in descriptions:
            df_export = df[(df["Location Name"] == city) & (df["description"] == description)]
            df_export.to_excel(f"/Users/lvjiawei/Documents/weather/{city}/{description}.xlsx",index=False)
    print("Complete!")
else:
    print("model_selection type Error")