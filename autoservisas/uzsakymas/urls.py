from django.urls import path

from uzsakymas.views import Puiku

urlpatterns=[
    path("", Puiku)
]
from django.urls import path

from uzsakymas.views import Puiku

urlpatterns = [
    path('', Puiku )
]