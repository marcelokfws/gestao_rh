from django.urls import path
from .views import EmpresaCreate, EmpresaEdit, EmpresaList

urlpatterns = [
    path('list', EmpresaList.as_view(), name='list_empresas'),
    path('novo', EmpresaCreate.as_view(), name='create_empresa'),
    path('editar/<int:pk>/',
         EmpresaEdit.as_view(), name='edit_empresa'),

]