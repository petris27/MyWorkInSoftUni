odd_set = set()
even_set = set()
for row in range(1, int(input()) + 1):
    ascii_sum_name = sum(ord(l) for l in input()) // row # ord vrushta ascii stoinost za wsqka bukwa

    if ascii_sum_name % 2 == 0: # delenie s ostatuk
        even_set.add(ascii_sum_name)
    else:
        odd_set.add(ascii_sum_name)

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_even_set == sum_odd_set:
    print(*odd_set.union(even_set), sep=", ")
elif sum_even_set < sum_odd_set:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")