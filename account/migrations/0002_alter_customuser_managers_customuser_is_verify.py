# Generated by Django 4.0.6 on 2022-07-25 15:56

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_verify',
            field=models.DateTimeField(null=True),
        ),
    ]
