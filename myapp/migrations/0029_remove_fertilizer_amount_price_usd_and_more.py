# Generated by Django 4.1.7 on 2023-06-16 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_alter_fertilizer_amount_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizer_amount',
            name='price_Usd',
        ),
        migrations.AddField(
            model_name='fertilizer_price',
            name='Date',
            field=models.DateField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizer_price',
            name='price_Usd',
            field=models.FloatField(blank=True, db_index=True, default=0, null=True),
        ),
    ]
