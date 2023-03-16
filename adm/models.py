from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=11, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    endereço = models.CharField(max_length=100)
    número = models.CharField(max_length=10)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
class Carro(models.Model):
    PLACA = {
        ('mercosul', 'Mercosul'),
        ('modelo antigo', 'Modelo antigo'),
    }
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, related_name = 'carros')
    carro = models.CharField(max_length=50)
    ano = models.CharField(max_length=4)
    placa_tipo = models.CharField(max_length=13, choices=PLACA)
    placa = models.CharField(max_length=8, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.carro
    
class Peça(models.Model):
    nome_peça = models.CharField(max_length=255)
    produto = models.CharField(max_length=255)
    preço = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    código = models.IntegerField(unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.nome_peça
    
class Serviço(models.Model):
    STATUS = (
        ('fazendo', 'Fazendo'),
        ('feito', 'Feito'),
    )
    
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name='servicos', null=True)
    pecas = models.ManyToManyField(Peça, related_name='servicos' )
    serviço = models.CharField(max_length=255)
    descrição = models.TextField()
    status = models.CharField(max_length=7, choices=STATUS)
    valor_serviço = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.serviço
    

    
    