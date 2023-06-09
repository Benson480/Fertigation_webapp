# Generated by Django 4.1.7 on 2023-05-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_fertilizer_detail_supplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fertilizer_element',
            old_name='composition',
            new_name='composition1',
        ),
        migrations.AddField(
            model_name='fertilizer_element',
            name='composition2',
            field=models.FloatField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizer_element',
            name='composition3',
            field=models.FloatField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizer_element',
            name='composition4',
            field=models.FloatField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizer_element',
            name='composition5',
            field=models.FloatField(db_index=True, null=True),
        ),
    ]
