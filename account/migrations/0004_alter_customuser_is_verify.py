# Generated by Django 4.0.6 on 2022-07-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_is_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_verify',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
