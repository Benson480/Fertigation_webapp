# Generated by Django 4.1.7 on 2023-07-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_fertilizer_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='fertilizer_amount',
            name='Media',
            field=models.CharField(choices=[('Hydroponics', 'Hydroponics'), ('Soil', 'Soil')], max_length=255),
        ),
    ]
