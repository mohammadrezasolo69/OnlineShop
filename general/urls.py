from django.urls import path
from general import views

app_name = 'general'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('navbar/', views.NavbarView.as_view(), name='navbar')
]
