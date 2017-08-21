# Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. 
# You may assume that the array was originally sorted in increasing order.

# find 5 in l5, 16, 19, 20, 25, 1, 3, 4, 5, 7, l0, 14

array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

find = 10

def finder(array, find):
	if len(array) == 1:
		if array[0] == find:
			print("found at %d" %0)
		else:
			print("failure")

	beg = 0
	end = len(array) - 1

	while beg < end:
		mid = beg + (end - beg)//2
		if array[mid] == find:
			return(mid)
		if array[mid] < array[end]:
			if array[mid] < find and find < array[end]:
				beg = mid
			else:
				end = mid
		elif array[beg] < array[mid]:
			if find < array[mid] and array[beg] < find:
				end = mid
			else:
				beg = mid

	# if array[mid] == find:
	# 	print("found!")
	# elif beg <= find and find < array[mid]:
	# 	finder(array[:mid], find, (array[:mid])[0], (array[:mid])[-1])
	# elif array[mid] < find and find <= end:
	# 	print("going up")
	# 	finder(array[mid:], find, (array[mid:])[0], (array[mid:])[-1])
	# else:
	# 	print("not found!")

print(finder(array,find))
