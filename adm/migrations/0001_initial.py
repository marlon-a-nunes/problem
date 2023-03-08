# Generated by Django 4.1.6 on 2023-02-09 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=11, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('endereço', models.CharField(max_length=100)),
                ('número', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carro', models.CharField(max_length=50)),
                ('ano', models.CharField(max_length=4)),
                ('placa_tipo', models.CharField(choices=[('mercosul', 'Mercosul'), ('modelo antigo', 'Modelo antigo')], max_length=13)),
                ('placa', models.CharField(max_length=7, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carros', to='adm.cliente')),
            ],
        ),
    ]