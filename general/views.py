from django.shortcuts import render
from django.views import generic

from general.models import Slider
from product.models import Category


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

        context = {
            'sliders': sliders,
            'baner_category': baner_category
        }
        return render(request, self.templates_name, context)
