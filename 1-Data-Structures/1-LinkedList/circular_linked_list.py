from linked_list import Node

# circular Linked List

class Circular_Linked_List():
	def __init__(self) -> None:
		self.head = None

	def traverse(self, start=None): 
		if not start:
			start = self.head
		curr = start
		while curr.next != start:
			yield curr
			curr = curr.next
		yield curr
	
	def print_list(self, start=None):
		return '->'.join([str(curr.data) for curr in self.traverse(start)])
	
	def __reversed__(self):
		prev = None
		curr = self.head
		curr.next, prev, curr = prev, curr, curr.next
		while curr != self.head:
			curr.next, prev, curr = prev, curr, curr.next
		self.head.next = prev
		self.head = prev
		return self

	
if __name__ == '__main__':
	a = Node("a")
	b = Node("b")
	c = Node("c")
	d = Node("d")
	a.next = b
	b.next = c
	c.next = d
	d.next = a
	c_list = Circular_Linked_List()
	c_list.head = a
	print(c_list.print_list())
	print(reversed(c_list).print_list())