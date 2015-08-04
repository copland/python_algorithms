class Stack:

	def __init__(self):
		self.stackList = []
		self.top = -1

	def push(self, item):
		self.top = self.top + 1
		self.stackList.append(item)

	def pop(self):
		if not self.isEmpty():
			poppedItem = self.stackList.pop(self.top)
			self.top = self.top - 1
			return poppedItem
		else:
			raise Exception('The stack is empty so nothing can be popped')

	def peek(self):
		if not self.isEmpty():
			return self.stackList[self.top]
		else:
			return []

	def isEmpty(self):
		isEmpty = True
		if self.top > -1:
			isEmpty = False
		return isEmpty

	def size(self):
		return self.top + 1

	def show(self):
		return self.stackList