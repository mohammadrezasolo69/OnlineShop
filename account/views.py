from django.shortcuts import render, redirect
from django.views import generic
from account.forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages


class LoginView(generic.View):
    form_class = LoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome to Panel', 'info')
                return redirect('account:login')
            messages.error(request, 'User with this profile was not found', 'warning')
        return render(request, self.template_name, {'form': form})


class RegisterView(generic.View):
    form_class = RegisterForm
    template_name = 'account/register.html'

    def get(self, request):
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
            messages.success(request, 'Welcome to OnlineShop', 'info')
            return redirect('account:login')
        messages.error(request, 'You have entered your mobile number or email or password incorrectly .', 'warning')
        return render(request, self.template_name, {'form': form})
