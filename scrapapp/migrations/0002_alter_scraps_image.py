# Generated by Django 4.2.7 on 2023-11-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scraps',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
