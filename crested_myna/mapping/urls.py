from django.urls import path, include
from mapping.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
]
