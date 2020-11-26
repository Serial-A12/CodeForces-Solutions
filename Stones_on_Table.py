stones = int(input("")) # garbage value
inp = input("") # stone arrangement input
similars = 0
for i in range(0, len(inp)-1): # RGBBR #RRGBR
    if inp[i] != inp[i+1]:
        pass
    else:
        similars += 1
print(similars)