import random
M = 5
matrix = [[random.randint(1, 100) for _ in range(M)] for _ in range(M)]
for a in range(M):
    for i in range(M):
        for j in range(M-1):
            if matrix[j][a] < matrix[j+1][a]:
                for k in range(M):
                    matrix[j][k], matrix[j+1][k] = matrix[j+1][k], matrix[j][k]
for a in matrix:
    print(a)
