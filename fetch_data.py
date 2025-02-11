import requests
import pandas as pd
from datetime import datetime, timedelta

def datetime_to_string(date):
    return date.strftime("%Y-%m-%d")

def fetch_one_Data(date, commodity):
    URL= 'https://siskaperbapo.jatimprov.go.id/home2/getDataMap/?tanggal=' + date + '&komoditas=' + commodity

    response = requests.get(URL, 
                    headers={'Content-Type': 'text/html; charset=UTF-8'},
                    data={'tanggal': date, 'komoditas': commodity})

    json_data = response.json()
    return json_data

def fetch_dataset(start_date, end_date, commodity):
    dataset = []
    new_keys = ['tanggal', 'min', 'max', 'avg']
    
    date = start_date
    while date <= end_date:
        print(date)
        json_data = fetch_one_Data(datetime_to_string(date), commodity)
        data = {key: json_data.get(key) for key in new_keys if key in json_data}
        dataset.append(data)
        date += timedelta(days=1)
    
    return dataset

def main():
    start_date = datetime(end_date.year-10, end_date.month, end_date.day) # You can change the start date 
    end_date = datetime.now()
    Medium = '4' # You can change the commodity code
    all_Data = fetch_dataset(start_date, end_date, Medium)
    df = pd.DataFrame(all_Data)
    df.to_csv('Medium 2014-2024.csv', index=False)

if __name__ == '__main__':
    main()
