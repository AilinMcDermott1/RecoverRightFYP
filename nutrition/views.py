from django.shortcuts import render
import requests
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NutritionForm, ExerciseForm
import subprocess as sp
from django.http import JsonResponse
from django.db.models import Count, Q
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View, TemplateView
from django.contrib.auth import get_user_model
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


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


User = get_user_model()

class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'nutrition/chart.html', {"users": 10})

def get_data(request, *args, **kwargs):
    data = {
        "calories_in": 200,
        "calories_out": 300
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 12, 22, 13, 11, 15]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

def meals(request):
    args = {"user": request.user}
    return render(request, 'nutrition/meals.html', args)

# class ChartView(TemplateView):
#     template_name = 'nutrition/chart.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ChartView, self).get_context_data(**kwargs)
#         context['30_day_registrations'] = self.thirty_day_registrations()
#         return context
#
#     def thirty_day_registrations(self):
#         final_data = []
#
#         # date = arrow.now()
#         for day in xrange(1, 30):
#             date = date.replace(days=-1)
#             count = User.objects.filter(
#                 date_joined__gte=date.floor('day').datetime,
#                 date_joined__lte=date.ceil('day').datetime).count()
#             final_data.append(count)
#
#         return final_data


# class LineChartJSONView(BaseLineChartView):
#     def get_labels(self):
#         """Return 7 labels for the x-axis."""
#         return ["January", "February", "March", "April", "May", "June", "July"]
#
#     def get_providers(self):
#         """Return names of datasets."""
#         return ["Central", "Eastside", "Westside"]
#
#     def get_data(self):
#         """Return 3 datasets to plot."""
#
#         return [[75, 44, 92, 11, 44, 95, 35],
#                 [41, 92, 18, 3, 73, 87, 92],
#                 [87, 21, 94, 3, 90, 13, 65]]
#
#
# line_chart = TemplateView.as_view(template_name='nutrition/chart.html')
# # line_chart_json = LineChartJSONView.as_view()


