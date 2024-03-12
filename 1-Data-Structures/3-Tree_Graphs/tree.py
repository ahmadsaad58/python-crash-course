class TreeNode():
	def __init__(self, val) -> None:
		self.left = None
		self.right = None
		self.val = val

def bfs(root): 
	if not root:
		return
	
	# Initialize a queue with the root node
	q = [root] 

	while q:
		# Dequeue the current node
		node = q.pop(0)

		# logic to do something with BFS
		print(node.val)

		# Enqueue the left child
		if node.left:
			q.append(node.left)

		# Enqueue the right child
		if node.right:
			q.append(node.right)


def dfs(root):
	if not root: 
		return
	
	s = [root]

	while s:
		# pop the top node
		node = s.pop()

		# logic to do something with DFS
		print(node.val)

		# push the left child
		if node.left:
			s.append(node.left)

		# push the right child
		if node.right:
			s.append(node.right)


def dfs_recursive(root, ans):
	if not root: 
		return 
	print(root.val)
	dfs(root.left)
	dfs(root.right)



def main():
	root = TreeNode(10)
	left = TreeNode(5)
	right = TreeNode(15)
	left_2 = TreeNode(0)
	right_2 = TreeNode(20)
	root.left = left
	root.right = right 
	left.left = left_2
	right.right = right_2


	# bfs(root)
	print(dfs(root))
	# dfs_recursive(root)





if __name__ == '__main__':
	main()

