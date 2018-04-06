import requests
import json


url = "https://trackapi.nutritionix.com/v2/natural/exercise"

body = {

    # "query=ran%205%20miles"
    'query' : '5 mile run'

}

headers = {
    'x-app-id': "ff0ccea8",
    'x-app-key': "605660a17994344157a78f518a111eda",
    'Content-Type': "application/x-www-form-urlencoded",
    }

response = requests.request("POST", url, data=body, headers=headers)



data = response.json()

print ('exercise name: ', data['exercises'][0]['user_input'])
print ('exercise duration: ', data['exercises'][0]['duration_min'])
print ('calories burned: ', data['exercises'][0]['nf_calories'])
# print ('food calories: ', data['foods'][0]['nf_total_fat'])

print(response.text)