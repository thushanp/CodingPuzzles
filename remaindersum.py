# Check if there exist two elements in an array whose sum is equal to the sum of rest of the array

array = [2, 11, 5, 1, 4, 7]

mydict = dict()
summer = 0

for x in array:
	mydict.setdefault(x, None)
	mydict[x] = x
	summer += x

findval = summer / 2

for x in array:
	try:
		if mydict[findval - x] == findval - x:
			print "found!"
			print x, (findval - x)
			break
	except:
		continue

