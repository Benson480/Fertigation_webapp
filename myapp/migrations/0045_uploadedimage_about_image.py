# Generated by Django 4.1.7 on 2023-08-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0044_fertilizer_amount_fertigation_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='about_Image',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True),
        ),
    ]
