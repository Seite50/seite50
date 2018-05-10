from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models.book import Book


class BookTestBase(APITestCase):
    """
    Test-Cases zum erstellen von Büchern
    """

    def setUp(self):
        """
        Daten die für jeden Test auf´s neue benötigt werden 
        """
        self.book.save()
        self.bookpk = self.book.id

    @classmethod
    def setUpTestData(cls):
        """
        Daten die für alle Tests benötigt werden
        """
        cls.bookid = "1234"
        cls.title = "TestBuch"
        cls.description = "Ein Buch ueber das Testen"
        cls.published_date = "2018-05-07"
        cls.seite50_sentence = "Uch wie ist das schoen"

        cls.book_data = {
            'bookid': cls.bookid,
            'title': cls.title,
            'description': cls.description,
            'published_date': cls.published_date,
            'seite50_sentence': cls.seite50_sentence,
        }

        cls.book = Book(
            bookid=cls.bookid,
            title=cls.title,
            description=cls.description,
            published_date=cls.published_date,
            seite50_sentence=cls.seite50_sentence)


class CreateBookTest(BookTestBase):
    def test_api_can_create_a_book(self):
        """
        Es wird sichergestellt, dass ein Buch erstellt werden kann
        """
        res = self.client.post(
            reverse('create'), self.book_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)


class GetBookTest(BookTestBase):
    """
    Test Cases zum lesen von Büchern
    """

    def test_api_can_get_a_book(self):
        """
        Es wird sichergestellt, dass ein Buch gelesen werden kann
        """
        response = self.client.get(
            reverse('details', kwargs={'pk': self.book.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateBookTest(BookTestBase):
    """
    Test Cases zum lesen von Büchern
    """

    def test_api_can_update_book(self):
        """
        Es wird sichergestellt, dass ein Buch geändert werden kann
        """
        response = self.client.put(
            reverse('details', kwargs={'pk': self.book.id}), {'title': "new"},
            format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteBookTest(BookTestBase):
    def test_api_can_delete_book(self):
        """
        Es wird sichergestellt, dass ein Buch gelöscht werden kann
        """
        response = self.client.delete(
            reverse('details', kwargs={'pk': self.book.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
