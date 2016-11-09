import unittest 
import sys
sys.path.insert(0,'/home/jonathan/Python/weather')
#reference to the above: http://askubuntu.com/questions/470982/how-to-add-a-python-module-to-syspath/471168
from main import *

#test cases are ran when methods start with letters test
class Test_Basics(unittest.TestCase):
	def test_sample(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_locations_equal(self):
		self.assertEqual(locations, ['Sunnyvale, US', 'San Jose, US', 'Palo Alto, US', 'San Francisco, US', 'Oakland, US', 'Berkeley, US'])

if __name__ == '__main__':
	unittest.main()
	#print(locations)
