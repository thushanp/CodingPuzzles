# Check if there exist two elements in an array whose sum is equal to the sum of rest of the array
# python 3.7.x
import sys

array = [2, 11, 5, 1, 4, 7]

mydict = dict()
summer = 0

for x in array:
	mydict.setdefault(x, None)
	mydict[x] = x
	summer += x

findval = summer / 2
find2 = summer // 2

if findval != find2:
	print("doesn't exist")
	sys.exit()

for x in array:
	try:
		if mydict[find2 - x] == find2 - x:
			print ("found!")
			print (x, (find2 - x))
			break
	except:
		continue

