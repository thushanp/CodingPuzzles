# better binary search
# uses two indices instead of recursion so you can return the index value
# uses less memory

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # this two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x

print(binary_search([1,2,3,4,5,5,6,7,8,8,9,10,11,13,15,15,16,17,18,18,20,21,23,23,23,25,26], 4))