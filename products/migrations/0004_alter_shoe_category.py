# Generated by Django 5.1.1 on 2024-09-13 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('products', '0003_orders_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='categories.category'),
        ),
    ]