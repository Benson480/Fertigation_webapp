# Generated by Django 4.1.7 on 2023-06-17 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_remove_fertilizer_amount_price_usd_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizer_cost',
            name='Fertilizer',
        ),
    ]