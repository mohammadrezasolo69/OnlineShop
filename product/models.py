from general.models import BaseModel
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django.core.validators import MaxValueValidator

from product.manager import CategoryManager
from product.utile.slug_generetor import unique_slug_generator


# ------------------------------ Product Model -------------------------------------------------------------------------
class Product(BaseModel):
    class TypeChoices(models.TextChoices):
        new = 'new'
        discount = 'discount'
        normal = 'normal'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    title = models.CharField(max_length=300)
    short_description = models.TextField(max_length=500)
    description = models.TextField()  # todo : TextFields => CKEditor
    slug = models.SlugField(unique=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='uploads/products/thumbnail_image')
    thumbnail_image_alt = models.CharField(max_length=300, blank=True)
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    type = models.CharField(max_length=200, choices=TypeChoices.choices, default=TypeChoices.new)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='products')
    tags = TaggableManager()

    @property
    def discount_price_finally(self):
        price_finally = int(self.price * (100 - self.discount) / 100)
        return price_finally


@receiver(pre_save, sender=Product)
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_image_alt:
        instance.thumbnail_image_alt = instance.title


# ------------------------------ Variant Model -------------------------------------------------------------------------

class Variant(BaseModel):
    class Meta:
        verbose_name = 'Variant'
        verbose_name_plural = 'Variants'

    def __str__(self):
        return self.product.title

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='variants')
    size = models.ForeignKey('Size', on_delete=models.CASCADE, related_name='variants')
    color = models.ForeignKey("Color", on_delete=models.CASCADE, related_name='variants')
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name='variants')
    quantity = models.PositiveIntegerField(default=0)


# ------------------------------ Size Model -------------------------------------------------------------------------
class Size(BaseModel):
    def __str__(self):
        return self.size

    size = models.CharField(max_length=200, blank=True, null=True)


# ------------------------------ Color Model -------------------------------------------------------------------------
class Color(BaseModel):
    def __str__(self):
        return self.color

    color = models.CharField(max_length=300, blank=True, null=True)


# -------------------------------- Brand Model ----------------------------------------------------------------------
class Brand(BaseModel):
    def __str__(self):
        return self.brand

    brand = models.CharField(max_length=300, blank=True, null=True)


# ------------------------------ Gallery Model -------------------------------------------------------------------------

class Gallery(BaseModel):
    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='galleries')
    image = models.ImageField(upload_to='uploads/Galleries/images')


# -------------------------------- Category Model ----------------------------------------------------------------------
class Category(BaseModel):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='uploads/Galleries/images', blank=True)
    is_sub = models.BooleanField(default=False)

    objects = CategoryManager()


@receiver(pre_save, sender=Category)
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# -------------------------------- Category Model ----------------------------------------------------------------------
class Comment(BaseModel):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()  # todo :  TextFields => CKEditor
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)

# ----------------------------------------------------------------------------------------------------------------------
