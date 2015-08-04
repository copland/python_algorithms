from binary_tree import BinaryTree

def buildParseTree(exp):
	exp_list = exp.split()
	expTree = BinaryTree('')
	currentTree = expTree
	for token in exp_list:
		if token == '(':
			currentTree.insertLeft('')
