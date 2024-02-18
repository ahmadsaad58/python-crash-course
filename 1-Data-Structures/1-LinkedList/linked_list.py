# simple linked list class

class Node():
	def __init__(self, data) -> None:
		self.data = data
		self.next = None

	def __str__(self) -> str:
		return f'{self.data}->{self.next}'
	
	def __repr__(self) -> str:
		return f'Node(data={self.data})'
	
	def __eq__(self, __value) -> bool:
		if isinstance(__value, Node):
			return self.data == __value.data
		else:
			return self.data == __value 
		
	def __del__(self) -> None:
		# print('Deleting: {}'.format(self.data))
		pass

class DoubleNode(Node):
	def __init__(self, data) -> None:
		super().__init__(data)
		self.prev = None
	
	def __str__(self) -> str:
		return f'{self.prev}->{self.data}->{self.next}'

class Linked_List():
	def __init__(self, head=None) -> None:
		self.head = head

	def __len__(self) -> int:
		return sum(1 for _ in self)
	
	def __contains__(self, target) -> bool:
		for curr in self: 
			if curr == target:
				return True
		return False
	
	def __reversed__(self): 
		prev, curr = None, self.head
		while curr: 
			curr.next, prev, curr = prev, curr, curr.next
		self.head = prev
		return self
	
	def __bool__(self):
		return self.head
			
	def append(self, item) -> None:
		# check type and convert all to Nodes
		if isinstance(item, list):
			start = Linked_List.__create_node_from_list(item)
		elif isinstance(item, Node):
			start = item
		else: 
			start = Node(item)
		if not self.head:
			self.head = start
		else:
			for curr in self:
				pass
			curr.next = start 

	def __create_node_from_list(nodes: list): 
		start = Node(nodes[0])
		curr = start
		for element in nodes[1:]: 
			curr.next = Node(element)
			curr = curr.next
		return start
		
	def __iadd__(self, item):
		self.append(item)
		return self
	
	def push(self, node) -> None:
		node.next = self.head
		self.head = node

	def add_after(self, target, node) -> None:
		if not self.head:
			raise Exception('No Head')
		for curr in self:
			if curr == target:
				node.next, curr.next = curr.next, node
				return
		raise Exception('Target: {} does not exist'.format(target))
	
	def add_before(self, target, node) -> None:
		if not self.head:
			raise Exception('No Head')
		if target == self.head:
			self.push(node)
			return
		prev = self.head
		for curr in self:
			if curr == target:
				prev.next, node.next = node, curr
				return
			prev = curr
		raise Exception('Target: {} does not exist'.format(target))
	
	def pop(self) -> None:
		curr = self.head
		self.head = self.head.next
		return curr.data
	
	def remove(self, target):
		if not self.head:
			raise Exception('No Head')
		if target == self.head:
			self.pop()
			return
		prev = self.head
		for curr in self:
			if curr == target:
				prev.next = curr.next
				curr.next = None
				return
			prev = curr
		raise Exception('Target: {} does not exist'.format(target))
	
	def __isub__(self, target):
		self.remove(target)
		return self
				
	def __iter__(self):
		curr = self.head
		while curr:
			yield curr
			curr = curr.next 
	
	def __str__(self) -> str:
		ret = [str(curr.data) for curr in self]
		ret.append('NONE')
		return '->'.join(ret)
		
	

if __name__ == '__main__':
	my_node = Node(5)
	my_list = Linked_List(my_node)
	my_list.append(Node(6))
	my_list.append(Node(7))
	my_list.append(Node(8))
	my_list.append(9)
	my_list.append([12, 13, 14, 15])
	my_list += 16
	my_list.push(Node(2))
	# print(my_list)
	my_list.add_after(Node(2), Node(4))
	my_list.add_after(Node(15), Node(16))
	my_list.add_before(4, Node(3))
	my_list.add_before(2, Node(1))
	print(my_list)
	print("Popped", my_list.pop())
	my_list.remove(2)
	my_list -= 16
	my_list.remove(8)
	print(my_list)
	print(len(my_list))
	print(5 in my_list)
	my_list -= 3
	my_list -= 4
	my_list -= 5
	my_list -= 6
	my_list -= 7
	my_list -= 9
	print(my_list)
	print(reversed(my_list))
	my_double_node = DoubleNode(5)
	print(my_double_node)