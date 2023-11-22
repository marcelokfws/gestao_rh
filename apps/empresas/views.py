from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return redirect('list_empresas')


class EmpresaList(ListView):
    model = Empresa

    def get_queryset(self):
        return Empresa.objects.all()


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']


