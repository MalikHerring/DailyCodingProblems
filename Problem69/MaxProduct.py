def max_product(int_list):
  """Finds the largest product of any 3 numbers from a list
  
  Given a list of integers, return the largest product that 
  can be made by multiplying any three integers.
  
  Args:
    int_list: A list of integers.
    
  Returns:
    None if the list is too small, else the highest product
  """  
	if len(int_list) < 3:
		return None
	int_list = sorted(int_list)
	lower = int_list[0] * int_list[1] * int_list[-1]
	upper = int_list[-1] * int_list[-2] * int_list[-3]
	return (lower if lower > upper else upper)
