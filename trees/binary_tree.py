class BinaryTree:

	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			newLeft = BinaryTree(newNode)
			newLeft.leftChild = self.leftChild
			self.leftChild = newLeft

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			newRight = BinaryTree(newNode)
			newRight.rightChild = self.rightChild
			self.rightChild = newRight

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def getRootVal(self):
		return self.key

	def setRootVal(self, obj):
		self.key = obj

