def get_weather_weekly_forecast(path):
    '''
    https://data.gov.tw/dataset/9308
    '''
    import pandas as pd
    import requests

    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314'
    r = requests.get(url)

    # Parse
    data = pd.read_json(r.text)
    data = data.loc['locations', 'records']
    data = data[0]['location']

    # Fetch Data ......
    results = pd.DataFrame()

    # 共22個地區，每個地區約30秒，資料筆數約60368
    for i in range(len(data)):
        loc_data = data[i]
        
        loc_name = loc_data['locationName']
        geocode = loc_data['geocode']
        lat = loc_data['lat']
        lon = loc_data['lon']
        weather_data = loc_data['weatherElement']

        # 資料類型，有15個
        # 0              PoP12h 12小時降雨機率
        # 1                   T 平均溫度
        # 2                  RH 平均相對濕度
        # 3               MinCI 最小舒適度指數
        # 4                  WS 最大風速
        # 5               MaxAT 最高體感溫度
        # 6                  Wx 天氣現象
        # 7               MaxCI 最大舒適度指數
        # 8                MinT 最低溫度
        # 9                UVI 紫外獻指數
        # 10 WeatherDescription 天氣預報綜合描述
        # 11              MinAT 最低體感溫度
        # 12               MaxT 最高溫度
        # 13                 WD 風向
        # 14                 Td 平均露點溫度
        
        
        for j in range(len((weather_data))):
            ele_data_dict = weather_data[j]
            
            for k in range(len(ele_data_dict)):
                ele_name = ele_data_dict['elementName']
                ele_desc = ele_data_dict['description']
                ele_data = ele_data_dict['time']

                # 此欄位為質性資料，如「'陰短暫雨。降雨機率 90%。溫度攝氏18至22度。
                # 舒適。東北風 風速5級(每秒8公尺)。相對濕度92%。'」，因此不保留
                if ele_name == 'WeatherDescription':
                    continue
                
                for l in range(len(ele_data)):
                    start_time = ele_data[l]['startTime']
                    end_time = ele_data[l]['endTime']
                    value = ele_data[l]['elementValue'][0]['value']
                    
                    # 先保留全部的資料，最後再決定要保留哪些欄位
                    new_data = \
                        pd.DataFrame({'location':[loc_name],
                                      'geocode':[geocode],
                                      'lat':[lat],
                                      'lon':[lon],
                                      'element':[ele_name],
                                      'description':[ele_desc],
                                      'start_time':[start_time],
                                      'end_time':[end_time],
                                      'value':[value]})
                    
                    results = results.append(new_data)
        print('update_weekly_forecast' + str(i) + '/' + str(len(data)))
            
    results = results.reset_index(drop=True)
    results.to_csv(path + '/r.csv', index=False)
    return results