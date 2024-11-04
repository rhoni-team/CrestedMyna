from django.urls import path, include
from mapping.views import IndexTemplateView, GetRecords, GetCountriesPolygonsWithACRecords

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('get-records/', GetRecords.as_view(), name='get-records'),
    path('get-countries-polygons/', GetCountriesPolygonsWithACRecords.as_view(), name='get-countries-polygons'),
]
