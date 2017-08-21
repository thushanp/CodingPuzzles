# Given a long list comprising of binaries digits, 0/1 in random order, 
# build the longest possible alternating sequence without using extra space.

# quadratic O(n^2) solution

random = [0,1,0,1,1,1,0,0,0,1,1,1,1,0,0]

print(random)

for i in range(0,len(random)-1):
	if random[i] == 0:
		for x in range(i,len(random)):
			if random[x] == 1:
				del random[x]
				random.insert(i+1,1)
	elif random[i] == 1:
		for x in range(i,len(random)):
			if random[x] == 0:
				del random[x]
				random.insert(i+1,0)

print(random)

