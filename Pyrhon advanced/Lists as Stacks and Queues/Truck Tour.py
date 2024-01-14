from collections import deque

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pump_data_copy = pumps_data.copy()
gas_in_tank = 0
index = 0

while pump_data_copy:
    petrol, distance = pump_data_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pumps_data.rotate(-1)
        pump_data_copy = pumps_data.copy()
        index += 1
        gas_in_tank = 0

print(index)
