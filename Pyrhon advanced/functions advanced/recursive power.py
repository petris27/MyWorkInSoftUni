def recursive_power(number, power):
    if power == 1:
        return number
    return number ** power


print(recursive_power(10, 100))