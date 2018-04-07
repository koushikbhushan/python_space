"""Write a program, stored in a file named nonredundant.py, that performs the following task.
• The program prompts the user to input a file name. If there is no file with that name in the working
directory, then the program outputs an (arbitrary) error message and exits.
• The contents of the file consists of lines with text of the form R(m,n) where m and n are integers (that just
represent labels), with possibly spaces before and after the opening and closing parentheses, respectively.
It represents a partial order relation R (so an asymmetric and transitive binary relation). For instance,
the contents of the file partial_order_1.txt can be represented as:

3 5 2 1

4
It can be seen that two facts are redundant:
– the fact R(3, 1), which follows from the facts R(3, 5), R(5, 2) and R(2, 1);
– the fact R(4, 1), which follows from the facts R(4, 2) and R(2, 1).
• The program outputs the facts that are nonredundant, respecting the order in which they are listed in
the file.
Here is a possible interaction:
$ cat partial_order_1.txt
R(3,5)
R(4,2)
R(5,2)
R(2,1)
R(3,1)
R(4,1)
$ python3 nonredundant.py
Which data file do you want to use? partial_order_1.txt
The nonredundant facts are:
R(3,5)
R(4,2)
R(5,2)
R(2,1)"""

path_dict = {}
def create_dict(paths, curr):
	global path_dict
	if curr not in path_dict:
		path_dict[curr[0]] = [curr[1]]
	else:
		if curr[1] not in path_dict[curr[0]]:
			path_dict[curr[0]].append(curr[1])
	for path in paths:
		if path[0] == curr[i]:
			create_dict(paths, path)		
try:
	file_name = input('Enter the input file name:')
	f_handle = open(file_name, 'r')
	lines = f_handle.readlines()
	lines =  [line.strip() for line in lines]
	lines = list(map(lambda x: (x[2],x[4]),lines))
	
	for line in lines:
		if line[0] not in path:
			path[line[0]] = line[1]
	print(lines)
	print(path_dict)
except:
	print('No file')	