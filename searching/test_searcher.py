__author__ = 'copland'

from searcher import Searcher
import unittest


class SearcherTests(unittest.TestCase):

	def setUp(self):
		self.alist = [2,3,4,5,6,11,25]
		self.searcher = Searcher()

	def test_binarySearch(self):
		self.assertEqual(True, self.searcher.binary_search(self.alist, 2))
		self.assertEqual(True, self.searcher.binary_search(self.alist, 25))
		self.assertEqual(True, self.searcher.binary_search(self.alist, 5))
		self.assertEqual(False, self.searcher.binary_search(self.alist, 7))
		self.assertEqual(False, self.searcher.binary_search(self.alist, 26))
	
if __name__ == '__main__':
	unittest.main()	
