"""Main View to load Vue app in Django html template"""
from django.views.generic.base import TemplateView


class IndexTemplateView(TemplateView):
    """Loads index.html where the frontend is set
    """

    def get_template_names(self):
        template_name = 'mapping/home.html'
        return template_name
