# Inplace rotate square matrix by 90 degrees
# Given an square matrix, turn it by 90 degrees in anti-clockwise direction 
# without using any extra space.

from numpy import matrix

mymatrix = matrix([[4,5,6,8], [5,7,2,9], [3,6,9,2], [1,4,7,9]])

print(mymatrix)

for i in range(0,mymatrix.shape[1]):
	temp1 = mymatrix[i,mymatrix.shape[1]]
	mymatrix[i,mymatrix.shape[1]] = mymatrix[0,-i]
	
