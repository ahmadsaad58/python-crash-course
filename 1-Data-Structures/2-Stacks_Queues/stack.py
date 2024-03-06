
# homemade stack 

class Stack():
	def __init__(self) -> None:
		self.stack = []

	def __len__(self) -> int:
		return len(self.stack)
	
	def __contains__(self, target) -> bool:
		return target in self.stack
		
	def push(self, item) -> None:
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[-1]
	
class Minstack():
	def __init__(self) -> None:
		self.stack_ = []
		self.min_stack = []

	def push(self, item) -> None: 
		self.stack_.append(item)
		if not self.min_stack or self.min_stack[-1] > item: 
			self.min_stack.append(item)

	def pop(self) -> None:
		if self.stack_.pop() == self.min_stack[-1]:
			self.min_stack.pop()

	def top(self) -> int:
		return self.stack_[-1]
	
	def get_min(self) -> int:
		 return self.min[-1]	
	

#  easier/better to use deque
from collections import deque

def is_valid(s):
	valid_beginnings = '({['
	valid_endings = ')}]'
	valid_mappings = {key : value for key, value in zip(valid_endings, valid_beginnings)}

	stack_ = deque()

	for char in s: 
		if char in valid_beginnings:
			stack_.append(char)
		if char in valid_endings:
			if len(stack_) == 0 or valid_mappings[char] != stack_.pop():
				return False
			
	return len(stack_) == 0






        
if __name__ == '__main__':
	print('starting')
	for test in ["()[]{}", '()', '(]']:
		print(is_valid(test))