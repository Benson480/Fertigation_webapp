# Generated by Django 4.1.7 on 2024-03-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0058_rename_about_image_uploadedimage_about_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='file',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
