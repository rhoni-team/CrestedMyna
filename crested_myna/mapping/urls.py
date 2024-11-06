""" URLS for the mapping app """
from django.urls import path
from mapping.views.views_load_templates import (HomeTemplateView,
                                                AboutTheSpeciesTemplateView,
                                                AboutTheSpatialAnalysisTemplateView)
from mapping.views.views_get_data import GetRecords, GetCountriesPolygonsWithACRecords

urlpatterns_load_templates = [
    path('', HomeTemplateView.as_view(), name='home'),

    path('about-the-species/', 
         AboutTheSpeciesTemplateView.as_view(),
         name='about-the-species'),

    path('about-the-spatial-analysis/', 
         AboutTheSpatialAnalysisTemplateView.as_view(),
         name='about-the-spatial-analysis'),
]

urlpatterns_get_data = [
    path('get-records/', GetRecords.as_view(), name='get-records'),

    path('get-countries-polygons/',
         GetCountriesPolygonsWithACRecords.as_view(),
         name='get-countries-polygons'),
]

urlpatterns = urlpatterns_load_templates + urlpatterns_get_data
