# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to O.

from numpy import matrix
import numpy as np

mymatrix = matrix([[4,5,3,8,4,8,4], [5,7,0,7,2,9,4], 
	[3,7,9,6,9,2,3], [1,4,7,4,0,9,2], [1,2,4,7,4,7,5], [2,5,8,4,6,8,9]])

print(mymatrix)
new = mymatrix

for x in range(0,mymatrix.shape[0]):
	for y in range(0,mymatrix.shape[1]):
		if mymatrix[x,y] != 0:
			continue
		else:
			for z in range(0,mymatrix.shape[0]):
				new[z,y] = 0
			for l in range(0,mymatrix.shape[1]):
				new[x,l] = 0

print(mymatrix)
print(new)
