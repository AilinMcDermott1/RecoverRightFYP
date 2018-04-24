from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Goal
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib import request
from .forms import CreateGoal
from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404
from django.contrib import messages




@login_required
def goal_list(request):
    # goals = Goal.objects.all().order_by('created_data')
    goals = Goal.objects.filter(user=request.user).order_by('created_data')
    return render(request, 'goals/goal_list.html', { 'goals': goals })


def goal_detail(request, title):
    goal = Goal.objects.get(title)
    return render(request, 'goals/goal_detail.html', { 'goals': goals })


@login_required
def goal_create(request, *args):
    if request.method == 'POST':
        form = forms.CreateGoal(request.POST, request.FILES)
        if form.is_valid():
            goal_create = form.save(commit=False)
            goal_create.user = request.user
            goal_create.save()

            # save goal to db

            return redirect('goals:goal_list')
    else:
        form = forms.CreateGoal()
    return render(request, 'goals/goal_create.html', {'form': form})



def goals_delete(request, id=None):
    goal = get_object_or_404(Goal, id=id)

    creator = goal.user.username

    if request.method == "POST" and request.user.is_authenticated and request.user.username == creator:
        goal.delete()
        messages.success(request, "Goal successfully deleted!")
        return redirect('goals:goal_list')

    context = {'goal': goal,
               'creator': creator,
               }

    return render(request, 'goals/delete_goal.html', context)

