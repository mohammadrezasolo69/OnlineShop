from django.shortcuts import render
from django.views import generic
from product.models import Product, Category


class ProductListView(generic.ListView):
    template_name = 'product/list_product.html'
    queryset = Product.objects.filter(active=True)
    paginate_by = 12


class CategoryView(generic.ListView):
    template_name = 'product/category_list.html'
    queryset = Category.objects.get_parent_categories()


class SearchView(generic.ListView):
    template_name = 'product/list_product.html'
    paginate_by = 12

    def get_queryset(self):
        query_param = self.request.GET.get('search')
        qs = Product.objects.search(query_param)
        if qs is not None:
            return qs
        return Product.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context
