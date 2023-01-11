from rest_framework import serializers

from .models import Imovel


class ImoveisSerializer(serializers.ModelSerializer):
	class Meta:
		model = Imovel
		fields = ["id", "codigo", "max_hospedes", "num_banheiros", "pet_friendly", "valor_limpeza", "data_ativacao",
					"dt_criacao", "dt_atualizacao"]
