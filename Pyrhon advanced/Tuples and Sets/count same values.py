typle_a = tuple([float(element) for element in input().split()]) #a tuple with a comprehension
unique_elements = {} # a dictionary

for n in typle_a:
    if n not in unique_elements: # using the dictionary to store the info of the tuple and use it to print it easely
        unique_elements[n] = typle_a.count(n)

for el, inn in unique_elements.items(): # giving a specific name to the numbers in the console and returning view object, which contains the key-value of the dictionary
    print(f"{el} - {inn} times")

