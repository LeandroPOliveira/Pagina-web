from django.urls import path
from bikes.views import index

urlpatterns = [
    path('', index, name='index'),
]