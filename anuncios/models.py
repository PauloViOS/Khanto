from django.db import models
from imoveis.models import Imovel


class Anuncio(models.Model):
	class Plataforma(models.TextChoices):
		AIRBNB = 'AIRBNB', 'AirBnb'
		BOOKING = 'BOOKING', 'Booking'
		TRIVAGO = 'TRIVAGO', 'Trivago'
		HOTEL_URBANO = 'HOTEL_URBANO', 'Hotel Urbano'
	imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
	plataforma = models.CharField(max_length=30, choices=Plataforma.choices)
	taxa_plataforma = models.FloatField()
	dt_criacao = models.DateTimeField(auto_now_add=True)
	dt_atualizacao = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		taxas_dict = {
			'AIRBNB': 50,
			'BOOKING': 50,
			'TRIVAGO': 50,
			'HOTEL_URBANO': 50,
		}
		self.taxa_plataforma = taxas_dict[self.plataforma]
		super().save()
