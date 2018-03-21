# Given a matrix with each cell containing each number of candies, and a constraint that you can move only right or down, 
#from the top left corner to the bottom right corner, find the path that gets you maximum candies.
def find_max_path(matrix,n,m):
	#define a cost matrix
	cost_matrix = [[[0, '0'] for x in range(m)] for x in range(n)]
	cost_matrix[0][0] = [matrix[0][0], str(matrix[0][0])]

	#Populate cost of first row
	for i in range(1, n):
		cost_matrix[i][0] = [cost_matrix[i-1][0][0]+matrix[i][0], cost_matrix[i-1][0][1]+'->'+str(matrix[i][0])]

	#Populate cost of first column
	for i in range(1, m):
		cost_matrix[0][i] = [cost_matrix[0][i-1][0]+matrix[0][i], cost_matrix[0][i-1][1]+'->'+str(matrix[0][i])]

	for i in range(1, n):
		for j in range(1, m):
			if cost_matrix[i-1][j][0] > cost_matrix[i][j-1][0]:
				cost_matrix[i][j] = [matrix[i][j] + cost_matrix[i-1][j][0], cost_matrix[i-1][j][1]+'->'+str(matrix[i][j])]
			else:
				cost_matrix[i][j] = [matrix[i][j] + cost_matrix[i][j-1][0], cost_matrix[i][j-1][1]+'->'+str(matrix[i][j])]

	return cost_matrix[n-1][m-1][0], cost_matrix[n-1][m-1][1]

if __name__ == "__main__":
	n = int(input('Enter the number of rows'))
	matrix=[]    
	for i in range(n):
		lst=list(map(int,input().split()))
		matrix.append(lst)
	max_candies,max_path = find_max_path(matrix,n,len(matrix[0]))
	print(f'Max candies:{max_candies} can be collected in {max_path}')

