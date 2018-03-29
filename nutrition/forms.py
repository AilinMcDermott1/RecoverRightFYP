from django import forms
from django.http import HttpResponse
from django.conf import settings
import requests
import json

class NutritionForm(forms.Form):
    food = forms.CharField(max_length=250)

    def search(self):
        # result = {}
        food = self.cleaned_data['food']

        headers = {
            'x-app-id': "ff0ccea8",
            'x-app-key': "605660a17994344157a78f518a111eda",
            'x-remote-user-id': "7a43c5ba-50e7-44fb-b2b4-bbd1b7d22632",
        }

        url = 'https://trackapi.nutritionix.com/v2/search/instant?'
        body = {'query': food}
        response = requests.request("GET", url, params=body, headers=headers)
        data = response.json()

        print ('food name: ', data['branded'][0]['food_name'])
        print ('food calories: ', data['branded'][0]['nf_calories'])
        print ('food brand: ', data['branded'][0]['brand_name'])




