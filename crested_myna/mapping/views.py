"""Main View to load Vue app in Django html template"""
from django.views.generic.base import TemplateView
from data_analysis.models import ACRecord


class IndexTemplateView(TemplateView):
    """Loads index.html where the frontend is set
    """

    template_name = 'mapping/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = ACRecord.objects.all()[:5]
        return context
