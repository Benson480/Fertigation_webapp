# Generated by Django 4.1.7 on 2023-08-11 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0051_alter_fertilizer_amount_observation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fertilizer_amount',
            old_name='Amount',
            new_name='Fertilizer_Amount',
        ),
    ]
