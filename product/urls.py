from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('categort-list/', views.CategoryView.as_view(), name='category_partial'),
    path('search/', views.SearchView.as_view(), name='search'),
]
