from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.cache import cache
from datetime import datetime
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, \
    PasswordResetDoneView, PasswordChangeView, PasswordChangeDoneView

from account.forms import (
    LoginForm, RegisterForm, ResetPasswordForm, ResetPasswordConfirmForm, ChangePasswordForm, ProfileEditForm,
    OtpVerifyRegisterForm
)
from account.utile.send_email import send_otp


# ////////////////////////////////// Login User \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class LoginView(generic.View):
    form_class = LoginForm
    template_name = 'account/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('account:profile')
        form = self.form_class

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            send_otp(request, cd['email'])

            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)

                messages.success(request, 'Welcome to Panel', 'info')
                return redirect('account:login')
            messages.error(request, 'User with this profile was not found', 'warning')
        return render(request, self.template_name, {'form': form})


# ////////////////////////////////// Register User \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class RegisterView(generic.View):
    form_class = RegisterForm
    template_name = 'account/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('account:profile')

        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = get_user_model().objects.create_user(
                email=cd['email'],
                phone_number=cd['phone_number'],
                full_name=cd['full_name'],
                password=cd['password']
            )

            send_otp(request, cd['email'])

            messages.success(request, 'Welcome to OnlineShop', 'info')
            return redirect('account:register_verify')
        messages.error(request, 'You have entered your mobile number or email or password incorrectly .', 'warning')
        return render(request, self.template_name, {'form': form})


class OtpVerifyRegisterView(generic.View):
    form_class = OtpVerifyRegisterForm
    template_name = 'account/verify_otp.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('account:profile')

        form = self.form_class
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = get_user_model().objects.get(email=cd['email'])

            if cache.get(f'otp_{cd["email"]}') is None:  # otp code expire
                messages.error(request, 'OTP code expire')
                user.delete()
                return redirect('account:register')

            else:  # otp code no expire
                if cd['code'] == cache.get(f'otp_{cd["email"]}'):  # send otp code ==  Code entered
                    user.is_verify = datetime.now()
                    user.is_active = True
                    user.save()
                    return redirect('account:login')
                else:  # send otp code !=  Code entered
                    messages.error(request, 'The entered code is incorrect')
                    return redirect('account:register_verify')

        return render(request, self.template_name, {'form': form})


# ////////////////////////////////// Logout User \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class LogoutView(LoginRequiredMixin, generic.View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have successfully logged out .', 'success')
        return redirect('account:login')


# ////////////////////////////////// Password Reset User \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class ResetPasswordView(PasswordResetView):
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_send_email.html'
    form_class = ResetPasswordForm
    success_url = reverse_lazy('account:password_reset_done')


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = "account/password_reset_done.html"


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    form_class = ResetPasswordConfirmForm
    success_url = reverse_lazy("account:password_reset_complete")


class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


# ////////////////////////////////// Password Change \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('account:password_change_done')


class ChangePasswordDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'


# ///////////////////////////////////// Profile User \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class ProfileView(LoginRequiredMixin, generic.View):
    template_name = 'account/profile.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = ProfileEditForm
    template_name = 'account/profile_edit.html'
    success_url = reverse_lazy('account:profile')
