# Generated by Django 4.1 on 2022-08-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
