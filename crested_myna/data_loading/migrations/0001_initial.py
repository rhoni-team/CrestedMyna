# Generated by Django 5.1.1 on 2024-11-04 21:45

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklist_id', models.CharField(max_length=100)),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('location', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=2)),
                ('country_code', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('state_code', models.CharField(max_length=150)),
                ('observation_date', models.DateField()),
                ('year', models.IntegerField(null=True)),
                ('observation_count', models.IntegerField(blank=True, null=True)),
                ('time_observations_started', models.TimeField(null=True)),
                ('duration_minutes', models.IntegerField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
            options={
                'ordering': ['country', 'year'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed Country', max_length=120, null=True)),
                ('iso2', models.CharField(blank=True, max_length=2, null=True, verbose_name='2 Digit ISO')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='CountryWithACRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed Country', max_length=120, null=True)),
                ('iso2', models.CharField(blank=True, max_length=2, null=True, verbose_name='2 Digit ISO')),
                ('latitude', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('tot_birds_count', models.IntegerField(default=1, null=True)),
                ('tot_observations_events', models.IntegerField(null=True)),
                ('is_exotic', models.BooleanField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
