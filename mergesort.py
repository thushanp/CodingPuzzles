def msort3(x):

    # initialise my results array
    result = []

    # case for when we get to single elements
    if len(x) < 2:
        return x

    # find middle of the given array
    mid = int(len(x) / 2)

    # recursively sort lower and upper half
    y = msort3(x[:mid])
    z = msort3(x[mid:])

    # initialise counters
    i = 0
    j = 0

    # iterate through both halves appending to results array
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1

    # concatenate the lower and upper half
    result += y[i:]
    result += z[j:]
    return result

print(msort3([3,5,1,4,6,3,2,6,3,4]))
