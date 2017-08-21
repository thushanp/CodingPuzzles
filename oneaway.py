# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, 
# write a function to check if they are
# one edit (or zero edits) away.

onestring = "hello"
twostring = "helo"

if abs(len(onestring) - len(twostring)) > 1:
	print("failure")
elif abs(len(onestring) - len(twostring)) == 1:
	newdict = dict()
	seconddict = dict()
	for x in onestring:
		newdict.setdefault(x,0)
		newdict[x] += 1
	for y in twostring:
		seconddict.setdefault(y,0)
		seconddict[y] += 1

	for key,val in newdict.items():
		

# etc.

# add a case for if the length's are equal
