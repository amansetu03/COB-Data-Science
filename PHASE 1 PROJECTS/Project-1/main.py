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

#json_data = json.dumps(json_respond,indent = 4)#indent 4 is use to formate
# print(json_data)

df = pd.DataFrame(json_respond)

# print(df.head(100))
df.to_csv("Output/API_data.csv",index = False)
print("File saved!")