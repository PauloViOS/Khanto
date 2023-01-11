from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Imovel


class ImovelAdmin(ModelAdmin):
	list_display = ("id","codigo", "max_hospedes", "num_banheiros", "pet_friendly", "valor_limpeza", "data_ativacao",
					"dt_criacao", "dt_atualizacao")


admin.site.register(Imovel, ImovelAdmin)
