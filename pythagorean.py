# Given an array of integers, write a function that returns true if there is a triplet 
# (a, b, c) that satisfies a^2 + b^2 = c^2
# python 3.x

# O(n^3) naive solution

array = [3, 1, 4, 6, 5]

# for x in array:
# 	for y in array:
# 		if y is not x:
# 			for z in array:
# 				if z is not y and z is not x:
# 					if x**2 + y**2 == z**2:
# 						print("found a triple, %d ^ 2 + %d ^ 2 = %d ^ 2" %(x, y, z))
# 						break

# O(n^2) solution?

mydict = dict()

for x in array:
	mydict[x**2] = x**2

for y in array:
	for z in array:
		if z is not y:
			try:
				if mydict[z**2-y**2] == z**2-y**2:
					print("found triple, %d ^ 2 + %d ^ 2 = %d ^ 2" %(pow((z**2 - y**2),(1/2)), y, z)) 
			except KeyError:
				continue
