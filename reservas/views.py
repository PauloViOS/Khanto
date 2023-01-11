from rest_framework import viewsets

from .models import Reserva
from .serializers import ReservasSerializer


class ReservasViewset(viewsets.ModelViewSet):
	queryset = Reserva.objects.all()
	serializer_class = ReservasSerializer