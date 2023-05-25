from django.urls import path

from automobilis.views import labas

urlpatterns = [
    path('', labas)
]