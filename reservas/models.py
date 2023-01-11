import uuid

from django.core.validators import MinValueValidator
from django.db import models

from anuncios.models import Anuncio
from imoveis.models import Imovel


class Reserva(models.Model):
	codigo = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
	anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
	data_checkin = models.DateField()
	data_checkout = models.DateField()
	preco = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0)])
	comentario = models.TextField(max_length=500)
	num_hospedes = models.IntegerField(validators=[MinValueValidator(0)])
	dt_criacao = models.DateTimeField(auto_now_add=True)
	dt_atualizacao = models.DateTimeField(auto_now=True)


	@property
	def preco_total(self):
		anuncio = Anuncio.objects.get(id=self.anuncio)
		return self.preco + anuncio.taxa_plataforma
