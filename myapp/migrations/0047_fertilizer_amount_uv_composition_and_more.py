# Generated by Django 4.1.7 on 2023-08-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0046_alter_uploadedimage_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizer_amount',
            name='Uv_Composition',
            field=models.FloatField(blank=True, db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fertilizer_amount',
            name='Uv_Element',
            field=models.CharField(blank=True, choices=[('Nitrate', 'Nitrate [NO3N]'), ('Phosphorus', 'Phosphorus [P]'), ('Potassium', 'Potassium [K]'), ('Calcium', 'Cacium [Ca]'), ('Magnesium', 'Magnesium [Mg]'), ('Sulphur', 'Sulphur [S]'), ('Ammoniacal N', 'Ammoniacal N [NH4N]'), ('Iron', 'Iron [Fe]'), ('Manganese', 'Manganese [Mn]'), ('Copper', 'Copper [Cu]'), ('Boron', 'Boron [B]'), ('Zinc', 'Zinc [Zn]'), ('Molybdenum', 'Molybdenum [Mo]')], db_index=True, max_length=200, null=True),
        ),
    ]