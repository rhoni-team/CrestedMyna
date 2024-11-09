# CrestedMyna

A web application to visualize the global expansion of the Crested Myna _(Acridotheres cristatellus)_. You can view the live application at https://crestedmyna.rhonidev.com/.

Observations for the species were analyzed across the different countries where it was recorded and over time.

This species prefers open areas such as agricultural lands, parks and urban spaces. A spatial analysis was conducted to determine whether, outside its native range, this species occupies rural areas or remains within urban zones like other exotic species such as the house sparrow _(Passer domesticus)_.

# Technologies

## R

The ebird data used in this application was first read by using [R](https://www.r-project.org/). The code used for this process is available in our repository [Crested Myna Data Analysis](https://github.com/rhoni-team/Crested_Myna_Data_Analysis).

## PostGIS and PostgreSQL

Data analysis, data processing and spatial analysis were performed mostly through SQL by using [PostGIS](https://postgis.net/) and [PostgreSQL](https://www.postgresql.org/). The code can be found in the [data_loading/migrations folder](./crested_myna/data_loading/migrations) of this repository.

## Django and Python

This web application was developed on [Django](https://www.djangoproject.com/).

## Leaflet

Spatial data visualizations were made by using [Leaflet](https://leafletjs.com/).

## eCharts

Data visualizations were made by using [EChartsJS](https://echartsjs.com/index.html).
