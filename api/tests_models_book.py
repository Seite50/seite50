from django.test import TestCase

from .models_book import Book

# Create your tests here.
class ModelTestCase(TestCase):

    def setUp(self):
        self.bookid = "1234"
        self.title = "TestBuch"
        self.description = "Ein Buch über das Testen"
        self.published_date = "2018-05-07"
        self.seite50_sentence = "Uch wie ist das schön"

        self.book = Book(bookid=self.bookid,
                         title=self.title,
                         description = self.description,
                         published_date = self.published_date,
                         seite50_sentence = self.seite50_sentence)

    def test_model_can_create_a_book(self):
        old_count = Book.objects.count()
        self.book.save()
        new_count = Book.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_model_can_create_a_correct_book(self):
        db_book = Book.objects.get()
        self.assertEqual(db_book,self.book)
