from rest_framework import viewsets

from .models import Anuncio
from .serializers import AnunciosSerializer


class AnunciosViewset(viewsets.ModelViewSet):
	queryset = Anuncio.objects.all()
	serializer_class = AnunciosSerializer
