from .models import Prenda, Match
from rest_framework import serializers

ACCIONES = [
    (1, 'positivo'),
    (0, 'neutral'),
    (-1, 'negativo'),
]


class PrendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prenda
        fields = ('id', 'marca', 'modelo', 'tipo', 'imagen')
        read_only_fields = ('imagen',)


class MatchSerializer(serializers.ModelSerializer):
    accion = serializers.ChoiceField(choices=ACCIONES, write_only=True)

    class Meta:
        model = Match
        fields = ('prenda_1', 'prenda_2', 'positivos', 'negativos', 'neutrales', 'accion', 'total_matches')
        read_only_fields = ('positivos', 'negativos', 'neutrales', 'total_matches')

    def validate(self, data):
        if data['prenda_1'].tipo == data['prenda_2'].tipo:
            raise serializers.ValidationError("Las prendas no pueden ser del mismo tipo")
        return data

    def create(self, validated_data):
        prenda_1 = validated_data.get('prenda_1')
        prenda_2 = validated_data.get('prenda_2')

        try:
            match = Match.objects.get(prenda_1__in=(prenda_1, prenda_2), prenda_2__in=(prenda_1, prenda_2))
        except Match.DoesNotExist:
            match = Match(prenda_1=prenda_1, prenda_2=prenda_2)

        if validated_data['accion'] == 1:
            match.positivos += 1
        elif validated_data['accion'] == -1:
            match.negativos += 1
        elif validated_data['accion'] == 0:
            match.neutrales += 1

        match.save()
        return match


class MatchDetailSerializer(serializers.ModelSerializer):

    prenda_1 = PrendaSerializer(read_only=True)
    prenda_2 = PrendaSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ('prenda_1', 'prenda_2', 'positivos', 'negativos', 'neutrales', 'total_matches')
        read_only_fields = ('prenda_1', 'prenda_2', 'positivos', 'negativos', 'neutrales', 'total_matches')
