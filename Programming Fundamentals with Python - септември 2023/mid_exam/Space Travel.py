route = input().split("||")
initial_fuel = int(input())
initial_ammunition = int(input())

for command in route:
    command_parts = command.split()
    action = command_parts[0]

    if action == "Travel":
        distance = int(command_parts[1])
        if initial_fuel >= distance:
            initial_fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print("Mission failed.")
            break

    elif action == "Enemy":
        enemy_armor = int(command_parts[1])
        if initial_ammunition >= enemy_armor:
            initial_ammunition -= enemy_armor
            print(f"An enemy with {enemy_armor} armor is defeated.")
        else:
            fuel_needed_to_escape = enemy_armor * 2
            if initial_fuel >= fuel_needed_to_escape:
                initial_fuel -= fuel_needed_to_escape
                print(f"An enemy with {enemy_armor} armor is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    elif action == "Repair":
        ammunition_added = int(command_parts[1]) * 2
        fuel_added = int(command_parts[1])  # Corrected index
        initial_ammunition += ammunition_added
        initial_fuel += fuel_added
        print(f"Ammunitions added: {ammunition_added}.")
        print(f"Fuel added: {fuel_added}.")

    elif action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break