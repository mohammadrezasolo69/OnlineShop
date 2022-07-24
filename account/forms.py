from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator

messages = {
    'required': ' This field is required.',
    'invalid': 'The email entered is not valid.',
}


# ////////////////////// Admin Panel \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'phone_number', 'full_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'phone_number', 'full_name', 'password')


# ///////////////////// Login User \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="The entered mobile phone is not valid")


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', error_messages=messages,
                             widget=forms.EmailInput(
                                 attrs={
                                     "id": "form1Example13",
                                     "class": "form-control form-control-lg",
                                     'placeholder': 'enter your email address . ',
                                 }))

    password = forms.CharField(label='Password', validators=[phone_regex], error_messages=messages,
                               widget=forms.PasswordInput(attrs={
                                   "id": "form1Example13",
                                   "class": "form-control form-control-lg",
                                   'placeholder': 'enter your email address . ',
                               }))
