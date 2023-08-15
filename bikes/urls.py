from django.urls import path
from bikes.views import index, nova_bike, editar_bike, filtro

urlpatterns = [
    path('', index, name='index'),
    path('nova-bike', nova_bike, name='nova_bike'),
    path('editar-bike', editar_bike, name='editar_bike'),
    path('filtro/<str:categoria>', filtro, name='filtro')
]