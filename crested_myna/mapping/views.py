"""Main View to load Vue app in Django html template"""
from typing import List

from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.views.generic.base import TemplateView
from django.core.serializers import serialize

from data_loading.models import ACRecord
from data_loading.models import Country

import json

class IndexTemplateView(TemplateView):
    """Loads index.html where the frontend is set
    """

    template_name = 'mapping/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = ACRecord.objects.all()[:5]
        return context


class GetRecords(View):
    """Get records from the database"""

    def get(self, request):

        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        if is_ajax:
            records = ACRecord.objects.values_list('location', flat=True)
            response = JsonResponse({ "records": list(records)})
            return response
        
        else:
            return HttpResponseBadRequest('Invalid request')


class GetCountriesPolygons(View):
    """Get countries polygons from the database"""

    def get_country_code_for_countries_with_ac_records(self) -> List["str"]:
        """Get a list of country codes for countries with AC records"""
        all_records = ACRecord.objects.all().order_by('country_code')
        country_codes = all_records.distinct('country_code').values_list('country_code', flat=True)
        return country_codes
    
    def get_countries_polygons_with_ac_records(self, country_codes: List["str"]) -> List["Country"]:
        """Get a list of countries polygons for countries with AC records"""
        countries_pol = Country.objects.filter(iso2__in=country_codes)
        return countries_pol
    
    def serialize_countries_polygons_as_geojson(self, countries_polygons: List["Country"]) -> str:
        """Serialize countries polygons as geojson"""
        geojson = serialize('geojson', countries_polygons)
        
        geojson_without_crs = json.loads(geojson)
        geojson_without_crs.pop('crs', None)
        geojson_without_crs = json.dumps(geojson_without_crs)

        return geojson_without_crs

    def get(self, request):
        """Get the countries polygons with AC records as geojson""" 
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        if is_ajax:
            countries = self.get_country_code_for_countries_with_ac_records()
            countries_polygons = self.get_countries_polygons_with_ac_records(countries)
            geojson_pol = self.serialize_countries_polygons_as_geojson(countries_polygons)
            response = JsonResponse({ "countries": geojson_pol})
            return response
        else:
            return HttpResponseBadRequest('Invalid request')
    