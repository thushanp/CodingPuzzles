# Write an algorithm which computes the number of trailing zeros in n factorial.

# kinda messy, clean up later

n = 100

remainder = n % 5

i = (n - remainder )//5

highest = 5
z = 0

while n / highest > 1:
	highest = highest * 5
	z += 1

highest = highest // 5
z = z -1

while n - highest >= 0:
	if (n - highest) < 0:
		highest = highest // 5
		z = z -1
	i = i + z
	n = n - highest

print(i)




