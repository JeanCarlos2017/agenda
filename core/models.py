from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Evento (models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criação: ')
    data_evento = models.DateTimeField(verbose_name='Data do Evento: ')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'coreEvento' #forçar o nome da tabela

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        #para converter a data em português
        tuplaSemana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
        tuplaMes = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                'Novembro', 'Dezembro')
        return self.data_evento.strftime('{}, %d de {} de %Y as %H:%M'.format(tuplaSemana[self.data_evento.weekday()],
                                                                               tuplaMes[self.data_evento.month - 1]))

    def get_data_evento_input(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

