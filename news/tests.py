from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
 def setUp(self):
        self.james= Editor(first_name = 'Zubeyr', last_name ='Abubakar', email ='zubkayare@gmail.com')
        def test_instance(self):
        self.assertTrue(isinstance(self.zubeyr,Editor))