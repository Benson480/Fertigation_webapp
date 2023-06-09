# Generated by Django 4.1.7 on 2023-06-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_remove_fertilizer_cost_fertilizer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fertilizer_amount',
            old_name='amount',
            new_name='Amount',
        ),
        migrations.RenameField(
            model_name='fertilizer_amount',
            old_name='Water_Volume_m3',
            new_name='H2O_m3_Per_Ha',
        ),
        migrations.AddField(
            model_name='fertilizer_amount',
            name='Area_Ha',
            field=models.FloatField(blank=True, db_index=True, default=0, null=True),
        ),
    ]
