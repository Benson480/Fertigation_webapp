# Generated by Django 4.1.7 on 2023-06-08 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_fertilizer_amount_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizer_amount',
            name='Media',
            field=models.CharField(choices=[('HYDROPONICS', 'HYDROPONICS'), ('SOIL', 'SOIL')], max_length=255),
        ),
        migrations.CreateModel(
            name='Fertilizer_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price_USD', models.FloatField(blank=True, db_index=True, null=True)),
                ('Fertilizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fertilizer')),
            ],
        ),
        migrations.CreateModel(
            name='Fertilizer_Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fertilizers_Cost_USD', models.FloatField(db_index=True, null=True)),
                ('Fertilizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fertilizer')),
            ],
        ),
    ]
