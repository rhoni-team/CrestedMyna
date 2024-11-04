# Generated by Django 5.1.1 on 2024-11-04 20:10

""" SQL command to get the latitude and longitude for each record
as a geometry point field.
"""

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_loading', '0004_sql_update_acrecord_observations_count'),
    ]

    operations = [
        migrations.RunSQL(
            """
            UPDATE data_loading_acrecord 
                SET geom = ST_SetSRID(ST_MakePoint(longitude, latitude), 4326);
            """
        )
    ]
