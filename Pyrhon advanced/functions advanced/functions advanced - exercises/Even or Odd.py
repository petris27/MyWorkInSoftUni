def even_odd(*args):
    command = args[-1] # takes the last element of the list
    if command == "even":
        return [num for num in args[:-1] if num % 2 == 0] # takes everything, without the last one
    else:
        return [num for num in args[:-1] if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))