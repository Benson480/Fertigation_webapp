# Generated by Django 4.1.7 on 2023-05-22 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_composition_fertilizer_element_composition1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizer_element',
            name='composition4',
            field=models.FloatField(db_index=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='fertilizer_element',
            name='element4',
            field=models.CharField(db_index=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fertilizer_element',
            name='composition3',
            field=models.FloatField(db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='fertilizer_element',
            name='element3',
            field=models.CharField(db_index=True, default=None, max_length=200, null=True),
        ),
    ]
