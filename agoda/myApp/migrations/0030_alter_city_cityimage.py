# Generated by Django 5.0.1 on 2024-01-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0029_alter_city_cityimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='cityimage',
            field=models.ImageField(height_field='media/none', upload_to='city_images', verbose_name='Şehir Resmi', width_field='media/none'),
        ),
    ]