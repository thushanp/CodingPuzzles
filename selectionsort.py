# initialise array

s = [5,6,3,6,7,3,2]

print s


sortedlst = []
storage = s

while len(storage) != 0:
	temp = storage[0]
	for x in storage:
		if temp > x:
			temp = x
	sortedlst.append(temp)
	storage.remove(temp)

print sortedlst