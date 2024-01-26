golemina = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(golemina)]
primary = [matrix[r][r] for r in range(golemina)] # making the first diagonal
second = [matrix[r][golemina - r - 1] for r in range(golemina)] # making the second diagonal
# with this way we use comprehension to use several finctions on one line
# on the first diagonal we just take one element from every row to form diagonal
# on the second one, to form reverse diagonal we use formula(golemina - r - 1) to make backwards
# movement through the rows of the matrix

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)} ")
print(f"Secondary diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")