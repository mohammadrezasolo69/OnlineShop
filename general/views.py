from django.shortcuts import render
from django.views import generic

from general.models import Slider
from product.models import Category, Product


class NavbarView(generic.View):
    template_name = 'inc/navbar.html'

    def get(self, request):
        qs = Category.objects.filter(active=True, is_sub=False)
        return render(request, self.template_name, {'categories': qs})


class Home(generic.View):
    """ Slider , new Product , discount Product ... """

    templates_name = 'general/home.html'

    def get(self, request):
        sliders = Slider.objects.filter(active=True)
        baner_category = Category.objects.last_three_objects()
        new_products = Product.objects.get_new_product()
        discount_products = Product.objects.get_discount_product()

        context = {
            'sliders': sliders,
            'baner_category': baner_category,
            'new_product': new_products,
            'discount_product': discount_products
        }
        return render(request, self.templates_name, context)
