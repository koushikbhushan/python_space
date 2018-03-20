#Algorithm to find the nth node from end of the linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next_node = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next_node = self.head
		self.head = new_node

	def find_nth_node_from_last(self, n):
		first_pointer = self.head
		second_pointer = self.head
		for i in range(n):
			if second_pointer != None:
				second_pointer = second_pointer.next_node
		if second_pointer == None:
			return None
		while second_pointer != None :
			second_pointer = second_pointer.next_node
			first_pointer = first_pointer.next_node
		return first_pointer.data

	def print(self):
		start = self.head
		print('Created linked list:', end=" ")
		while start != None:
			print(start.data, end=" ")
			start = start.next_node
		print()	

if __name__ == '__main__':
	elements = list(map(int, input('Enter elements for linked list:').split()))
	#print(elements)
	n = int(input('Index from last:'))
	linked_list = LinkedList()
	for i in elements:
		linked_list.push(i)

	linked_list.print()
	data = linked_list.find_nth_node_from_last(n)	
	print(f'{n} node from last is: ',data)