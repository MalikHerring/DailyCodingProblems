def perfect_number(base):
  """Creates a perfect number given a base positive integer
  
  A perfect number is one whose digits add up to 10. Given
  a base positive number we will calculate what number to 
  add to that number to make it a perfect number. 
  
  Args:
    base: The base number that must be postive.
    
  Returns:
    A number whose digits add up to 10 or None if not possible.
  
  """
	if type(base) is not int or base < 0:
		return None
	base = str(base)
	lt = [int(x) for x in base]
	if sum(lt) > 10:
		return None
	else:
		lt.append(10-sum(lt))
	lt = [str(x) for x in lt]
	return int("".join(lt))
