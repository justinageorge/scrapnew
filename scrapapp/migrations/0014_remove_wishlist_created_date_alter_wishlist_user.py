# Generated by Django 4.2.7 on 2024-02-20 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scrapapp', '0013_alter_scrapsfeauture_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='scrap_wish', to=settings.AUTH_USER_MODEL),
        ),
    ]
