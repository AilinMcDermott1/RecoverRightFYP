from django.shortcuts import render
import requests
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NutritionForm

def nutritionix(request):
    search_result = {}
    if 'food' in request.POST:
        form = NutritionForm(request.POST)
        if form.is_valid():
            search_result = form.search()
    else:
        form = NutritionForm()
    return render(request, 'nutrition/nutrition.html', {'form': form, 'search_results': search_result})


# def naturalnutrients(request):
#     results = {}
#     if 'query' in request.POST:
#         form = NaturalNutritionForm(request.POST)
#         if form.is_valid():
#             results = form.search()
#     else:
#         form = NaturalNutritionForm()
#     return render(request, 'nutrition/nutrition.html', {'form': form, 'results': results})

