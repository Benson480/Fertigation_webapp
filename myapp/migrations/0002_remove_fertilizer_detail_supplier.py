# Generated by Django 4.1.7 on 2023-05-22 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizer_detail',
            name='supplier',
        ),
    ]
