# Generated by Django 4.1.7 on 2023-05-22 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_fertilizer_element_element_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fertilizer_element',
            old_name='composition1',
            new_name='composition',
        ),
        migrations.RenameField(
            model_name='fertilizer_element',
            old_name='element1',
            new_name='element',
        ),
        migrations.RemoveField(
            model_name='fertilizer_element',
            name='composition2',
        ),
        migrations.RemoveField(
            model_name='fertilizer_element',
            name='composition3',
        ),
        migrations.RemoveField(
            model_name='fertilizer_element',
            name='composition4',
        ),
        migrations.RemoveField(
            model_name='fertilizer_element',
            name='composition5',
        ),
        migrations.RemoveField(
            model_name='fertilizer_element',
            name='element2',
        ),
        migrations.RemoveField(
            model_name='fertilizer_element',
            name='element3',
        ),
        migrations.RemoveField(
            model_name='fertilizer_element',
            name='element4',
        ),
        migrations.RemoveField(
            model_name='fertilizer_element',
            name='element5',
        ),
    ]
