from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from prenda.models import Prenda, CAMISA


class PrendaTest(APITestCase):

    def test_create_prenda_OK(self):

        url = reverse('prenda-list')

        data = {
            'marca': 'marca de ropa',
            'modelo': 'modelo de ropa',
            'tipo': CAMISA,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Prenda.objects.count(), 1)
        self.assertEqual(Prenda.objects.get().marca, 'marca de ropa')
        self.assertEqual(Prenda.objects.get().modelo, 'modelo de ropa')
        self.assertEqual(Prenda.objects.get().tipo, CAMISA)

    def test_create_prenda_FAIL(self):
        url = reverse('prenda-list')

        data = {
            'marca': 'marca de ropa',
            'modelo': 'modelo de ropa',
            'tipo': 'tipo_fail',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Prenda.objects.count(), 0)

    def test_list_prendas(self):

        url = reverse('prenda-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

        Prenda.objects.create()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

        Prenda.objects.create()
        Prenda.objects.create()
        Prenda.objects.create()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 4)
        self.assertEqual(len(response.data['results']), 4)
