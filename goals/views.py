from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Goal
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib import request





# def goal_list(request):
#     goals = Goal.objects.all().order_by('start_date')
#     return render(request, 'goals/goal_list.html', { 'goals': goals })


def goal_detail(request, slug):
    # return HttpResponse(slug)
    goal = Goal.objects.get(slug=slug)
    # form.instance.goal = Goal.objects.get(slug=self.kwargs['slug'])
    return render(request, 'goals/goal_detail.html', { 'goal': goal })

@login_required
def goal_create(request, *args):
    if request.method == 'POST':
        form = forms.CreateGoal(request.POST, request.FILES)
        if form.is_valid():
            goal_create = Post(CreateGoal.title.data, CreateGoal.text.data)
            # save article to db

            return redirect('goals:list')
    else:
        form = forms.CreateGoal()
    return render(request, 'goals/goal_create.html', {'form': form})


# @login_required(login_url="/account/login/")
class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = 'goals'

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)