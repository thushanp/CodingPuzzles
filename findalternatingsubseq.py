# Given a long list comprising of binaries digits, 0/1 in random order, 
# find the longest alternating subsequence without using extra space.

# I gave a solution in quadratic time then optimized to linear.

random = [0,1,0,1,1,1,0,0,0,1,1,1,1,0,0]

print(random)

# O(n)

tracker = 0
currentbeg = 0
currenthigh = 0

def findalternator(array):
	for i in range(0,len(array)):
		if array[i] == 0 and array[i+1] == 1:
			tracker += 1
			if tracker != 1:
				beginning = array[i]
		elif array[i] == 1 and array[i+1] == 0:
			tracker += 1
			if tracker != 1:
				beginning = array[i]
		elif tracker > currenthigh:
			currenthigh = tracker
			currentbeg = beginning
			tracker = 0

print(currentbeg, currenthigh)
