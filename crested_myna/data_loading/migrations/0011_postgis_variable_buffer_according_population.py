# Generated by Django 5.1.1 on 2024-11-08 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_loading', '0010_sql_cities_with_ac_records'),
    ]

    operations = [
        migrations.RunSQL(
            """
            -- Update the buffer_radio field with the variable buffer according to the population
            UPDATE data_loading_citiesacexotic
                SET buffer_radio = ROUND(CAST(2000 + ((population::float / 20000000) * (150000 - 2000)) AS INTEGER), 0);
            
            -- Create the buffer_geom field with the buffer according to the buffer_radio
            UPDATE data_loading_citiesacexotic
                SET buffer_geom = ST_Buffer(geom, buffer_radio);

            -- Create a view with the dissolved buffers
            CREATE OR REPLACE VIEW dissolved_buffers_view AS
            WITH dissolved AS (
                SELECT
                iso2,
                ST_Union(buffer_geom) AS dissolved_geom
            FROM
                data_loading_citiesacexotic
            GROUP BY
                iso2
            )
            SELECT
                iso2,
                (ST_Dump(dissolved_geom)).geom AS dissolved_geom
            FROM
                dissolved;

            -- Transform the buffer_geom to 4326
            INSERT INTO data_loading_buffercitiesexotic4326(iso2, geom)
            SELECT 
                iso2,
                ST_Transform(dissolved_geom, 4326) AS geom
            FROM dissolved_buffers_view;

            -- Drop the view
            DROP VIEW dissolved_buffers_view;
            """
        )
    ]