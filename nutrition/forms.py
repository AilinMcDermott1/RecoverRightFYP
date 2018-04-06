from django import forms
from django.http import HttpResponse
from django.conf import settings
import requests
import json

class NutritionForm(forms.Form):
    food = forms.CharField(max_length=100000)

    def search(self):
        # result = {}
        food = self.cleaned_data['food']

        headers = {
            'x-app-id': "ff0ccea8",
            'x-app-key': "605660a17994344157a78f518a111eda",
            'x-remote-user-id': "7a43c5ba-50e7-44fb-b2b4-bbd1b7d22632",
            'Content-Type': "application/x-www-form-urlencoded",

        }

        url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        body = {
            'query': food,
            'timezone': 'US/Eastern',
        }
        response = requests.request("POST", url, data=body, headers=headers)
        data = response.json()

        print ('food name: ', data['foods'][0]['food_name'])
        print ('food calories: ', data['foods'][0]['nf_calories'])
        print ('food protein: ', data['foods'][0]['nf_protein'])
        print ('food fats: ', data['foods'][0]['nf_total_fat'])
        # print(response.json())



class ExerciseForm(forms.Form):
    exercise = forms.CharField(max_length=1000000)

    def search2(self):
        exercise = self.cleaned_data['exercise']

        headers = {
            'x-app-id': "ff0ccea8",
            'x-app-key': "605660a17994344157a78f518a111eda",
            'Content-Type': "application/x-www-form-urlencoded",
        }

        url = "https://trackapi.nutritionix.com/v2/natural/exercise"
        body = {
            'query': exercise
        }



        response = requests.request("POST", url, data=body, headers=headers)
        data = response.json()

        print ('exercise name: ', data['exercises'][0]['user_input'])
        print ('exercise duration: ', data['exercises'][0]['duration_min'])
        print ('calories burned: ', data['exercises'][0]['nf_calories'])


