# implement binary search on a sorted array

array = [1,2,3,4,5,5,6,7,8,8,9,10,11,13,15,15,16,17,18,18,20,21,23,23,23,25,26]

def binarysearch(val, x):
	new = []
	if val == x[0]:
		print "value found"
	elif len(x) < 2:
		print "value not found in array"
	else:
		mid = int(len(x)/2) 
		if val < x[mid]:
			new = x[:mid]
			binarysearch(val,new)
		else:
			new = x[mid:]
			binarysearch(val,new)

binarysearch(4,array)