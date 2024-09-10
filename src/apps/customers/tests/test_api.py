from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.client.login(username='admin', password='admin')
        self.url = reverse('customers-list')
        
    # def test_authenticate_user(self):
    #     user = authenticate(username='admin', password='admin')
    #     self.assertTrue((user is not None) and user.is_authenticated)
    #     user = authenticate(username='test', password='wrong')
    #     self.assertFalse((user is not None) and user.is_authenticated)

    # def test_request_list_authorized(self):
    #     url = reverse('customers-list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #     self.client.force_authenticate(user=self.user)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_customer(self):
    #     self.client.force_authenticate(user=self.user)
    #     data = {
    #         'document': '110.025.546-08',
    #         'firstName': 'João',
    #         'lastName': 'Silva',
    #         'gender': 'M',
    #         'email': 'joao.silva@example.com',
    #         'emailSecondary': 'joao.secondary@example.com',
    #         'phoneNumber': '+55 35 99153-5567',
    #         'birthDate': '1990-01-01',
    #         'avatar': ''
    #     }
    #     response = self.client.post(self.url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)        

    # def test_update_customer(self):
    #     self.client.force_authenticate(user=self.user)
    #     # Primeiro, crie um cliente para atualizar
    #     create_response = self.client.post(self.url, {
    #         'document': '110.025.546-08',
    #         'firstName': 'AAsdawsdaw',
    #         'lastName': 'Silva',
    #         'gender': 'M',
    #         'email': 'joao.silva@example.com',
    #         'emailSecondary': 'joao.secondary@example.com',
    #         'phoneNumber': '+55 35 99153-5567',
    #         'birthDate': '1990-01-01',
    #         'avatar': ''
    #     }, format='json')
    #     self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
    #     print(create_response.data)
    #     customer_id = create_response.data['id']
    #     update_url = reverse('customer-detail', args=[customer_id])
    #     update_data = {
    #         'firstName': 'João Atualizado',
    #         'lastName': 'Silva Atualizado'
    #     }
    #     response = self.client.put(update_url, update_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_delete_customer(self):
    #     self.client.force_authenticate(user=self.user)
    #     # Primeiro, crie um cliente para deletar
    #     create_response = self.client.post(self.url, {
    #         'document': '110.025.546-08',
    #         'firstName': 'João',
    #         'lastName': 'Silva',
    #         'gender': 'M',
    #         'email': 'joao.silva@example.com',
    #         'emailSecondary': 'joao.secondary@example.com',
    #         'phoneNumber': '+55 35 99153-5567',
    #         'birthDate': '1990-01-01',
    #         'avatar': ''
    #     }, format='json')
    #     self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
    #     customer_id = create_response.data['id']
    #     delete_url = reverse('customer-detail', args=[customer_id])
    #     response = self.client.delete(delete_url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)