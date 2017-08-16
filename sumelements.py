# given an array, find out if there are two elements in it that sum to a given number

array = [3,5,7,2,4,7,8]

mydict = dict()
findsum = 14

for x in array:
	mydict.setdefault(x,[])
	mydict[x].append(x)

for x in array:
	try:
		if findsum - x == x and mydict[findsum - x][1] == findsum - x:
			print "found duplicate"
			break
		elif mydict[findsum - x][0] == findsum - x:
			print "found!"
			break
	except:
		continue