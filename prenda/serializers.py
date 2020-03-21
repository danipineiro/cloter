from .models import Prenda, Match
from rest_framework import serializers


class PrendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prenda
        fields = ('marca', 'modelo', 'tipo')


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('prenda_1', 'prenda_2', 'positivos', 'negativos', 'neutrales')


    def create(self, validated_data):
        prenda_1 = validated_data.get('prenda_1')
        prenda_2 = validated_data.get('prenda_2')

        try:
            match = Match.objects.filter(prenda_1__in=(prenda_1, prenda_2), prenda_2__in=(prenda_1, prenda_2))
            print('ya existe')
        except:
            pass
        return super().create(validated_data)

        # try:
        #     obj = Match.objects.get(prenda_1=validated_data.get('prenda_1', None),
        #                             prenda_2=validated_data.get('prenda_2', None))
        # except:
        #     pass
        # return instance

