from django.urls import path
from . import views

urlpatterns = [
    path('', views.MexicoGDPPage.as_view(),name='mexico'),
]
