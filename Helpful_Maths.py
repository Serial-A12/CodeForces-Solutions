given = input("").split("+")
# convert to normal numbers for calculation
for i in range(0, len(given)):
    given[i] = int(given[i])
# sort array algorithm
for i in range(0, len(given)):
    for j in range(0, len(given)):
        if given[i] < given[j]:
            given[j],given[i] = given[i],given[j]
# print
output=""
for i in range(-len(given), 0):
    output=output+f"{given[i]}+" if i != -1 else output+f"{given[i]}"

print(output)