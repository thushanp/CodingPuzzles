# k largest(or smallest) elements in an array 
# Question: Write an efficient program for printing k largest elements in an array. 
# Elements in array can be in any order.

# For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the 
# largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.

# merge sort method? O(nlog(n))

array = [1, 23, 12, 9, 30, 2, 50]

def mergesort(x):
	result = []
	if len(x) < 2:
		return x

	mid = int(len(x)/2)

	y = mergesort(x[:mid])
	z = mergesort(x[mid:])

	i = 0
	j = 0

	while i < len(y) and j < len(z):
		if y[i] > z[j]:
			result.append(z[j])
			j += 1
		else:
			result.append(y[i])
			i += 1


	result += y[i:]
	result += z[j:]

	return result

array = mergesort(array)
start = len(array) - 3
print(array[start:])