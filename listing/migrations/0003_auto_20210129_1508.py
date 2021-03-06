# Generated by Django 2.1.7 on 2021-01-29 13:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20210129_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='availableDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image3',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image4',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image5',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image6',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image7',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image8',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='numberOfBathrooms',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='numberOfBedrooms',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='suburb',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='listing.Suburb'),
        ),
    ]
