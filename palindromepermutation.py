# Given a string, write a function to check if it is a permutation of a palindrome.
# The palindrome does not need to be limited to just dictionary words.


string = "Tact coa"

converted = string.lower()

newdict = dict()

for x in converted:
	if x is not " ":
		newdict.setdefault(x,0)
		newdict[x] += 1

already = False

for key,val in newdict.items():
	if val % 2 == 1:
		if already == True:
			print("not a permutation of a palindrome")
			break
		else:
			already = True