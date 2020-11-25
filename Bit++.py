add = '++x'
add2 = 'x++'
sub = '--x'
sub2 = 'x--'
 
n = int(input(''))
m = []
for i in range(n):
    m.append(input('').lower())
 
x = 0
for i in m:
    if i == add or i == add2:
        x += 1
    elif i == sub or i == sub2:
        x -= 1
    
print(x)