def decrypt_commands(message, commands):
    for command in commands:
        tokens = command.split()
        action = tokens[0]

        if action == "Replace":
            current_char, new_char = tokens[1], tokens[2]
            message = message.replace(current_char, new_char)
            print(message)

        elif action == "Cut":
            start_index, end_index = int(tokens[1]), int(tokens[2])
            if 0 <= start_index < len(message) and 0 <= end_index < len(message):
                message = message[:start_index] + message[end_index + 1:]
                print(message)
            else:
                print("Invalid indices!")

        elif action == "Make":
            case = tokens[1]
            if case == "Upper":
                message = message.upper()
            elif case == "Lower":
                message = message.lower()
            print(message)

        elif action == "Check":
            check_string = tokens[1]
            if check_string in message:
                print(f"Message contains {check_string}")
            else:
                print(f"Message doesn't contain {check_string}")

        elif action == "Sum":
            start_index, end_index = int(tokens[1]), int(tokens[2])
            if 0 <= start_index < len(message) and 0 <= end_index < len(message):
                substring = message[start_index:end_index + 1]
                ascii_sum = sum(map(ord, substring))
                print(ascii_sum)
            else:
                print("Invalid indices!")

initial_message = input()
commands_list = []

while True:
    command = input()
    if command == "Finish":
        break
    commands_list.append(command)

decrypt_commands(initial_message, commands_list)