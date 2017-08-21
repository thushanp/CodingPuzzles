# given a number of digits finding the maximum number using those digits

array = [4,3,6,7,2,3,5,9,4,2]

array.sort(reverse=True)

print(''.join('%d'%x for x in array))