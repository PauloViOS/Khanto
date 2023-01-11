from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Anuncio


class AnuncioAdmin(ModelAdmin):
	list_display = ('id', 'imovel', 'plataforma', 'taxa_plataforma', 'dt_criacao', 'dt_atualizacao')
	exclude = ('taxa_plataforma',)


admin.site.register(Anuncio, AnuncioAdmin)
