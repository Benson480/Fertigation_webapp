# Generated by Django 4.1.7 on 2023-06-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_fertilizer_detail_fertilizer_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fertilizer_amount',
            old_name='container',
            new_name='Fertilizer_Product',
        ),
        migrations.AddField(
            model_name='fertilizer_amount',
            name='registeredDate',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
    ]
