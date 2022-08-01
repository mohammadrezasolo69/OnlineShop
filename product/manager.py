from django.db import models
from django.db.models import Q


class CategoryManager(models.Manager):
    def last_three_objects(self):
        return super().get_queryset().filter(active=True, is_sub=False).order_by('-id')[0:3]

    def get_parent_categories(self):
        return super().get_queryset().filter(active=True, is_sub=False)


class ProductManager(models.Manager):
    def search(self, query_param):
        lookup = (
                Q(title__icontains=query_param) |
                Q(description__icontains=query_param)
        )
        return super().get_queryset().filter(lookup, active=True).distinct()
