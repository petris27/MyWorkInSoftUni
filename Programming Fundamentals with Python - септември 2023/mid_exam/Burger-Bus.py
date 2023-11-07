total_profit = 0
number_of_cities = int(input())

for cities in range(1, number_of_cities + 1):
    city_name = input()
    owner_income = float(input())
    owner_expenses = float(input())

    if cities % 3 == 0:
        owner_expenses += owner_expenses * 0.5

    if cities % 5 == 0:
        owner_income -= owner_income * 0.1
        print(f"In {city_name} Burger Bus earned {owner_income - owner_expenses:.2f} leva.")
    else:
        print(f"In {city_name} Burger Bus earned {owner_income - owner_expenses:.2f} leva.")

    total_profit += (owner_income - owner_expenses)

print(f"Burger Bus total profit: {total_profit:.2f} leva.")