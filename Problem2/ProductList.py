"""Problem #2 from DailyCodingProblem.com

Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except the one at i.

"""

def DailyCodingProblem(lt):
	""" Generates a list of products.
		
	Given an array of integers, return a new array such 
	that each element at index i of the new array is the 
	product of all the numbers in the original array except 
	the one at i.
	
	Args: 
		lt: List of integers.
		
	Returns:
		Returns a new list of integers where each index
		is the product of all numbers besides the number
		at that index from lt.

	"""
	product = 1
	ret_list = []
	for x in lt:
		product *= x
	for x in range(lt):
		ret_list.append(product/lt[x])
	return ret_list
