from django.urls import path
from . import views

urlpatterns = [
    path('', views.MexicoGDPPage.as_view(),name='mexico'),
    path('index', views.IndexPage.as_view(),name='index'),
]
