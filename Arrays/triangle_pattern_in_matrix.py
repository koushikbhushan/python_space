from random import seed, randint

def check_triangle(grid,i,j,count, size):
    if i >= len(grid)-1:
        return False,size
    if count-2 == 1:
        if grid[i+1][j-1] != 0:#grid[i+1][j-1] == 1
            size = size+1
            return True,size
        return False,size
    for n in range(j-count+1, j-1):
        if grid[i+1][n+1] == 0:#grid[i+1][n+1] != 1
            return False,size
    is_tri,size = check_triangle(grid, i+1, n+1, count-2, size) 
    return is_tri,size+1


def find_triangle_pattern(grid, n):
    triangle_size_dict = {}
    triangle_count = []
    dict_already_tracked = {}
    for i in range(n):
        count = 0
        start_point = 0
        while start_point < n:
            #print("Start", start_point)
            for j in range(start_point,n):
                if grid[i][j] != 0:#grid[i][j] == 1
                    #if count == 0:
                    #    start_point += 1
                    count+= 1
                else:
                    count = 0
                    #start_point += 1
                    #break

                if count > 1 & count%2 == 1:
                    #print(i,j,count)
                    str_track_key = str(i)+'>'+str(j)+'>'+str(count)
                    if str_track_key in dict_already_tracked:
                        break;   
                    dict_already_tracked[str_track_key] = True    
                    is_triangle, size = check_triangle(grid,i,j,count, 1)
                    if is_triangle:
                        if size in triangle_size_dict:
                            triangle_size_dict[size] = triangle_size_dict[size]+1
                        else:
                            triangle_size_dict[size] = 1
            count = 0
            start_point += 1
            #print("Start",start_point)  
        #print(triangle_size_dict)           
    for size,count in   triangle_size_dict.items():
        triangle_count.append((size,count))
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
			print(int(grid[i][j] != 0), end=" ")
			#print(grid[i][j], end=" ")
		print()
			
#grid = [[4,2,1,1,1,1,1],[8,7,9,1,1,1,2],[3,9,4,4,1,5,7],[3,9,4,4,1,5,7],[3,9,4,4,1,5,7],[3,9,4,4,1,5,7],[3,9,4,4,1,5,7]]
#dim=7
#print(check_triangle(grid, 0, 6, 5))
#print(check_triangle([[1,1,1],[2,2,2]], 0, 2, 3))
#South

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')


print_matrix(grid)
triangle_count = find_triangle_pattern(grid, dim)
print("Number of triangles to south: ",triangle_count)	
	
print("***********************")
rotate_matrix(grid)
print_matrix(grid)
triangle_count = find_triangle_pattern(grid,dim)
print("Number of triangles to west: ",triangle_count)

print("***********************")
rotate_matrix(grid)
print_matrix(grid)	
triangle_count = find_triangle_pattern(grid,dim)
print("Number of triangles to north: ",triangle_count)

print("***********************")
rotate_matrix(grid)
print_matrix(grid)	
triangle_count = find_triangle_pattern(grid,dim)
print("Number of triangles to east: ",triangle_count)

