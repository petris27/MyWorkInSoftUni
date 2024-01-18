from collections import deque
from datetime import datetime, timedelta
machines = {}

for r in input().split(";"):
    name, time_needed = r.split("-")
    machines[name] = [int(time_needed), 0]

production_period = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    production_period += timedelta(0, 1)
    product = products.popleft()

    nonworking_machines = []

    for name, value in machines.items():
        if value[1] != 0:
            machines[name][1] -= 1

        if value[1] == 0:
            nonworking_machines.append([name, value])

    if not nonworking_machines:
        products.append(product)
        continue

    machines_name, data = nonworking_machines[0]
    machines[machines_name][1] = data[0]
    print(f"{machines_name} - {product} [{production_period.strftime('%H:%M:%S')}]")