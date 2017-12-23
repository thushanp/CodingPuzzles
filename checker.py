lst = [0,1,2,3,4,5,6,7,8,9,10]

for a in lst:
	for b in lst:
		for c in lst:
			for d in lst:
				if ((a*c + 2*b*d)%11 == 0) and ((a*d + b*c)%11 == 0):
					if (a == 0 & b == 0) or (c == 0 & d == 0):
						break
					else:
						print(a,b,c,d)