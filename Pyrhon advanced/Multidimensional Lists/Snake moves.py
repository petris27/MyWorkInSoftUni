from collections import deque

rows, columns = [int(x) for x in input().split()]
word = list(input())

copy = deque(word)

for row in range(rows):
    while len(copy) < columns:
        copy.extend(word)

    if row % 2 == 0:
        print(*[copy.popleft() for _ in range(columns)], sep="")
    else:
        print(*[copy.popleft() for _ in range(columns)][::-1], sep="")