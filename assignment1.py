import random

#Generates a list L of random nonnegative integers at most equal to a given upper bound,
#of a given length, all controlled by user input.

#Outputs four lists:

#elements_to_keep, consisting of L's smallest element, L's third smallest element,
#  L's fifth smallest element, ...
#  Hint: use sorted(), list slices, and set()
#L_1, consisting of all members of L which are part of elements_to_keep, preserving
#  the original order
#L_2, consisting of the leftmost occurrences of the members of L which are part of
#  elements_to_keep, preserving the original order
#L_3, consisting of the LONGEST, and in case there are more than one candidate, the
#  LEFTMOST LONGEST sequence of CONSECUTIVE members of L that reduced to a set,
#  is a set of integers without gaps.*/

def get_input():
	lower, upper, length = raw_input("Enter lower bound, upper bound and length: ").split()
	lower, upper, length = int(lower), int(upper), int(length)
	return lower,upper, length

def generate_list(lower, upper, length):
	return random.sample(range(lower, upper), length)

def get_elements_to_keep(l):
	l_sorted = sorted(set(l))
	return l_sorted[0: len(l_sorted): 2]

def generate_l1(l, elements_to_keep):
	l1 = []
	for element in l:
		if element in elements_to_keep:
			l1.append(element)
	return l1		

def generate_l2(l, elements_to_keep):
	l2 = []
	for element in l:
		if element in elements_to_keep and element not in l2:
			l2.append(element)
	return l2	

def generate_l3(l):
	max_sub = []
	for	i in range(len(l)):
		n = i+1
		while n <= len(l):
			sub = l[i:n]
			n = n+1
			if check_consecutive(sub) :
				if len (sub) > len(max_sub):
					max_sub = sub
	return max_sub				


def check_consecutive(sub):
	if len(sub) <= 1:
		return False
	sub_sort = sorted(sub)
	i = 1
	while i < len(sub_sort):
		if sub_sort[i] !=  sub_sort[i - 1] and sub_sort[i] - sub_sort[i - 1] != 1:
			return False
		i = i+1	
	return True		

if __name__ == '__main__':
	lower, upper, length = get_input()
	l = generate_list(lower, upper, length)
	print('Main list is: ', l)
	elements_to_keep = get_elements_to_keep(l)
	print('Elements to keep: ', elements_to_keep)
	l1 = generate_l1(l, elements_to_keep)
	print('L1 is: ', l1)
	l2 = generate_l2(l, elements_to_keep)
	print('L2 is: ', l2)
	l3 = generate_l3(l)
	print('L3 is: ', l3)