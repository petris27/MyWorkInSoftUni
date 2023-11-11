#creating list using comprehation
#squares = [i for i in range(1, 11)]
#even_numbers = [u for u in range(2, 22, 2)]
#print(squares)
#print(even_numbers)


#lambda function for filtering even numbers
#slist = [1, 2, 3, 4, 5, 6]
#square = list(filter(lambda x: x % 2 == 0, slist))
#print(square)


#lambda function
#x = int(input())
#square = lambda x: x**2
#print(square(x))

#map function
#celsius = [10, 15, 20, 25, 30, -5]
#farenheit = list(map(lambda x: x * 9/5 + 32, celsius))
#print(farenheit)


#reduce function
#from functools import reduce
#numbers = [4, 76, 3, 90, 22]
#product = reduce(lambda x, y: x * y, numbers)
#print(product)


#enumerate function
#names = ["Jack", "Petris", "Milla"]
#for index, names in enumerate(names):
#    print(f"Person {index}, Name: {names}")


#zip function
#names = ["Alice", "Bob", "Charlie"]
#ages = [25, 30, 35]
#
#for name, age in zip(names, ages):
#    print(f"{name} is {age} years old.")


#list unpacking
#coordinates = (3, 7)
#x, y = coordinates
#print("x:", x)
#print("y:", y)


#problem
#Write a Python program to create a dictionary
# where the keys are names and the values are
# the corresponding scores. Use a list comprehension,
# a lambda function, and the zip function to achieve this.
# lists - 1 -names = ["Alice", "Bob", "Charlie"]
#2 - scores = [85, 92, 78]
#names = ["Alice", "Bob", "Charlie"]
#scores = [85, 92, 78]
#score_dict = {name: score for name, score in zip(names, scores)}
#print(score_dict)