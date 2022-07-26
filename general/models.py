"""

    The models of this app are only for inheritance and include common fields between all models

"""

from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated')
    active = models.BooleanField(default=False)
