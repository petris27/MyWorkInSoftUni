row = int(input())
matrix = []
for _ in range(row):
    matrix.append([int(el) for el in input().split()])

sum = 0
for row_index in range(row):
    for col_index in range(row):
        if row_index == col_index:
            sum += matrix[row_index][col_index]
print(sum)