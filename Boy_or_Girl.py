name = []
for i in (input("")):
    name.append(i)
name = list(dict.fromkeys(name)) # convert list to dictionary - this gets rid of duplicates - then reconvert to list
output = "CHAT WITH HER!" if (len(name) % 2 == 0) else "IGNORE HIM!"
print(output)