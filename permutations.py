# Design an algorithm to print all permutations of a string.
# For simplicity, assume all characters are unique. 

# s = "test"
# temp = []
# for x in s:
# 	temp.append(x)

# permutations = []

# for i in xrange(0, len(s)):
# 	store = temp[:i] + temp[i+1:]
# 	for y in xrange(0, (len(s)-i)):
# 		new = store[:i] + [temp[i]] + store[(i+y):]
# 		permutations.append(new)

# print permutations

def Permute(string):
    if len(string) == 0:
        return ['']
    prevList = Permute(string[1:len(string)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(string)):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList

string = '\n'.join(Permute('abc'))
print string