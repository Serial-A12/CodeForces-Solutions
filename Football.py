inp = input("")
count = 1
for i in range(0, len(inp)-1):
    if inp[i] == inp[i+1]:
        count += 1
        if count > 6:
            print("YES")
            exit(0)
    else:
        count = 1
print("NO")