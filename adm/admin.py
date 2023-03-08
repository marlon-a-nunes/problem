from django.contrib import admin

from adm.models import Cliente, Carro, Serviço
    
class CarroInline(admin.TabularInline):
    model = Carro
    
class ClienteAdmin(admin.ModelAdmin):
    inlines = [
        CarroInline,
        ]
    
class ServiçoInline(admin.TabularInline):
    model = Serviço
    
class CarroAdmin(admin.ModelAdmin):
    inlines = [
        ServiçoInline,
    ]
    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Carro, CarroAdmin)
admin.site.register(Serviço)