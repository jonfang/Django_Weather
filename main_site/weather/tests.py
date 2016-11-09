from django.test import TestCase

# Create your tests here.
class Test_Basics(TestCase):
	def test_sample(self):	
		self.assertEqual('foo'.upper(), 'FOO')

