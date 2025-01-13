from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class FaceRecognitionViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('facerecognition')

    def test_face_recognition(self):
        with open('path/to/test/image.jpg', 'rb') as image:
            response = self.client.post(self.url, {'image': image}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('faces', response.data)
