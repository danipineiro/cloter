from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Prenda, Match
from rest_framework import viewsets, mixins, status
from .serializers import PrendaSerializer, MatchSerializer


class PrendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows prendas to be viewed or edited.
    """
    queryset = Prenda.objects.all().order_by('-id')
    serializer_class = PrendaSerializer

    @action(detail=False, methods=['get'])
    def pareja_random(self, request):
        """
        Devuelve dos prendas de distinto tipo entre sí elegidas aleatoriamente
        """

        try:
            prenda_1 = Prenda.objects.order_by('?')[0]
            prenda_2 = Prenda.objects.exclude(tipo=prenda_1.tipo).order_by('?')[0]
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        prendas = [
            prenda_1,
            prenda_2
        ]

        serializer = self.get_serializer(prendas, many=True)
        return Response(serializer.data)


class MatchViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Match.objects.all().order_by('-id')
    serializer_class = MatchSerializer
