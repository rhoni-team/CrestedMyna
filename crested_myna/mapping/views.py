"""Main View to load Vue app in Django html template"""
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.views.generic.base import TemplateView
from data_loading.models import ACRecord


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
            print(response)
            return response
        
        else:
            return HttpResponseBadRequest('Invalid request')
