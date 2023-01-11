from rest_framework import viewsets

from .models import Imovel
from .serializers import ImoveisSerializer


class ImoveisViewset(viewsets.ModelViewSet):
	queryset = Imovel.objects.all()
	serializer_class = ImoveisSerializer
