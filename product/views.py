from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product, Category
from django.urls import reverse
from django.http import Http404


class ProductListView(generic.ListView):
    template_name = 'product/list_product.html'
    queryset = Product.objects.filter(active=True)
    paginate_by = 12


class ProductDetailView(generic.DetailView):
    template_name = 'product/detail_product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Product.objects.related_product(self.object)
        return context


class CategoryFilterView(generic.ListView):
    template_name = 'product/category_filter.html'
    paginate_by = 12

    def get_queryset(self):
        global slug
        slug = self.kwargs.get('slug')
        qs = Product.objects.filter(active=True, category__slug=slug)
        if qs is not None:
            return qs
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = slug
        return context


class CategoryView(generic.ListView):
    template_name = 'product/category_list.html'
    queryset = Category.objects.get_parent_categories()


class SearchView(generic.ListView):
    template_name = 'product/list_product.html'
    paginate_by = 12

    def get_queryset(self):
        global query_param
        query_param = self.request.GET.get('search')
        qs = Product.objects.search(query_param)
        if qs is not None:
            return qs
        return Product.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = query_param
        return context


class LikeView(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        url = request.META.get('HTTP_REFERER')
        product = Product.objects.get(id=pk)
        if product is None:
            raise Http404

        user = request.user
        if product.like.filter(id=user.id).exists():
            product.like.remove(user)
        else:
            product.like.add(user)
        return redirect(url)


class FavouriteView(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        url = request.META.get('HTTP_REFERER')
        product = Product.objects.get(id=pk)
        if product is None:
            raise Http404
        user = request.user.id
        if product.favourite.filter(id=user).exists():
            product.favourite.remove(user)
        else:
            product.favourite.add(user)
        return redirect(url)


class ListFavouritesView(LoginRequiredMixin, generic.ListView):
    template_name = 'product/favourite_users.html'

    def get_queryset(self):
        products = Product.objects.filter(favourite=self.request.user.id)
        return products
