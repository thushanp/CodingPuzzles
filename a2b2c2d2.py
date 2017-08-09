# Find all positive integer solutions under 1000 to a^2 + b^2 = c^2 + d^2
# python 2.7x

# How do i want to approach this?

# Each of a/b/c/d needs to be limited to < 1000, xrange solves this

# Iterate through every digit from 1-1000 would waste time
# so let's brute force first and then optimise



# Soln0: this naive version does all solutions in O(n^4)

# for a in xrange(1,100):
# 	for b in xrange(1,100):
# 		for c in xrange(1,100):
# 			for d in xrange(1,100):
# 				if a**2 + b**2 == c**2 + d**2:
# 					print "%d^2 + %d^2 = %d^2 + %d^2" %(a, b, c, d)



# Soln1: this naive version does all solutions in O(n^3)

# from __future__ import division

# for a in xrange(1,100):
# 	for b in xrange(1,100):
# 		for c in xrange(1,100):
# 			if a**2 + b**2 - c**2 >= 0:
# 				d = pow(a**2 + b**2 - c**2, 1/2)
# 				if a**2 + b**2 == c**2 + d**2:
# 					print "%d^2 + %d^2 = %d^2 + %d^2" %(a, b, c, d)



# Soln2: reduce redundancies

# from __future__ import division

# for a in xrange(1,1000):
# 	for b in xrange(1,1000):
# 		for c in xrange(1,1000):
# 			if c == a or c == b:
# 				continue
# 			else:
# 				if a**2 + b**2 - c**2 >= 0:
# 					d = pow(a**2 + b**2 - c**2, 1/2)
# 					if a**2 + b**2 == c**2 + d**2:
# 						print "%d^2 + %d^2 = %d^2 + %d^2" %(a, b, c, d)



# Soln3: dict/hash table solution, O(n^2) run-time

from __future__ import division

# declare my dictionary and n
mydict = dict()
n = 1000

# load up my dict with all pythagorean numbers as keys and the appropriate c^2+d^2 values as tuples (c,d)
for c in xrange(1,n):
	for d in xrange(1,n):
		result = c**2 + d**2
		mydict.setdefault(result,[])
		tupler = (c,d)
		mydict[result].append(tupler)

# iterates through all numbers up to n for a and b and prints the appropriate c,d values
for a in xrange(1,n):
	for b in xrange (1,n):
		result = a**2 + b**2
		list = mydict.get(result)
		if list is not None and len(list) > 1:
			for x in list:
				for y in list:
					print(x,y)