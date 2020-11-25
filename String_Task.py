s = input('').lower()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for i in vowels:
    s = s.replace(i, '')
a = ''
for i in s:
    i = '.' + i
    a += i

print(a)