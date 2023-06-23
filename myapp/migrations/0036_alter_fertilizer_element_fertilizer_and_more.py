# Generated by Django 4.1.7 on 2023-06-23 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_dictionary_alter_fertilizer_element_fertilizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizer_element',
            name='Fertilizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fertilizer'),
        ),
        migrations.DeleteModel(
            name='Dictionary',
        ),
    ]