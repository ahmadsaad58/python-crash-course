#  easier/better to use deque
from collections import deque

class Queue():
	def __init__(self) -> None:
		self.q = deque()

	def enqueue(self, item) -> None:
		self.q.append(item)

	def dequeue(self) -> int:
		return self.q.popleft() 
	
	def __len__(self) -> int:
		return len(self.q)
	
	def __contains__(self, target) -> bool:
		return target in self.q
	

