from django.test import TestCase
from django.urls import reverse
from .models import Shelter

# Create your tests here.

class ShelterListViewTests(TestCase):
    def setUp(self):
        Shelter.objects.create(title="Shelter 1", address="123 Main St")
        Shelter.objects.create(title="Shelter 2", address="456 Elm St")

    def test_shelter_is_list(self):
        url = reverse('shelter-CRUD')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        body= response.json()
        self.assertIsInstance(body, dict) 
        self.assertIsInstance(body["results"], list) 

    def test_shelter_list_content(self):
        url = reverse('shelter-CRUD') 
        response = self.client.get(url)
        body=response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(body["results"]), 2)

    def test_shelter_list_pagination(self):
        for i in range(10):
            Shelter.objects.create(title=f"Shelter {i+3}", address=f"{i+3} Random St")
        url = reverse('shelter-CRUD')
        response = self.client.get(url, {'page_size': 5})
        body=response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(body["results"]), 5)
