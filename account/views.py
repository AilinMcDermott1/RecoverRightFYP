from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView

from account.forms import RegisterUserForm, LoginForm, EditProfileForm
from account.models import UserProfileModel


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "account/register.html"


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        UserProfileModel.objects.create(user=user)
        # return render(request, 'account/profile.html', context_instance=RequestContext(request))
        # return HttpResponse('account/profile.html')
        return HttpResponseRedirect(reverse('account:profile'))
        # return render(request, 'account/profile.html', args)
        # success_url = reverse_lazy('account:profile.html')



class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('account:profile.html')


def profile(request):
    args = {"user": request.user}
    return render(request, 'account/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('account:profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/edit_profile.html', args)