# implement binary search from memory

def binary_search(array, find):
	beg = 0
	end = len(array)

	while beg < end:
		mid = beg + (end - beg)//2
		if array[mid] == find:
			return mid
		elif array[mid] < find:
			if beg == mid:
				return "not found"
			beg = mid
		elif array[mid] > find:
			end = mid


print(binary_search([1,2,3,4,5,5,6,7,8,8,9,10,11,13,15,15,16,17,18,18,20,21,23,23,23,25,26], 4))