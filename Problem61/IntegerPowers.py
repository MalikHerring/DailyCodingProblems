"""Problem #61 from DailyCodingProblem.com

Implement integer exponentiation. That is, implement the pow(x, y) function, 
where x and y are integers and returns x^y.

"""

def intpow(base, power):
	"""Used to calculate integer exponentiation
	
	Given a base and a power we use a recursive method that
	maintains a speed faster than a for loop of repeated 
	multiplication as we increase it by double every time.
	
	Args:
		base: The base number we are exponentiating
		power: Number of times we multiply base by itself, must be positive
	
	Returns:
		This returns base^power
	
	"""
	if power is 0:
		return 1
	if power is 1:
		return base
	if (power & 1) is not 0:
		return base * intpow(base * base, power // 2)
	else:
		return intpow(base * base, power // 2)
