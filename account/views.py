from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, UpdateView
from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from account.forms import RegisterUserForm, LoginForm,  UpdateProfile, UserProfileForm
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
        # UserProfileModel.objects.create(user=user)
        login(self.request, user)


        return HttpResponseRedirect(reverse('account:profile'))

        # profile = form.save(commit=False)
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = User.objects.create_user(username=username, password=password)
        # profile.user = user
        # profile.save()
        # UserProfileModel.objects.create(user=user)
        #
        # return HttpResponseRedirect(reverse('account:profile'))



class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('account:profile.html')


def profile(request):
    args = {"user": request.user}
    return render(request, 'account/profile.html', args)


# def edit_profile(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('account:profile'))
#     else:
#         form = UserChangeForm(instance=request.user)
#         args = {'form': form}
#         return render(request, 'account/edit_profile.html', args)

def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('account:profile'))
            return render(request, 'account/profile.html')
    else:
        form = UpdateProfile()
        if request.user.is_authenticated():
            form = UpdateProfile(instance=request.user)
        args['form'] = form
        return render(request, 'account/edit_profile.html', args)

# class EditUserProfileView(UpdateView): #Note that we are using UpdateView and not FormView
#     model = UserProfileModel
#     form_class = UserProfileForm
#     template_name = "account/profile.html"
#
#     def get_object(self, *args, **kwargs):
#         user = get_object_or_404(User, pk=self.kwargs['username'])
#
#         # We can also get user object using self.request.user  but that doesnt work
#         # for other models.
#
#         return user.userprofilemodel
#
#     def get_success_url(self, *args, **kwargs):
#         return reverse("account/edit_profile.html")

# class UserEditProfileView(LoginRequiredMixin,UpdateView):
#     login_url = '/'
#     model = UserProfileModel
#     fields = [
#         'first_name',
#         'last_name',
#         'email',
#         'age',
#         'height',
#         'weight',
#         ]
#     template_name_suffix = 'account:edit_profile.html'
#
#     def get_success_url(self):
#         userid = self.kwargs['pk']
#         return reverse_lazy('account:profile.html', kwargs={'pk': userid})