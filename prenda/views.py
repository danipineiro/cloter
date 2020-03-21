from .models import Prenda, Match
from rest_framework import viewsets
from.serializers import PrendaSerializer, MatchSerializer


class PrendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows prendas to be viewed or edited.
    """
    queryset = Prenda.objects.all().order_by('-id')
    serializer_class = PrendaSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all().order_by('-id')
    serializer_class = MatchSerializer