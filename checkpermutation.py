s = "testing"
second = "testgin"

newdict = dict()
seconddict = dict()

for x in s:
	newdict.setdefault(x,None)
	if newdict[x] is not None:
		newdict[x] = newdict[x] + 1
	else:
		newdict[x] = 0

for x in second:
	seconddict.setdefault(x,None)
	if seconddict[x] is not None:
		seconddict[x] = seconddict[x] + 1
	else:
		seconddict[x] = 0

for y in s:
	if newdict[y] != seconddict[y]:
		print "they are not anagrams!"
