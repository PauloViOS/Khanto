from django.core.validators import MinValueValidator
from django.db import models


class Imovel(models.Model):
	max_hospedes = models.IntegerField(validators=[MinValueValidator(0)])
	num_banheiros = models.IntegerField(validators=[MinValueValidator(0)])
	pet_friendly = models.BooleanField(default=False)
	valor_limpeza = models.DecimalField(decimal_places=2, max_digits=7)
	data_ativacao = models.DateField()
	dt_criacao = models.DateTimeField(auto_now_add=True)
	dt_atualizacao = models.DateTimeField(auto_now=True)

	class Meta:
		constraints = [
			models.CheckConstraint(
				name="data_ativacao_depois_de_dt_criacao",
				check=models.Q(data_ativacao__gte=models.F("dt_criacao"))
			)
		]
		verbose_name_plural = 'imoveis'

	@property
	def codigo(self):
		return f"IMV{self.id}"
