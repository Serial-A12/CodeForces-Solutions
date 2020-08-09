def main():
    n = int(input(''))
    solvable = 0
    problems = 0
    for i in range(n):
        array = input('').split(' ')
        for j in array:
            # if it solvable by a person then increase the number of people who can solve the problem
            if j == '1':
                solvable += 1
        # if two or more people can solve it then increase count of number of problems they can solve
        if solvable >= 2:
            problems += 1
        solvable = 0

    print(problems)

main()