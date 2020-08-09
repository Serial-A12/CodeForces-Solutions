def main():
    n = int(input(''))
    words = []
    for i in range(n):
        words.append(input(""))

    for i in range(len(words)):
        if len(words[i]) > 10:
            words[i] = words[i][0] + str(len(words[i]) - 2) + words[i][-1]
        print(words[i])

main()