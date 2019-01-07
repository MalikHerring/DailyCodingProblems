"""Problem #2: Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except the one at i."""

def DailyCodingProblem(lt):
	"""Given an array of integers, return a new array such that each element at index i of the 
  new array is the product of all the numbers in the original array except the one at i."""
	product = 1
	ret_list = []
	for x in lt:
		product *= x
	for x in range(lt):
		ret_list.append(product/lt[x])
	return ret_list
