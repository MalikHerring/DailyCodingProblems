"""Problem #1 from DailyCodingProblem.com

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

"""

def sum_integers(lt, k):
	"""Return whether any two numbers from the list add up to k
	
	Given a list of integers and a k value, we will check if any
	two integers within the list add up to k. This function utilizes
	a dictionary so that we may do this in an order of O(n). Once
	the numbers have been found the function prints the numbers or
	that 'No Matches found'
	
	Args:
		lt: This is a list of integers.
		k: The integer value we are trying to add up to
	
	Returns:
		True if we found 2 numbers, or False otherwise
	
	"""
      	dt = {}
	for x in lt:
		try:
			dt[x]
			print "Found Numbers, " + str(x) + " and " + str(k-x)
			return True
		except KeyError as ke:
			dt[k-x] = True
		timesPassed += 1
	print "No Matches found"
	return False
