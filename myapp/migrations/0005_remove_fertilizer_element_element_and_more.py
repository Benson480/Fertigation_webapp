# Generated by Django 4.1.7 on 2023-05-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_composition_fertilizer_element_composition1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizer_element',
            name='element',
        ),
        migrations.AddField(
            model_name='fertilizer_element',
            name='element1',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fertilizer_element',
            name='element2',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fertilizer_element',
            name='element3',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fertilizer_element',
            name='element4',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fertilizer_element',
            name='element5',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]
