rows, columns = [int(number) for number in input().split(", ")]
matrix = []

for first_step in range(rows):
    rows_broi = [int(num) for num in input().split()]
    matrix.append(rows_broi)

for column_index in range(columns):
    col_total = 0
    for row_index in range(rows):
        col_total += matrix[row_index][column_index]
    print(col_total)
