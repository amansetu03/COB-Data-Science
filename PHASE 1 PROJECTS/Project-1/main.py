import pandas as pd
import requests
import json


api_link = "https://data.binance.com/api/v3/ticker/24hr"
# now getting the responce
print("wait Loading.",end = "")
while True:
    responce = requests.get(api_link)
    if responce.status_code == 200:
        print("\nApi Responding")
        json_respond = responce.json()
        break
    else:
        print(".",end = "")

df = pd.DataFrame(json_respond)

df.to_csv("Output/API_data.csv",index = False)
print("File saved!")