matrix_row, matrix_cow = [int(x) for x in input().split(", ")]
summed_numbers = 0
matrix = []


for relay in range(matrix_row):
    row_of_matrix = [int(row) for row in input().split(", ")]
    summed_numbers += sum(row_of_matrix)
    matrix.append(row_of_matrix)

print(summed_numbers)
print(matrix)