from django.contrib import admin
from general.models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass
