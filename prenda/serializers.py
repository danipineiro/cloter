from .models import Prenda
from rest_framework import serializers


class PrendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prenda
        fields = ('marca', 'modelo', 'tipo')
