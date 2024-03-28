# Minimum Number of Increments on Subarrays to Form a Target Array

def min_step_with_zeros(target):
	steps, prev = 0, 0

	for val in target:
		if val > prev:
			steps += val - prev
		prev = val

	return steps


#  Serialize and Deserialize Binary Tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



import collections

def serialize(root):
	ret = []
	q = collections.deque([root])

	while q:
		node = q.popleft()
		if node:
			ret.append(str(node.val))
			q.append(node.left)
			q.append(node.right)
		else:
			ret.append('')

	return ','.join(ret)
        

def deserialize(data):
	if not data:
		return  

	d = data.split(',')
	ret = TreeNode(d[0])
	q = collections.deque([ret])

	i = 1
	while q: 
		node = q.popleft()
		if i < len(d) and d[i]:
			node.left = TreeNode(int(d[i]))
			q.append(node.left)

		i += 1

		if i < len(d) and d[i]:
			node.right = TreeNode(int(d[i]))
			q.append(node.right)

		i += 1

	return ret

def print_tree(root): 
	if root:
		print(root.val) 
		print_tree(root.left)
		print_tree(root.right)



#  Serialize and Deserialize Trie
		
class Trie():
	def __init__(self, val) -> None:
		self.val = val
		self.children = []


# def serialize(root):
# 	ret = []
# 	q = collections.deque([root])

# 	while q:
# 		node = q.popleft()
# 		if node:
# 			ret.append(str(node.val))
# 			for child in node.children:
# 				q.append(child)
# 		else:
# 			ret.append('')

# 	return ','.join(ret)
        

# def deserialize(data):
# 	if not data:
# 		return  

# 	d = data.split(',')
# 	ret = TreeNode(d[0])
# 	q = collections.deque([ret])

# 	i = 1
# 	while q: 
# 		node = q.popleft()
# 		if i < len(d) and d[i]:
# 			child = Trie(int(d[i]))
# 			node.children.append(child)
# 			q.append(child)
# 		i += 1

# 	return ret




if __name__ == '__main__':
	# print(min_step_with_zeros([1,2,3,2,1]))

	root = TreeNode(1)
	root.left = TreeNode(2)
	right = TreeNode(3)
	right.left = TreeNode(4)
	right.right = TreeNode(5)
	root.right = right 

	serialized = serialize(root)
	print(serialized)
	print_tree(deserialize(serialized))