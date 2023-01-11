from rest_framework import serializers

from .models import Reserva


class ReservasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reserva
		fields = ['codigo', 'anuncio', 'data_checkin', 'data_checkout', 'preco', 'comentario', 'num_hospedes',
					'dt_criacao', 'dt_atualizacao']
