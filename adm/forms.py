from adm.models import Cliente, Carro, Serviço, Peça
from django import forms

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields=('nome', 'sobrenome', 'telefone','cpf', 'endereço', 'número', 'cidade', 'estado')
        
class CarroForm(forms.ModelForm):
     class Meta:
        model = Carro
        fields = ('carro', 'ano', 'placa_tipo', 'placa')

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Serviço
        fields=('serviço', 'descrição', 'status', 'valor_serviço', 'pecas')
        
class PecaForm(forms.ModelForm):
    class Meta:
        model = Peça
        fields = ('nome_peça', 'produto', 'preço', 'código')
        
    