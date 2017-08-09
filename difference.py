# Given an array of distinct integer values, count the number of pairs of integers that
# have difference k. For example, given the array {1, 7, 5, 9, 2, 12, 3} and the difference
# k = 2, there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9)

# list = [1,7,5,9,2,12,3]

# for x in list:
# 	for y in list:
# 		if abs(x-y) == 2:
# 			print x,y

# run-time is O(n^2)

# hash table?

list = [1,7,5,9,2,12,3]
difference = 2
counter = 0

mydict = dict()

for x in list:
	print x
	mydict[x] = x

print "\n"

for y in list:
	print "value", y
	try:
		if(mydict[y + difference] is not None or mydict[y - difference] is not None):
			counter = counter + 1
			print counter
	except:
		continue


# 1 3