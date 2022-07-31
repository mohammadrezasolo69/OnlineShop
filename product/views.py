from django.shortcuts import render
from django.views import generic
from product.models import Product


class ProductListView(generic.ListView):
    template_name = 'product/list_product.html'
    queryset = Product.objects.filter(active=True)
    paginate_by = 12
