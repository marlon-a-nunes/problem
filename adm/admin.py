from django.contrib import admin

from adm.models import Cliente, Carro, Serviço, Peça
    
class CarroInline(admin.TabularInline):
    model = Carro
    
class ServiçoInline(admin.TabularInline):
    model = Serviço
    
class PeçaInline(admin.TabularInline):
    model = Peça
    
class ClienteAdmin(admin.ModelAdmin):
    inlines = [
        CarroInline,
        ]

    
class CarroAdmin(admin.ModelAdmin):
    inlines = [
        ServiçoInline,
    ]
    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Carro, CarroAdmin)
admin.site.register(Serviço)
admin.site.register(Peça)