
#search/instant
import requests
import urllib.request as urllib2
import json

url = "https://trackapi.nutritionix.com/v2/search/instant?"

querystring = {"query":"chicken%20soup"}


headers = {
    'x-app-id': "ff0ccea8",
    'x-app-key': "605660a17994344157a78f518a111eda",
    'x-remote-user-id': "26ef87cb-e285-493b-9cda-141731ed3f02",

    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())


#######################################################################################################################

#natural/nutrients...
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
         'query': 'chicken',
         'timezone': 'US/Eastern',
}

response = requests.request("POST", url, headers=headers, data=body)

print(response.json())

for item in data("foods"):
    print item()


########################################################################################
import urllib.parse
import requests

main_api = 'https://trackapi.nutritionix.com/v2/natural/nutrients/'

while True:
    food_name = input('Food name: ')

    if food_name == 'quit' or food_name == 'q':
        break

    url = main_api + urllib.parse.urlencode({'food_name': food_name})
    print (url)

    json_data = requests.get(url).json()

    json_status = json_data['status']
    print ('API Status: ' + json_status)
    print()

    if json_status == 'OK':
        for each in json_data['foods'][0]['food_name']:
            print (each['food_name'])

        nf_calories = json_data['foods'][0]['nf_calories']
        print()
        print(nf_calories)
