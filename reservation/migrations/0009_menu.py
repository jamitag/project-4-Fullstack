# Generated by Django 3.2 on 2022-06-21 09:39

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_remove_reserve_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image')),
            ],
        ),
    ]