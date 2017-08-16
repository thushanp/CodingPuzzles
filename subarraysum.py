# Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.


array = [4,6,3,7,8,3]
sumval = 18
summer = 0

runningsum = []

for x in array:
	runningsum.append(x)
	summer = summer + x
	while summer > sumval:
		z = runningsum.pop(0)
		summer = summer - z
	if summer == sumval:
		print("found it, the subarray is:", runningsum)
		break