__author__ = 'Chris Opland'

class Sorter:

	def __init__(self):
		pass
	
	"""
	Bubble Sort 
	  Iterates through the least multiple times, comparing adjacent values and 
	  swapping them if they are out of order.
	Analysis:
   	  Worst Case: O(n^2) - all the numbers need to be changed
	  Avg Case: O( (n^2) / 2 ) - half the numbers need to be changed
	  Best Case: O(1) - no exchanges made
	"""
	def bubble_sort(self, alist):
		unsorted = True
		length = len(alist)
		while(unsorted):
			unsorted = False
			for i in range(1,length):
				if alist[i-1] > alist[i]:
					lower = alist[i]
					alist[i] = alist[i-1]
					alist[i-1] = lower
					unsorted = True
		return alist
	"""
	Selection Sort
	  Interates through the list n-1 times, finds the highest value in the list
	  and places it in the appropriate spot.
	Analysis:
	  Worst Case: O(n^2)
	  Avg Case: O( (n^2)/2 )
	  Best Case: O(1)
	"""
	def selection_sort(self, alist):
		for fillslot in range(len(alist)-1, 0, -1):
			maxPos = 0
			for location in range(1, fillslot+1):
				if alist[location] > alist[maxPos]:
					maxPos = location

			temp = alist[fillslot]
			alist[fillslot] = alist[maxPos]
			alist[maxPos] = temp
	
		return alist	

	"""
	Insertion Sort 
	  Maintains a sorted sublist in the lower positions of the list. Each new
	  item is then 'inserted' back into the sublist in its appropriate spot.
	Analysis:
	  Worst Case: O(n^2)
	  Avg Case: O( (n^2) / 2 )
	  Best Case: O(1)
	"""
	def insertion_sort(self, alist):
		for item in range(1, len(alist)):
			currentVal = alist[item]
			currentPos = item
			while currentPos > 0 and  alist[currentPos-1] > currentVal:
				alist[currentPos] = alist[currentPos-1]
				currentPos = currentPos - 1;
			
			alist[currentPos] = currentVal

		return alist


	"""
	Shell Sort - a.k.a Diminishing Increment Sort
	  Maintains number of smaller sublists, each of which is sorted using
	  Insertion Sort. The sort uses an increment i, called the gap, to create 
	  a sublist by choosing all items that are i items apart.
	Analysis:
	  Tends to fall somewhere O(n) and O(n^2) based on the gap. 
	"""
	def shell_sort(self, alist):
		sublistcount = len(alist)//2
		while sublistcount > 0:
			for startpos in range(sublistcount):
				self.__gapInsertionSort(alist, startpos, sublistcount)
			print("After increments of size", sublistcount, "The list is", alist)

			sublistcount = sublistcount // 2

		return alist

	def __gapInsertionSort(self, alist, start, gap):
		for i in range(start+gap, len(alist), gap):
			currentVal = alist[i]
			pos = i
			while pos >= gap and alist[pos - gap] > currentVal:
				alist[pos] = alist[pos-gap]
				pos = pos-gap

			alist[pos] = currentVal


	"""
	Merge Sort
	Analysis:
	
	"""
