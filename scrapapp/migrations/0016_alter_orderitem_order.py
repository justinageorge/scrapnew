# Generated by Django 4.2.7 on 2024-02-23 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrapapp', '0015_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='scrapapp.order'),
        ),
    ]
