# Generated by Django 5.1.1 on 2024-11-07 18:22
""" SQL PostGis command to make the polygons valid """

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_loading', '0003_add_world_cities_shp_data'),
    ]

    operations = [
        migrations.RunSQL(
            """
            -- Create a view with the valid geometries for the countries
            CREATE OR REPLACE VIEW valid_geom_view AS
            SELECT 
                id, 
                name,
                iso2,
                ST_MakeValid(geom) as valid_geom
            FROM data_loading_country;

            -- Update the Country table with the simplified geometries
            UPDATE data_loading_country
            SET geom = valid_geom
            FROM valid_geom_view
            WHERE data_loading_country.id = valid_geom_view.id;

            -- Drop the view
            DROP VIEW valid_geom_view;
            """
        )
    ]
