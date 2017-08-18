# Given a long list comprising of binaries digits, 0/1 in random order, 
# find the longest alternating subsequence without using extra space.

# O(n) solution here:

second = [1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0]


def findalternator(array):
	tracker = 0
	currentbeg = 0
	currenthigh = 0
	for i in range(0,len(array)):
		if i != len(array) - 1:
			if array[i] == 0 and array[i+1] == 1:
				tracker += 1
				if tracker == 1:
					beginning = array[i]
			elif array[i] == 1 and array[i+1] == 0:
				tracker += 1
				if tracker == 1:
					beginning = array[i]
			elif tracker > currenthigh:
				currenthigh = tracker + 1
				currentbeg = beginning
				tracker = 0
			else:
				tracker = 0
	return currentbeg, currenthigh

print(findalternator(second))
