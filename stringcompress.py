# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. 
# If the "compressed" string would not become smaller than the original string, 
# your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z).

string = "aabcccccaaad"

i = 1
result = []

for x in range(0,len(string)):
	if x != len(string) - 1 and string[x] == string[x+1]:
		i += 1
	else:
		result.append("%s%d" %(string[x], i))
		i = 1


if len(result)*2 <= len(string):
	print("".join(result))
else:
	print(string)