# Generated by Django 5.0 on 2023-12-29 07:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapapp', '0007_rename_picture_scraps_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='scraps',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('reject', 'Reject'), ('pending', 'Pending'), ('accept', 'Accept')], default='pending', max_length=100)),
                ('scrap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrap_bid', to='scrapapp.scraps')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('rating', models.PositiveIntegerField(choices=[(1, '1star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')])),
                ('scrap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrap_review', to='scrapapp.scraps')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapsFeauture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images')),
                ('place', models.CharField(max_length=200)),
                ('created_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_feauture', to='scrapapp.category')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_scraps', to='scrapapp.scraps')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrap_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('profile_pics', models.ImageField(blank=True, null=True, upload_to='profilepics')),
                ('bio', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField()),
                ('scrap', models.ManyToManyField(related_name='wish', to='scrapapp.scraps')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrap_wish', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]