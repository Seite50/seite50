from django.test import TestCase
from api.models.author import Author

class ModelTestCase(TestCase):

    fixtures = ['authors.json']

    @classmethod
    def setUpTestData(cls):
        cls.author = Author(
            name = "Markus Hartmann"
        )

    def test_model_can_create_a_book(self):
        """
        Es wird getestet ob ein Author angelegt werden kann
        """
        old_count = Author.objects.count()
        self.author.save()
        new_count = Author.objects.count()
        self.assertTrue(old_count<new_count)

    def test_model_can_delete_a_book(self):
        """
        Es wird getestet ob ein Author gelöscht werden kann
        """
        author = Author.objects.get()
        (number_of_deletions, Nil) = author.delete()
        self.assertTrue(number_of_deletions==1)

    def test_model_can_read_a_specific_author(self):
        """
        Es wird getestet ob ein bestimmter Author gefunden werden kann
        """
        author = Author.objects.get(id=3)
        self.assertEqual(author.name, "M. Hartmann")

    def test_model_can_delete_a_specific_author(self):
        """
        Es wird getestet ob ein bestimmter Author gelöscht werden kann
        """
        author = Author.objects.get(name = "M. Hartmann")
        (number_of_deletions, Nil) = author.delete()
        self.assertTrue(number_of_deletions==1)