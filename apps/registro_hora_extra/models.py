from django.db import models
from apps.funcionarios.models import Funcionario

class RegistroHoraExtra(models.Model):

    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Horas Extras'
        verbose_name_plural = 'Horas Extras'

    def __str__(self):
        return self.motivo
