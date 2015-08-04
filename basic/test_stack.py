__author__ = 'copland'

from algorithms.basic.stack import Stack
import unittest

class StackTests(unittest.TestCase):

	def setUp(self):
		self.testStack = Stack()

	def test_push(self):
		self.testStack.push(4)
		self.assertEqual([4], self.testStack.show())

	def test_pop_singleItemStack(self):
		self.testStack.push(4)
		self.assertEqual(4, self.testStack.pop())

	def test_pop_multiItemStack(self):
		self.testStack.push('1')
		self.testStack.push('2')
		self.assertEqual('2', self.testStack.pop())

	def test_pop_emptyStack(self):
		with self.assertRaises(Exception):
			self.testStack.pop()

	def test_size(self):
		self.testStack.push(4)
		self.assertEqual(1, self.testStack.size())

	def test_isEmpty(self):
		self.assertTrue(self.testStack.isEmpty())
		self.testStack.push('item')
		self.assertFalse(self.testStack.isEmpty())



if __name__ == '__main__':
	unittest.main()
