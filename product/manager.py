from django.db import models


class CategoryManager(models.Manager):
    def last_three_objects(self):
        return super().get_queryset().filter(active=True, is_sub=False).order_by('-id')[0:3]
