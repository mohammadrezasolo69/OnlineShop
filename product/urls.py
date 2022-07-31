from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list')
]
