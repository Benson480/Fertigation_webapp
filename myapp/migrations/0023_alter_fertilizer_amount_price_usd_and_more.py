# Generated by Django 4.1.7 on 2023-06-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_rename_container_fertilizer_detail_fertilizer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizer_amount',
            name='Price_USD',
            field=models.FloatField(blank=True, db_index=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='fertilizer_amount',
            name='amount',
            field=models.FloatField(blank=True, db_index=True, default=0, null=True),
        ),
    ]
