chat_history = []

while True:
    command = input()
    if command == "end":
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == "Chat":
        message = command_parts[1]
        chat_history.append(message)

    elif action == "Delete":
        message = command_parts[1]
        if message in chat_history:
            chat_history.remove(message)

    elif action == "Edit":
        message = command_parts[1]
        edited_message = command_parts[2]
        if message in chat_history:
            index = chat_history.index(message)
            chat_history[index] = edited_message

    elif action == "Pin":
        message = command_parts[1]
        if message in chat_history:
            chat_history.remove(message)
            chat_history.append(message)

    elif action == "Spam":
        messages = command_parts[1:]
        chat_history.extend(messages)

for message in chat_history:
    print(message)