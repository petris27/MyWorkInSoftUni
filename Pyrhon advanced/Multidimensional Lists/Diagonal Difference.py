razmer = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(razmer)]

first_summing, second_summing = 0, 0

for i in range(razmer):
    first_summing += matrix[i][i]
    second_summing += matrix[i][razmer - i - 1]

print(abs(first_summing - second_summing)) # absolute difference - namirane na absolutnata razlika
