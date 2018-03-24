def check_triangle(grid,i,j,count):
	if i >= len(grid)-1:
		return False	
	if count-2 == 1:
		if grid[i+1][j-1] == 1:
			return True
		return False
	for n in range(j-count+1, j-1):
		if grid[i+1][n+1] != 1:
			return False
	return check_triangle(grid, i+1, n+1, count-2)		


def find_triangle_pattern(grid, n):
	triangle_count = 0
	for i in range(n):
		count = 0
		for j in range(n):
			if grid[i][j] == 1:
				count+= 1
			else:
				count = 0	
			if count > 1 & count%2 == 1:
				if check_triangle(grid,i,j,count):
					triangle_count += 1
	return triangle_count

def rotate_matrix(grid):
	n = len(grid)
	for i in range(0, int(n/2)):
		for j in range(i, n-i-1):
			temp =	grid[i][j]
			grid[i][j] = grid[j][n-1-i]
			grid[j][n-1-i] = grid[n-1-i][n-1-j]
			grid[n-1-i][n-1-j] = grid[n-1-j][i]
			grid[n-1-j][i] = temp
	return grid

def print_matrix(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			print(grid[i][j], end=" ")
		print()
			
grid = [[4,2,1,1,1,1,1],[8,7,9,1,1,1,2],[3,9,4,4,1,5,7],[3,9,4,4,1,5,7],[3,9,4,4,1,5,7],[3,9,4,4,1,5,7],[3,9,4,4,1,5,7]]
#print(check_triangle(grid, 0, 6, 5))
#print(check_triangle([[1,1,1],[2,2,2]], 0, 2, 3))
#South
print_matrix(grid)
triangle_count = find_triangle_pattern(grid,7)
print("Number of triangles to south: ",triangle_count)	
	
print("***********************")
rotate_matrix(grid)
print_matrix(grid)
triangle_count = find_triangle_pattern(grid,7)
print("Number of triangles to west: ",triangle_count)

print("***********************")
rotate_matrix(grid)
print_matrix(grid)	
triangle_count = find_triangle_pattern(grid,7)
print("Number of triangles to north: ",triangle_count)

print("***********************")
rotate_matrix(grid)
print_matrix(grid)	
triangle_count = find_triangle_pattern(grid,7)
print("Number of triangles to east: ",triangle_count)

