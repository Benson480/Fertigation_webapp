# Generated by Django 4.1.7 on 2023-08-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0043_fertilizer_supplier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizer_amount',
            name='Fertigation_line',
            field=models.CharField(choices=[('Line 01', 'Line 01'), ('Line 02', 'Line 02'), ('Line 03', 'Line 03'), ('Line 04', 'Line 04'), ('Line 05', 'Line 05'), ('Line 06', 'Line 06')], db_index=True, max_length=255, null=True),
        ),
    ]
