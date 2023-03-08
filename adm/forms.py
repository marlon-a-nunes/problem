from django.forms import modelform_factory, modelformset_factory
from adm.models import Cliente, Carro, Serviço

ClienteFormset = modelform_factory(Cliente, fields=('nome', 'sobrenome', 'telefone',
    'cpf', 'endereço', 'número', 'cidade', 'estado',))
        
CarroFormset = modelform_factory(Carro, fields=('carro', 'ano', 'placa_tipo', 'placa'))

ServicoFormSet = modelformset_factory(Serviço, fields=('serviço', 'descrição', 'status', 'valor_serviço'), extra=1)