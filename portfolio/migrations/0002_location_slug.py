# Generated by Django 4.0.2 on 2022-02-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]