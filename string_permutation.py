def toString(list):
	return ''.join(list)
def printPermutation(text, start, end):
	if start == end:
		print(toString(text))
	else:		
		for i in range(start, end+1):
			#swap start and ith element
			text[start], text[i] = text[i],text[start]
			printPermutation(text, start+1, end)
			text[i], text[start] = text[start],text[i]

if __name__ == '__main__':
	text = input("Enter the string")
	printPermutation(list(text), 0, len(text)-1)


