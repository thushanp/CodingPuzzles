s = "hello"

# Implement an algorithm to determine if a string has all unique characters. 
# Hash table?

# mydict = dict()
# for x in s:
# 	mydict.setdefault(x, None)
# 	if mydict[x] is None:
# 		mydict[x] = x
# 		print x
# 	else:
# 		print "there are repeated chars"
# 		break


# What if you cannot use additional data structures?

for x in xrange(0,len(s)):
	for y in s[(x+1):]:
		if s[x] == y:
			print "there are repeated chars"
			break
