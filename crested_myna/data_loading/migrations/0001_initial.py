# Generated by Django 5.1.1 on 2024-11-08 21:29

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
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=250, null=True)),
                ('population', models.IntegerField(null=True)),
                ('iso2', models.CharField(max_length=10, null=True)),
                ('lat', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('lon', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=3857)),
            ],
        ),
        migrations.CreateModel(
            name='CitiesACExotic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=250, null=True)),
                ('population', models.IntegerField(null=True)),
                ('iso2', models.CharField(max_length=10, null=True)),
                ('lat', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('lon', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('buffer_radio', models.FloatField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=3857)),
                ('buffer_geom', django.contrib.gis.db.models.fields.PolygonField(null=True, srid=3857)),
            ],
        ),
        migrations.CreateModel(
            name='CitiesEsri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso2', models.CharField(max_length=10, null=True)),
                ('city_name', models.CharField(max_length=250, null=True)),
                ('population', models.IntegerField(null=True)),
                ('lat', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('lon', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=3857)),
            ],
        ),
        migrations.CreateModel(
            name='CitiesIMB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genc1', models.CharField(max_length=10, null=True)),
                ('city_name', models.CharField(max_length=250, null=True)),
                ('population', models.IntegerField(null=True)),
                ('lat', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('lon', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('iso2', models.CharField(max_length=2, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=3857)),
            ],
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
            name='CountrySimplified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed Country', max_length=120, null=True)),
                ('iso2', models.CharField(blank=True, max_length=2, null=True, verbose_name='2 Digit ISO')),
                ('simple_geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
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
