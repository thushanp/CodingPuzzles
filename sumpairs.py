# given an array, find if there exists a number in them that is the sum of another two numbers

# O(n^2) run-time

array = [1,2,7,9,13]

for x in array:
	for y in array:
		if x is y:
			continue
		elif x + y in array:
			print "True"
			break
	else:
		continue
	break
