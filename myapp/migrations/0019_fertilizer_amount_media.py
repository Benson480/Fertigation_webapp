# Generated by Django 4.1.7 on 2023-06-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_rename_watervolume_m3_fertilizer_amount_water_volume_m3'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizer_amount',
            name='Media',
            field=models.CharField(choices=[('HYDROPONICS', 'SOIL')], default='HYDROPONICS', max_length=255),
        ),
    ]
