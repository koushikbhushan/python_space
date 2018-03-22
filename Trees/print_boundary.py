class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None



def printLeftNodes(tree):
	if tree:
		if tree.left:
			print(tree.data)
			printLeftNodes(tree.left)
		elif tree.right:
			print(tree.data)
			printLeftNodes(tree.right)	


def printLeafNodes(tree):
	if tree:
		printLeafNodes(tree.left)
		if tree.left is None and tree.right	is None:
			print(tree.data)
		printLeafNodes(tree.right)

def printRightNodes(tree):
	if tree:
		if tree.right:
			printRightNodes(tree.right)
			print(tree.data)
		elif tree.left:
			printRightNodes(tree.left)
			print(tree.data)		

if __name__ == '__main__':
	root = Node(20)
	root.left = Node(8)
	root.left.left = Node(4)
	root.left.right = Node(12)
	root.left.right.left =  Node(10)
	root.left.right.right = Node(14)
	root.right = Node(22)
	root.right.right = Node(25)
	printLeftNodes(root)
	printLeafNodes(root)
	printRightNodes(root.right)