"""A python program to solve sudoku
Author: Koushik Bhushan B
Date Created: 03/18/2018
Reference: https://www.geeksforgeeks.org/backtracking-set-7-suduku/
"""
UNDEFINED = 'UNDEFINED'

def is_correct_row(grid, row, num):
	if num in grid[row]:
		return False
	return True

def is_correct_col(grid, col, num):
	for i in range(9):
		if num == grid[i][col]:
			return False
	return True
			
def is_correct_box(grid, row, col, num):
	for i in range(row - row%3, (row - row%3)+3 ):
		for j in range(col-col%3,(col-col%3)+3):
			if num == grid[i][j]:
				return False
	return True
				
def is_correct_val(grid, row, col, num):
	return is_correct_row(grid, row, num) and is_correct_col(grid, col, num) and is_correct_box(grid, row, col, num)

def find_next_location(grid):
	for i in range(len(grid[0])):
		for j in range(len(grid)):
			if grid[i][j] == 0 or grid[i][j] == UNDEFINED:
				return True, i, j
	return False, -1,-1

def solve_sudoku(grid):
	found,row,col=find_next_location(grid)
	if not found:
		return True

	for num in range(1,10):
		if is_correct_val(grid, row, col, num):
			#Update current position and solve the sudoku for next location
			grid[row][col] = num
			if(solve_sudoku(grid)):
				return True
			#Control coming to this point implies that sudoku cannot be solved with current value of num for current location. 
			#Reset the current location to 0 and try with next value of num
			grid[row][col] = 0
	return False		

def print_grid(grid):
	print('---------------------')
	for i in range(len(grid[0])):
		print('', end='|')
		for j in range(len(grid)):
			if j%3 == 2:
				print(grid[i][j], end='| ')
			else:
				print(grid[i][j], end=' ')
		print('')		
		if i%3 == 2:
			print('---------------------')	
			


if __name__ == '__main__':
	grid=[[4,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,5,0,0,0,0,6,0,0],[0,0,0,0,0,0,2,5,0],[0,0,0,0,0,0,0,7,4],[0,0,0,2,0,6,3,0,0]]

	if(solve_sudoku(grid)):
		print_grid(grid)
	else:
		print('No solution')   


