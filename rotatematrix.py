# Inplace rotate square matrix by 90 degrees
# Given an square matrix, turn it by 90 degrees in anti-clockwise direction 
# without using any extra space.


from numpy import matrix
import numpy as np

mymatrix = matrix([[4,5,6,8], [5,7,2,9], [3,6,9,2], [1,4,7,9]])

print(mymatrix)

# with extra space
print(mymatrix[0,:])
x = [element for element in mymatrix[0] for element in sublist]
print(x)
