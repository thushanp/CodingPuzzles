a = [2]
b = [3]
c = [9]
d = [5, 17]
e = [3]
f = [6]

listoflists = [a,b,c,d,e,f]

print listoflists

flattened = [item for sublist in listoflists for item in sublist]

print flattened