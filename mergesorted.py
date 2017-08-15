# You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.

a = [1,2,3,5,6,7]
b = [3,6,8,9,10,11,15]

def merger(a,b):
	result = []
	i = 0
	j = 0

	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			result.append(a[i])
			i = i + 1
		else:
			result.append(b[j])
			j = j + 1

	result += a[i:]
	result += b[j:]
	return result

print(merger(a,b))