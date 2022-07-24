from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator
from django.core import validators
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

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
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', error_messages=messages,
                             widget=forms.EmailInput(
                                 attrs={
                                     "id": "form1Example13",
                                     "class": "form-control form-control-lg",
                                     'placeholder': 'enter your email address . ',
                                 }))

    password = forms.CharField(label='Password', error_messages=messages,
                               widget=forms.PasswordInput(attrs={
                                   "id": "form1Example13",
                                   "class": "form-control form-control-lg",
                                   'placeholder': 'enter your password . ',
                               }))


# /////////////////// Register User \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="The entered mobile phone is not valid")


class RegisterForm(LoginForm):
    phone_number = forms.CharField(
        label='Phone Number', error_messages=messages,
        validators=[
            phone_regex,
            validators.MaxLengthValidator(limit_value=11, message="Mobile number cannot be more than 11 characters."),
            validators.MinLengthValidator(limit_value=11, message="Mobile number cannot be less than 11 characters."),
        ],
        widget=forms.TextInput(attrs={
            "id": "form1Example13",
            "class": "form-control form-control-lg",
            'placeholder': 'enter your phone number . ',
        }))

    full_name = forms.CharField(label='FullName', error_messages=messages,
                                widget=forms.TextInput(attrs={
                                    "id": "form1Example13",
                                    "class": "form-control form-control-lg",
                                    'placeholder': 'enter your full name . ',
                                }))

    password2 = forms.CharField(label='Confirm Password', error_messages=messages,
                                widget=forms.PasswordInput(attrs={
                                    "id": "form1Example13",
                                    "class": "form-control form-control-lg",
                                    'placeholder': 'enter your confirm password . ',
                                }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValueError('The entered email is duplicate')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if get_user_model().objects.filter(email=phone_number).exists():
            raise ValueError('The entered phone_number is duplicate')
        return phone_number

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if (password2 and password) and (password2 != password):
            raise ValueError('Password and confirm password do not match')
        return password2


# ////////////////////////////////// Password Reset User \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label='Email', error_messages=messages,
                             widget=forms.EmailInput(
                                 attrs={
                                     "id": "form1Example13",
                                     "class": "form-control form-control-lg",
                                     'placeholder': 'enter your email address . ',
                                 }))


class ResetPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', error_messages=messages,
                               widget=forms.PasswordInput(attrs={
                                   "id": "form1Example13",
                                   "class": "form-control form-control-lg",
                                   'placeholder': 'enter your password . ',
                               }))

    new_password2 = forms.CharField(label='Confirm Password', error_messages=messages,
                                widget=forms.PasswordInput(attrs={
                                    "id": "form1Example13",
                                    "class": "form-control form-control-lg",
                                    'placeholder': 'enter your confirm password . ',
                                }))

    def clean_password2(self):
        new_password1 = self.cleaned_data['new_password1']
        new_password2 = self.cleaned_data['new_password2']
        if new_password2 != new_password1:
            raise ValueError('Password and confirm password do not match')
        return new_password2
