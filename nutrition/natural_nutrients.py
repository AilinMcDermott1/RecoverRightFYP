# #natural/nutrients...
import requests
import json

url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

headers = {
    'x-app-id': "ff0ccea8",
    'x-app-key': "605660a17994344157a78f518a111eda",
    'x-remote-user-id': "7a43c5ba-50e7-44fb-b2b4-bbd1b7d22632",
    'Content-Type': "application/x-www-form-urlencoded",

    }

body = {
         'query': '1 cup of chicken soup',
         'timezone': 'US/Eastern',
         "locale": "en_US",
}

response = requests.request("POST", url, headers=headers, data=body)


data = response.json()

print ('food name: ', data['foods'][0]['food_name'])
print ('food calories: ', data['foods'][0]['nf_calories'])
print ('food calories: ', data['foods'][0]['nf_protein'])
print ('food calories: ', data['foods'][0]['nf_total_fat'])



print(response.json())