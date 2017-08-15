# can you search an ordered matrix in linear time? O(n)

from numpy import matrix
from numpy import linalg

A = matrix( [[1,2,9,10],[7,11,12,15],[21,24,27,29]])

print A
print A.shape

def searcher(x,i=0,j=A.shape[1]-1):
	print A[i, j]
	if A[i,j] == x:
		return "True"
	try:
		if x > A[i,j]:
			print "going down\n"
			searcher(x,i,j+1)
		elif x < A[i,j]:
			print "going left\n"
			searcher(x,i-1,j)
		else:
			return "Value not found"
	except:
		return "Value not found"

searcher(12)