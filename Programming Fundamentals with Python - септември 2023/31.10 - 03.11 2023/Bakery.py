order = input().split(" ")
bakery = {}
for i in range(0, len(order), 2):
    food = order[i]
    quantities = order[i + 1]
    bakery[food] = int(quantities)
print(bakery)