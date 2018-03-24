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

	def reverse(self):
		prev = None
		curr = self.head

		while curr != None:
			next = curr.next_node
			curr.next_node = prev
			prev = curr
			curr = next
		self.head = prev
	
	def reverse_recursive_util(self, curr, prev):
		if curr.next_node == None:
			self.head = curr
			curr.next_node = prev
			return
		
		next = curr.next_node
		curr.next_node = prev
		self.reverse_recursive_util(next, curr)

	def reverse_recursive(self):
		self.reverse_recursive_util(self.head, None)
				
			
	def print(self):
		start = self.head
		while start != None:
			print(start.data, end=" ")
			start = start.next_node
		print()

if __name__ == '__main__':
	elements = list(map(int, input('Enter elements for linked list:').split()))
	print('********Iterative*********')
	linked_list = LinkedList()
	for i in elements:
		linked_list.push(i)

	print('Original list:' ,end=" ")
	linked_list.print()
	linked_list.reverse()	
	print('Reverse list:' ,end=" ")
	linked_list.print()

	print('********Recursive*********')
	linked_list = LinkedList()
	for i in elements:
		linked_list.push(i)

	print('Original list:' ,end=" ")
	linked_list.print()
	linked_list.reverse_recursive()	
	print('Reverse list:' ,end=" ")
	linked_list.print()