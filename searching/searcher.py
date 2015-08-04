class Searcher:

    	def __init__(self):
        	pass

	def search(self, alist, item, search_type):
		if search_type == "sequential":
			self.sequential_search(alist, item)
		elif search_type == "binary":
			self.binary_search(alist, item)
	
	def sequential_search(self, alist, item):
        	pos = 0
        	for thing in alist:
            		if thing == item:
                		return True
        	return False

	def binary_search(self, alist, item):
		middle = len(alist)/2
        	if alist[middle] == item:
            		return True
        	elif len(alist) == 1 and alist[0] != item:
            		return False
        	elif alist[middle] < item:
            		return self.binary_search(alist[middle+1:len(alist)], item)
        	else:
            		return self.binary_search(alist[0:middle], item)
