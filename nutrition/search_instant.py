#search/instant
import requests
import urllib.request as urllib2
import json
from pprint import pprint

url = "https://trackapi.nutritionix.com/v2/search/instant?"

body = {

  'query': food,

}

headers = {
    'x-app-id': "ff0ccea8",
    'x-app-key': "605660a17994344157a78f518a111eda",
    'x-remote-user-id': "7a43c5ba-50e7-44fb-b2b4-bbd1b7d22632",
    'Content-Type': "application/json",

}

response = requests.request("GET", url, params=body, headers=headers)

data = response.json()

print ('food name: ', data['branded'][0]['food_name'])
print ('food calories: ', data['branded'][0]['nf_calories'])
# print ('food name: ', data['branded'][0]['food_name'])


# obj = json.loads(data)
# print(type(obj))
#
# print(obj)

print(response.json()['branded'])
