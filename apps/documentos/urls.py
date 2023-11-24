from django.urls import path
from .views import DocumentoCreate, DocumentoList

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
    path('list/', DocumentoList, name='documento_list'),
]