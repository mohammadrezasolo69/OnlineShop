from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('category/<slug>', views.CategoryFilterView.as_view(), name='category_list'),
    path('detail/<pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('like/<pk>', views.LikeView.as_view(), name='product_like'),
    path('favourite/<pk>', views.FavouriteView.as_view(), name='product_favourite'),
    path('favourites/', views.ListFavouritesView.as_view(), name='products_favourites_users'),
    path('category-list/', views.CategoryView.as_view(), name='category_partial'),
    path('search/', views.SearchView.as_view(), name='search'),
]
