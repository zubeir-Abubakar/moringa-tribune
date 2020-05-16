from django.test import TestCase
from .models import Editor,Article,tags
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.zubeyr= Editor(first_name = 'Zubeyr', last_name ='Abubakar', email ='zubkayare@gmail.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.zubeyr,Editor))