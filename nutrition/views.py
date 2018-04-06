from django.shortcuts import render
import requests
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NutritionForm, ExerciseForm

def nutritionix(request):
    search_result = {}
    if 'food' in request.POST:
        form = NutritionForm(request.POST)
        if form.is_valid():
            search_result = form.search()
    else:
        form = NutritionForm()
    return render(request, 'nutrition/nutrition.html', {'form': form, 'search_results': search_result})


def exercise(request):
    search_result2 = {}
    if 'exercise' in request.POST:
        form = ExerciseForm(request.POST)
        if form.is_valid():
            search_result2 = form.search2()
    else:
            form = ExerciseForm()
    return render(request, 'nutrition/exercise.html', {'form': form, 'search_results2': search_result2})

