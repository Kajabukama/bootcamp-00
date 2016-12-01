import unittest
from app.logic import magic_sum

class TestCalculator(unittest.TestCase):
	def test_magic_sum(self):
		self.assertEqual(magic_sum(5), 15)

if __name__ == '__main__':
    unittest.main()