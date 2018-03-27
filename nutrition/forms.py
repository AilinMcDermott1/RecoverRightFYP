from django import forms
from django.conf import settings
import requests
import json

class NutritionForm(forms.Form):
    food = forms.CharField(max_length=250)
    # nf_calories = forms.DecimalField()

    def search(self):
        result = {}
        food = self.cleaned_data['food']
        endpoint = 'https://trackapi.nutritionix.com/v2/search?{item_id}'
        url = endpoint.format(item_id=food)
        headers = {'app_id': settings.NUTRITIONIX_APP_ID, 'app_key': settings.NUTRITIONIX_APP_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200: #SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:
                result['message'] = 'No entry found for "%s"' % food
            else:
                result['message'] = 'The Nutritionix API is not available at the moment. Please try again later.'
        return result
