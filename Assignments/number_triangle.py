"""Write a program, stored in a file named triangle.py, that performs the following task.
• The program prompts the user to input a file name. If there is no file with that name in the working
directory, then the program outputs an (arbitrary) error message and exits.
• The contents of the file consists of some number of lines, each line being a sequence of integers separated
by at least one space, with possibly spaces before and after the first and last number, respectively, the
Nth line having exactly N numbers. For instance, the contents of the file triangle_1.txt can be
displayed as follows.

7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

• The program outputs:
– the largest value than can be obtained by summing up all numbers on a path that starts from the
top of the triangle, and at every level down to the penultimate level, goes down to the immediate
left or right neighbour;
– the number of paths that yield this largest value;
– the leftmost such path, in the form of a list."""

max_sum = 0
path = []
max_path = []
num_path = 0
def find_sum(tree, row, col, sum):	
	global max_sum
	global path
	global max_path
	global num_path
	path.append(tree[row][col])
	if len(tree) <= row+1:
		if sum > max_sum:`
			max_path = path[:]
			max_sum = sum
			num_path = 1
		elif sum == max_sum:
			num_path += 1
		return
	
			

	find_sum(tree, row+1, col, sum+tree[row+1][col])
	path.pop()
	find_sum(tree, row+1, col+1, sum+tree[row+1][col+1])
	path.pop()

f_handle = open('triangle.txt', 'r')
lines = f_handle.readlines()
lines = [line.strip() for line in lines]
lines = map(lambda e: [int(i) for i in e.split()], lines)
tree = list(lines)
find_sum(tree, 0,0,tree[0][0])
print('Largest sum: ', max_sum)
print('Number of paths: ',num_path)
print('Leftmost path: ',max_path)
