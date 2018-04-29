from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from account.models import UserProfileModel

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
        }

        # validate password...
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password2'] != ['password']:
                raise ValidationError("Passwords don't match")

            return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ('email', 'age', 'height', 'weight', 'bio', 'image')

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile




class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'username'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'password'}))


class UpdateProfile(forms.ModelForm):

    class Meta:
        model = UserProfileModel
        fields = ('email', 'age', 'height', 'weight', 'bio', 'image')


    # def clean_email(self):
    #     # username = self.cleaned_data.get('username')
    #     email = self.cleaned_data.get('email')
    #
    #     if email and User.objects.filter(email=email).count():
    #         raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
    #     return email

