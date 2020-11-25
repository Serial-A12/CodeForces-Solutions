from array import *
 
ints = input('').split(' ')
for i in range(len(ints)):
    ints[i] = int(ints[i])
 
m, n = ints[0], ints[1]
 
fittable = 0
 
T = [[0 for x in range(m)] for y in range(n)]
#e.g.
# [ [0, 0, 0]
#   [0, 0, 0]
#   [0, 0, 0] ]
# len(T) = 3
 
for i in range(len(T)):
    count = 0
    for j in range(len(T[i])):
        count += 1
        if count >= 2:
            fittable += 1
            count = 0
# no need to check by looping through the 2D array because 1. we know if m is not even then there'll be the last row left where we can still put dominos 2. efficiency
if m % 2 != 0:
    if n % 2 != 0:
        fittable += (n - 1) / 2
    else:
        fittable += n / 2
 
print(int(fittable))