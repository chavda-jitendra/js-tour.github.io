# Generated by Django 5.1.3 on 2025-02-07 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_tour_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, upload_to='tour_images/'),
        ),
    ]
