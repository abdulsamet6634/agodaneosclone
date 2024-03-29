# Generated by Django 5.0.1 on 2024-01-18 20:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0024_hotel_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Şehir İsmi')),
                ('cityimage', models.ImageField(upload_to=None, verbose_name='Şehir Resmi')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
