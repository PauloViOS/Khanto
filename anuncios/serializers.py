from rest_framework import serializers

from .models import Anuncio


class AnunciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Anuncio
		fields = ['id', 'imovel', 'plataforma', 'taxa_plataforma', 'dt_criacao', 'dt_atualizacao', ]
		read_only_fields = ('taxa_plataforma',)
