from django.urls import path,include
from account import views

app_name = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),

]
