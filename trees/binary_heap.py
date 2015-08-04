class BinaryHeap:

	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def insert(self, obj):
		self.heapList.append(obj)
		self.currentSize = self.currentSize + 1;
		self.percUp(self.currentSize)

	def findMin(self):
		return self.heapList[1]

	def delMin(self):
		print "Unimplemented"
		# TODO fill in

	def isEmpty(self):
		isEmpty = True
		if self.currentSize > 0:
			isEmpty = False
		return isEmpty

	def size(self):
		return self.currentSize

	def buildHeap(self, list):
		print "Unimplemented"
		# TODO fill in

	def percUp(self, i):
		while i // 2 > 0:
			parentIndex = i // 2
			if self.heapList[i] < self.heapList[parentIndex]:
				temp = self.heapList[parentIndex]
				self.heapList[parentIndex] = self.heapList[i]
				self.heapList[i] = temp
			i = parentIndex
