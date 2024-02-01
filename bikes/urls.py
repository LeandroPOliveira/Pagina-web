from django.urls import path
# from bikes.views import index, nova_bike, editar_bike, filtro, detalhes_bike
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('editar-bike', views.editar_bike, name='editar_bike'),
    path('detalhes-bike/<int:bike_id>', views.detalhes_bike, name='detalhes_bike'),
    path('filtro/<str:categoria>', views.filtro, name='filtro')
]

