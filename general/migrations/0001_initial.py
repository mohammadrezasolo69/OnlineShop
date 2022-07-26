# Generated by Django 4.0.6 on 2022-07-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads/Sliders')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
    ]
