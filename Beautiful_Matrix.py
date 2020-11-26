matrix = []
moves = 0
for a in range(0, 5):
    row = input(f"").split(" ")
    matrix.append(row)

# mid point of matrix, i,j = 3,3
# find location of 1

i, j = 0, 0
for a in range(0, len(matrix)): # rows
    for b in range(0, len(matrix[a])): # columns
        if matrix[a][b] == '1':
            i, j = a + 1, b + 1 # + 1 to move from zero indexing to one indexing
            # subtract from mid point to see how many times i and j should move to get to 3, 3 
            print( abs(i - 3) + abs(j - 3) )
            exit(0)