from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models.book import Book
import json

book_pk = 3

class BookTest(APITestCase):
    fixtures = ['books.json']
    """
    Test-Cases zum erstellen von Büchern
    """

    def test_api_can_create_a_book(self):
        """
        Es wird sichergestellt, dass ein Buch erstellt werden kann
        """
        book = {
            'bookid': '23',
            'title': 'Neues Buch',
            'description': 'Unsinn',
            'seite50_sentence': 'Ein neuer Satz ohne Verb.',
            'published_date': '1980-01-01',
        }
        res = self.client.post(
            reverse('create_book'), book, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_book(self):
        """
        Es wird sichergestellt, dass ein Buch gelesen werden kann
        """
        response = self.client.get(
            reverse('details_book', kwargs={'pk': book_pk}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_book(self):
        """
        Es wird sichergestellt, dass ein Buch geändert werden kann
        """
        book = json.loads(self.client.get(
            reverse('details_book', kwargs={'pk': book_pk}), format='json').content)
        book['title'] = "new title"
        response = self.client.put(
            reverse('details_book', kwargs={'pk': book_pk}), book,
            format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_book(self):
        """
        Es wird sichergestellt, dass ein Buch gelöscht werden kann
        """
        response = self.client.delete(
            reverse('details_book', kwargs={'pk': book_pk}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
