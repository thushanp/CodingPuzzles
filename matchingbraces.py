from collections import deque

inpt = "[{()}]"

def checker(braces):
	# first split up the stirng into a list of chars, and make a deque
	lst = list(braces)
	d = deque([])
	mydict = dict()
	posschar = ["{","[","(", ")", "}", "]"]
	for z in posschar:
		mydict.setdefault(z, 0)
	# iterate through chars making a deque
	for x in lst:
		if (x == "{" or x == "[" or x == "("):
			d.append(x)
			mydict[x] += 1
		elif (x == "}" or x == "]" or x == ")"):
			if (x == "}" and mydict["{"] < 1) or (x == "]" and mydict["["] < 1) or (x == ")" and mydict["("] < 1):
				print("fail! there's too many/few of", x)
				exit()
			if (x == "}" and (d.pop()) != "{") or (x == "]" and (d.pop()) != "[") or (x == ")" and (d.pop()) != "("):
				print("fail!", x, "is not matching properly")
				exit()
			mydict[x] -= 1

		else:
			print("input string is wrong")
			exit()


checker(inpt)