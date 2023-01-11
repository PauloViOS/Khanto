from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Reserva


class ReservaAdmin(ModelAdmin):
	list_display = ('codigo', 'anuncio', 'data_checkin', 'data_checkout', 'preco', 'comentario', 'num_hospedes',
					'dt_criacao', 'dt_atualizacao')


admin.site.register(Reserva, ReservaAdmin)