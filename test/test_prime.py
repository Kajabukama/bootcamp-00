# a unit test file to test for a function
# that generate prime numbers from 0 to n

import unittest
from app.prime_numbers import generate_prime

class TestCalculator(unittest.TestCase):

	# a method to test generate_prime(10) = (3,5,7,9)
	def test_general_prime(self):
		self.assertEqual(generate_prime(10), [3,5,7,9])

	# a method to test generate_prime(-1)  does not accept negative numbers
	def test_negative_input(self):
		self.assertEqual(generate_prime(-1), 'Invalid argument,no negative input allowed')

	#a method to test generate_prime('string') does not accept string input
	def test_string_input(self):
		self.assertEqual(generate_prime('test'),'Invalid argument,no string input allowed')

	#a method to test generate_prime(0.1) does not accept float input
	def test_flot_input(self):
		self.assertEqual(generate_prime(0.0), 'Invalid argument,no float input allowed')

	#a method to test generate_prime(0.1) does not accept float input
	def test_flot_input(self):
		self.assertEqual(generate_prime(0), 'Invalid argument,input must be greater than zero')
		
	

if __name__ == '__main__':
    unittest.main()
