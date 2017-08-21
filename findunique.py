# in a given array filled with duplicates except for one digit, find the one that's not repeated

# O(2n)

array = [1,1,3,3,6,6,3,3,8,2,2,5,5,9,9,9,3,3,5,5]

uniques = dict()
build = []

for x in array:
	uniques.setdefault(x, None)
	if uniques[x] == x or uniques[x] == "duped":
		uniques[x] = "duped"
		try:
			build.remove(x)
		except ValueError:
			continue
	else:
		uniques[x] = x
		build.append(x)

print(''.join("%d" % i for i in build))