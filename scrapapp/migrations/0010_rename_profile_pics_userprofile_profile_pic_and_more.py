# Generated by Django 5.0 on 2023-12-30 11:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapapp', '0009_category_parent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_pics',
            new_name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AlterField(
            model_name='scraps',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
