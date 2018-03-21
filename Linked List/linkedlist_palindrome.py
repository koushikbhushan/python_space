#Reverse a linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next_node = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		node = Node(data)
		node.next_node = self.head
		self.head = node

	
	def is_palindrome_util(self, node):
		#left = 	self.head

		if node is None:
			return True
		
		is_pal_ret = self.is_palindrome_util(node.next_node)
		if is_pal_ret is False:
			return False
		is_pal =  node.data == self.head.data
		self.head = self.head.next_node
		return is_pal

	def is_palindrome(self):
		return self.is_palindrome_util(self.head)
	
	def print(self):
		start = self.head
		while start != None:
			print(start.data, end=" ")
			start = start.next_node
		print()

if __name__ == '__main__':
	elements = input('Enter elements for linked list:').split()
	linked_list = LinkedList()
	for i in elements:
		linked_list.push(i)
	print(linked_list.is_palindrome())
	linked_list.print()
