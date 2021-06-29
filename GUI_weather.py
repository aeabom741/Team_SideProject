import tkinter as tk

def weather_search():
    import requests
    # import pandas as pd

    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314'
    r = requests.get(url)
    dict = r.json()

    city_dict = {"新竹縣":0, "金門縣":1, "苗栗縣":2, "新北市":3, "宜蘭縣":4, "雲林縣":5, "臺南市":6, "高雄市":7, "彰化縣":8, "臺北市":9, "南投縣":10, "澎湖縣":11, "基隆市":12, "桃園市":13, \
                "花蓮縣":14, "連江縣":15, "臺東縣":16, "嘉義市":17, "嘉義縣":18, "屏東縣":19, "臺中市":20, "新竹市":21}
    weatherElement_dict = {"12小時降雨機率":0, "平均溫度":1, "平均相對濕度":2, "最小舒適度指數":3, "最大風速":4, "最高體感溫度":5, "天氣現象":6, "最大舒適度指數":7, "最低溫度":8, "紫外線指數":9, \
                            "天氣預報綜合描述":10, "最低體感溫度":11, "最高溫度":12, "風向":13, "平均露點溫度":14}
    measure_dict = {"百分比":"%", "攝氏度":"˚C", "自定義 CI 文字":"", "公尺/秒":"m/s", "蒲福風級":" 蒲福風級", "自定義 Wx 文字":"", "NA ":"", "紫外線指數":"", "曝曬級數":"", "NA":"", "8方位":""}

    Counties = variable_city.get()
    weather_data = variable_weatherElements.get()


    data = dict["records"]["locations"][0]["location"][city_dict[Counties]]["weatherElement"][weatherElement_dict[weather_data]]["time"]
    result = open("/Users/shijunliao/Desktop/Python/side_project/weather/data.txt", "w")
    # df = pd.DataFrame(columns=["Start Time", "End Time", "Value"])
    for i in data:
        if weather_data in ["最小舒適度指數", "最大風速", "最大舒適度指數", "紫外線指數"]:
            result.write("{} \t\t {}\t\t{} \n".format(i["startTime"], i["endTime"], i["elementValue"][1]["value"]+measure_dict[i["elementValue"][1]["measures"]]))
            # df.loc[len(df)] = [i["startTime"], i["endTime"], i["elementValue"][1]["value"]+measure_dict[i["elementValue"][1]["measures"]]]
        else:
            result.write("{} \t\t {}\t\t{} \n".format(i["startTime"], i["endTime"], i["elementValue"][0]["value"]+measure_dict[i["elementValue"][0]["measures"]]))
            # df.loc[len(df)] = [i["startTime"], i["endTime"], i["elementValue"][0]["value"]+measure_dict[i["elementValue"][0]["measures"]]]
    result.close()
    result_label.configure(text=open("/Users/shijunliao/Desktop/Python/side_project/weather/data.txt", "r").read(),)


# GUI介面
window = tk.Tk()
window.title('天氣狀況查詢')
window.geometry('800x600')
window.configure(background='white')

header_label = tk.Label(window, text='天氣狀況查詢器')
header_label.pack()

# city 選單
city_frame = tk.Frame(window)
city_frame.pack(side=tk.TOP)
city_label = tk.Label(city_frame, text='縣市： ')
city_label.pack(side=tk.LEFT)
cityList = ["新竹縣", "金門縣", "苗栗縣", "新北市", "宜蘭縣", "雲林縣", "臺南市", "高雄市", "彰化縣", "臺北市", "南投縣", "澎湖縣", "基隆市", "桃園市", "花蓮縣", \
            "連江縣", "臺東縣", "嘉義市", "嘉義縣", "屏東縣", "臺中市", "新竹市"]
variable_city = tk.StringVar(window)
variable_city.set(cityList[0])
city_menu = tk.OptionMenu(city_frame, variable_city, *cityList)
city_menu.config(width=5, font=('Helvetica', 12))
city_menu.pack(side=tk.LEFT)

# weather elements 選單
weatherElements_frame = tk.Frame(window)
weatherElements_frame.pack(side=tk.TOP)
weatherElements_label = tk.Label(weatherElements_frame, text='天氣資料： ')
weatherElements_label.pack(side=tk.LEFT)
weatherElementsList = ["12小時降雨機率", "平均溫度", "平均相對濕度", "最小舒適度指數", "最大風速", "最高體感溫度", "天氣現象", "最大舒適度指數", "最低溫度", "紫外線指數", \
                        "天氣預報綜合描述", "最低體感溫度", "最高溫度", "風向", "平均露點溫度"]
variable_weatherElements = tk.StringVar(window)
variable_weatherElements.set(weatherElementsList[0])
weatherElements_menu = tk.OptionMenu(weatherElements_frame, variable_weatherElements, *weatherElementsList)
weatherElements_menu.config(width=10, font=('Helvetica', 12))
weatherElements_menu.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.config(width=100, height=20, font=('Helvetica', 12), justify="left")
result_label.pack()

search_btn = tk.Button(window, text="Search", command=weather_search)
search_btn.pack()


window.mainloop()
