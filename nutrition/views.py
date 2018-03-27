from django.shortcuts import render
import requests
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NutritionForm

def nutritionix(request):
    search_result = {}
    if 'food' in request.GET:
        form = NutritionForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = NutritionForm()
    return render(request, 'nutrition/nutrition.html', {'form': form, 'search_results': search_result})
