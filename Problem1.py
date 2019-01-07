"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."""

def DailyCodingProblem(lt, k):
  """Given a list, lt, of numbers and a number k, return whether any two numbers from the list add up to k"""
	timesPassed = 0
      dt = {}
	for x in lt:
		try:
			dt[x]
			print "Found Numbers, " + str(x) + " and " + str(k-x)
			print "Times passed: " + str(timesPassed)
			return
		except KeyError as ke:
			dt[k-x] = True
		timesPassed += 1
	print "No Matches found"
	print "Times passed: " + str(timesPassed)
	return
