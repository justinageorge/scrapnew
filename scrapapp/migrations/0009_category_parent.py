# Generated by Django 5.0 on 2023-12-30 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapapp', '0008_category_scraps_user_bids_reviews_scrapsfeauture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scrapapp.category'),
        ),
    ]
