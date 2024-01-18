n = int(input())
cars = set() # set
for _ in range(n): # for-loop for second line of input
    direction, car_number = input().split(", ")

    if direction == "IN": # if function for adding and removing info from the set
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)

if cars: #printing as much cars as it's in the set, using for-loop and if
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")