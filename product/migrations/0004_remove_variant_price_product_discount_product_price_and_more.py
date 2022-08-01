# Generated by Django 4.0.6 on 2022-07-31 07:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_is_sub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]