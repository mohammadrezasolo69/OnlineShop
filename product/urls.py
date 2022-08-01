from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('category/<slug>', views.CategoryFilterView.as_view(), name='category_list'),
    path('detail/<pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('category-list/', views.CategoryView.as_view(), name='category_partial'),
    path('search/', views.SearchView.as_view(), name='search'),
]
