order = input().split(" ")
bakery = {}
for s in range(0, len(order), 2):
    food = order[s]
    quantities = int(order[s + 1])
    bakery[food] = quantities

searched_food = input().split(" ")
for f in searched_food:
    if f in bakery:
        print(f"We have {bakery[f]} of {f} left")
    else:
        print(f"Sorry, we don't have {f}")