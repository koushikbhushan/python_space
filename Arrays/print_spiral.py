#Given a matrix, print the elements in spiral order
matrix = [[1,2,7],[3,4,5],[8,6,7]]
row_start = 0
col_start = 0
row_end = len(matrix[0])
col_end = len(matrix)

i=row_start
while row_start<row_end and col_start<col_end:
	for i in range(col_start, col_end):
		print(matrix[row_start][i], end=" ")
	row_start += 1

	for i in range(row_start,row_end):
		print(matrix[i][col_end-1], end=" ")
	col_end -= 1

	if row_end > row_start:
		for i in range(col_end-1, col_start-1,-1):
			print(matrix[row_end-1][i], end=" ")
		row_end -= 1
		
	if col_end > col_start:
		for i in range(row_end-1, row_start-1,-1):
			print(matrix[i][col_start], end=" ")	
		col_start += 1		 	