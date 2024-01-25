row_count = int(input())
martirx = []
for i in range(row_count):
    data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    martirx.append(data)
    
print(martirx)