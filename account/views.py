from django.shortcuts import render, redirect
from django.views import generic
from account.forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


class LoginView(generic.View):
    form_class = LoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, 'account/login.html', {'form': form})

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
        return render(request, 'account/login.html', {'form': form})
