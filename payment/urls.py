from django.urls import path
from . import views

urlpatterns = [
    path('pagamento-sucesso', views.pagamento_sucesso, name='pagamento_sucesso'),
]
