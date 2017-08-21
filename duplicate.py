# given a list of numbers find the one that occurs twice

array = [4,2,5,2,9,1,8,3,10]

mydict = dict()

for x in array:
	mydict.setdefault(x,None)
	if mydict[x] != None:
		print("found the duplicate, it's %d" %x)
		break
	else:
		mydict[x]=x

