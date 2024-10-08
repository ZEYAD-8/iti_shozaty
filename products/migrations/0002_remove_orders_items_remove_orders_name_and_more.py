# Generated by Django 5.1.1 on 2024-09-11 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='items',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='order_id',
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(default=30, on_delete=django.db.models.deletion.CASCADE, to='products.shoe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('delivered', 'Delivered'), ('in_delivery', 'In Delivery'), ('received', 'Received')], default='received', max_length=20),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
    ]