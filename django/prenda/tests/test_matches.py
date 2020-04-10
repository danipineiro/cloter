from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from prenda.models import Prenda, Match, CAMISA, CAMISETA


class MatchTest(APITestCase):

    def test_match_OK(self):
        p1 = Prenda.objects.create(tipo=CAMISA)
        p2 = Prenda.objects.create(tipo=CAMISETA)

        url = reverse('match-list')

        data = {
            'prenda_1': p1.id,
            'prenda_2': p2.id,
            'accion': 1,
        }

        self.assertEqual(Match.objects.count(), 0)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('positivos'), 1)
        self.assertEqual(Match.objects.count(), 1)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('positivos'), 2)
        self.assertEqual(Match.objects.count(), 1)

    def test_match_mismo_tipo_FAIL(self):
        p1 = Prenda.objects.create(tipo=CAMISA)
        p2 = Prenda.objects.create(tipo=CAMISA)

        url = reverse('match-list')

        data = {
            'prenda_1': p1.id,
            'prenda_2': p2.id,
            'accion': 1,
        }

        self.assertEqual(Match.objects.count(), 0)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Match.objects.count(), 0)

    def test_match_misma_prenda_FAIL(self):
        p1 = Prenda.objects.create(tipo=CAMISA)

        url = reverse('match-list')

        data = {
            'prenda_1': p1.id,
            'prenda_2': p1.id,
            'accion': 1,
        }

        self.assertEqual(Match.objects.count(), 0)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Match.objects.count(), 0)

    def test_match_accion_incorrecta_FAIL(self):
        p1 = Prenda.objects.create(tipo=CAMISA)
        p2 = Prenda.objects.create(tipo=CAMISETA)

        url = reverse('match-list')

        data = {
            'prenda_1': p1.id,
            'prenda_2': p2.id,
            'accion': 2,
        }

        self.assertEqual(Match.objects.count(), 0)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Match.objects.count(), 0)

    def test_total_matches(self):
        p1 = Prenda.objects.create(tipo=CAMISA)
        p2 = Prenda.objects.create(tipo=CAMISETA)

        url = reverse('match-list')

        data = {
            'prenda_1': p1.id,
            'prenda_2': p2.id,
            'accion': 1,
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('positivos'), 1)
        self.assertEqual(response.data.get('negativos'), 0)
        self.assertEqual(response.data.get('neutrales'), 0)
        self.assertEqual(response.data.get('total_matches'), 1)

        data = {
            'prenda_1': p1.id,
            'prenda_2': p2.id,
            'accion': -1,
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('positivos'), 1)
        self.assertEqual(response.data.get('negativos'), 1)
        self.assertEqual(response.data.get('neutrales'), 0)
        self.assertEqual(response.data.get('total_matches'), 2)

        data = {
            'prenda_1': p1.id,
            'prenda_2': p2.id,
            'accion': 0,
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('positivos'), 1)
        self.assertEqual(response.data.get('negativos'), 1)
        self.assertEqual(response.data.get('neutrales'), 1)
        self.assertEqual(response.data.get('total_matches'), 3)

