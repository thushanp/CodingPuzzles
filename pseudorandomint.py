# random integer generator 0-9, type in two single numbers between which to generate

import random

string = input()

alpha = int(string.split(",")[0])
beta = int(string.split(",")[1])

print(random.randint(alpha,beta))