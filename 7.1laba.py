m = int(input("Введите размер матрицы: "))
matrix = []
for i in range(m):
    a = []
    for j in range(m):
        a.append(int(input(f"Введите элемент [{i}][{j}]: ")))
    matrix.append(a)
count = 0
for i in range(m):
    for j in range(m):
        if i > j and matrix[i][j] < 0:
            count += 1
print(f"Количество отрицательных элементов ниже побочной диагонали: {count}")
