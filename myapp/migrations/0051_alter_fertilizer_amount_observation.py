# Generated by Django 4.1.7 on 2023-08-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0050_fertilizer_amount_observation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizer_amount',
            name='Observation',
            field=models.TextField(blank=True, db_index=True, max_length=100, null=True),
        ),
    ]