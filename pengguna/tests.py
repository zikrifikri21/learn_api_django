from django.test import TestCase
from .models import Book
from django.urls import reverse
import json

class BookModelTests(TestCase):
    def test_create_book(self):
        book = Book.objects.create(title="Test Book", author="Author", published_date="2023-01-01")
        self.assertEqual(book.title, "Test Book")

class BookViewTests(TestCase):
    def test_get_books(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        data = {'title': 'New Book', 'author': 'Author', 'published_date': '2023-01-01'}
        response = self.client.post(reverse('book_list'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
