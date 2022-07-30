from django.shortcuts import render
from django.views import generic

from product.models import Category


class NavbarView(generic.View):
    template_name = 'inc/navbar.html'

    def get(self, request):
        qs = Category.objects.filter(active=True, is_sub=False)
        return render(request, self.template_name, {'categories': qs})


class Home(generic.View):
    templates_name = 'general/home.html'

    def get(self, request):
        return render(request, self.templates_name, {})
