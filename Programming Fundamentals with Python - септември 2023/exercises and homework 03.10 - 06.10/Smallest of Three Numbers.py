def smallest(first, second, third):
    return min(first, second, third)


number_one = int(input())
number_two = int(input())
number_tree = int(input())
smallest_number = smallest(number_one, number_two, number_tree)
print(smallest_number)