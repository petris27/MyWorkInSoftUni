def sorting_cheeses(**kwarges):
    r = ""
    result = sorted(kwarges.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for cheese_name, quantities in result:
        r += cheese_name + "\n"
        for quantities in sorted(quantities, reverse=True):
            r += f"{quantities}\n"
    return r



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
