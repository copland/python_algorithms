__author__ = 'Chris Opland'

from sorter import Sorter
import unittest

class SorterTests(unittest.TestCase):

	def setUp(self):
		self._unsorted = [7,2,1,8,11,5,3,4]
		self._sorted   = [1,2,3,4,5,7,8,11]
		self.sorter = Sorter()

	def test_bubbleSort(self):
		self.assertEqual(self._sorted, self.sorter.bubble_sort(self._unsorted))

	def test_selectionSort(self):
		self.assertEqual(self._sorted, self.sorter.selection_sort(self._unsorted))

	def test_insertionSort(self):
		self.assertEqual(self._sorted, self.sorter.insertion_sort(self._unsorted))
	
	def test_shellSort(self):
		self.assertEqual(self._sorted, self.sorter.shell_sort(self._unsorted))
		

if __name__ == '__main__':
	unittest.main()
