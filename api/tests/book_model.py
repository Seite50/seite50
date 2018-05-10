from django.test import TestCase

from api.models.book import Book


# Create your tests here.
class ModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.bookid = "1234"
        cls.title = "TestBuch"
        cls.description = "Ein Buch über das Testen"
        cls.published_date = "2018-05-07"
        cls.seite50_sentence = "Uch wie ist das schön"

        cls.book = Book(
            bookid=cls.bookid,
            title=cls.title,
            description=cls.description,
            published_date=cls.published_date,
            seite50_sentence=cls.seite50_sentence)

    def test_model_can_create_a_book(self):
        old_count = Book.objects.count()
        self.book.save()
        new_count = Book.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_model_can_create_a_correct_book(self):
        self.book.save()
        db_book = Book.objects.get()
        self.assertEqual(db_book, self.book)
