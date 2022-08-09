from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class MexicoGDPPage(TemplateView):
    template_name = 'mexico_gdp_per_capita.html'
