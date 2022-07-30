from django.contrib import admin
from product.models import Product, Variant, Size, Color, Price, Brand, Category, Gallery
from django.utils.html import format_html


# ----------------------------------------- Inlines --------------------------------------------------------------------
class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1


# ---------------------------------------------------------------------------------------------------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'tag_list', 'active', 'thumbnail_image_tag')
    list_filter = ('category', 'active')
    list_editable = ('active',)
    search_fields = ('title', 'category')
    inlines = [VariantInline, GalleryInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u" , ".join(o.name for o in obj.tags.all())

    def thumbnail_image_tag(self, obj):
        return format_html('<img src="{}" style="width: 120px;border-radius: 15px;" />'.format(obj.thumbnail_image.url))

    thumbnail_image_tag.short_description = 'image'


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
