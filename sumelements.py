array = [3,5,7,2,4,7,8]

mydict = dict()
findsum = 15

for x in array:
	mydict[x] = x

for x in array:
	try:
		if mydict[findsum - x] == findsum - x:
			continue
	except:
		print "sum not found"
		break