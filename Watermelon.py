def main():
    weight = int(input(''))
    if check(weight) == 1:
        print("YES")
    else:
        print("NO")

def check(n):
    for i in range(1, n):
        if i % 2 == 0 and (n - i) % 2 == 0:
            return 1

    return 0
    
main()