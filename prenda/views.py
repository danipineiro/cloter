from .models import Prenda
from rest_framework import viewsets
from.serializers import PrendaSerializer


class PrendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows prendas to be viewed or edited.
    """
    queryset = Prenda.objects.all().order_by('-id')
    serializer_class = PrendaSerializer
