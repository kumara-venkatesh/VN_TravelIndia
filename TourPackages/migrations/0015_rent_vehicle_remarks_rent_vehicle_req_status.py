# Generated by Django 4.0.4 on 2022-08-14 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourPackages', '0014_rent_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent_vehicle',
            name='remarks',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='rent_vehicle',
            name='req_Status',
            field=models.CharField(choices=[('Requested', 'Requested'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default=None, max_length=10),
        ),
    ]