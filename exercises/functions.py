#a calculator program that can perform basic
# operations (addition, subtraction, multiplication,
# division). Write functions for each operation, and
# make sure to handle potential errors like division
# by zero.
'''
def addition(x, y):
    result = x + y
    return result

def subtraction(x, y):
    result = x - y
    return result

def multiplication(x, y):
    result = x * y
    return result

def division(x, y):
    if y != 0:
        result = x / y
        return result
    else:
        print("Error: Division denied.")

print(division(10, 20))'''

#Data types - условието е в judge
"""def data_type(type, parameter):
    result = None

    if type == "int":
        result = int(parameter) * 2
    elif type == "real":
        result = float(parameter) * 1.5
        result = "{:.2f}".format(result)
    elif type == "string":
        result = "$" + str(parameter) + "$"

    return result

type_1 = input()
parameter_2 = input()
result = data_type(type_1, parameter_2)
print(result)"""

#Center Point
def center_point(coordinates_1: list, coordinate_2: list):
    return min(coordinates_1, coordinate_2)


x = int(input())
xx = int(input())
y = int(input())
yy = int(input())
closest_point = center_point([x, xx], [y, yy])
print(f"({closest_point})")