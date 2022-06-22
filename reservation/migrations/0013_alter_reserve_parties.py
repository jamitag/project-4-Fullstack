# Generated by Django 3.2 on 2022-06-22 11:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0012_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='parties',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(6)]),
        ),
    ]
