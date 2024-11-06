from django.views.generic.base import TemplateView


class HomeTemplateView(TemplateView):
    """Loads home html where the frontend is set
    """
    template_name = 'mapping/home.html'


class AboutTheSpeciesTemplateView(TemplateView):
    """Loads home html where the frontend is set
    """
    template_name = 'the_species.html'


class AboutTheSpatialAnalysisTemplateView(TemplateView):
    """Loads home html where the frontend is set
    """
    template_name = 'spatial_analysis.html'
