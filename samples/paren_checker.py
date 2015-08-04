from algorithms.basic.stack import Stack

def parenChecker(exp):
	exp_list = list(exp)
	s = Stack()
	for token in exp_list:
		if token == '(':
			s.push(token)
		elif token == ')':
			s.pop()

	if s.size() > 0:
		return False
	else:
		return True