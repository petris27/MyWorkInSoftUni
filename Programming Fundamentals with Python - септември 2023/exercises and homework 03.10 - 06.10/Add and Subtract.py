def sum_numbers(integer_one, interger_two):
    return integer_one + interger_two


def subtract(sum_result, integer_tree):
    return sum_result - integer_tree


def add_and_subtract(integer_one, interger_two, integer_tree):
    sum_of_tree = sum_numbers(integer_one, interger_two)
    result = subtract(sum_of_tree, number_tree)
    return result

number_one = int(input())
number_two = int(input())
number_tree = int(input())
print(add_and_subtract(number_one, number_two, number_tree))