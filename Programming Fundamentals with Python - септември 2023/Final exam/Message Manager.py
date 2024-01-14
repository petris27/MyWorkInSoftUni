def message_manager(capacity, commands):
    users = {}

    for command in commands:
        tokens = command.split('=')
        action = tokens[0]

        if action == 'Add':
            username, sent, received = tokens[1], int(tokens[2]), int(tokens[3])
            if username not in users:
                users[username] = {'sent': sent, 'received': received}

        elif action == 'Message':
            sender, receiver = tokens[1], tokens[2]
            if sender in users and receiver in users:
                users[sender]['sent'] += 1
                users[receiver]['received'] += 1

                if users[sender]['sent'] + users[sender]['received'] == capacity:
                    print(f"{sender} reached the capacity!")
                    del users[sender]
                if users[receiver]['sent'] + users[receiver]['received'] == capacity:
                    print(f"{receiver} reached the capacity!")
                    del users[receiver]

        elif action == 'Empty':
            username = tokens[1]
            if username == 'All':
                users.clear()
            elif username in users:
                del users[username]

        elif action == 'Statistics':
            break

    print(f"Users count: {len(users)}")
    for username, messages in (users.items()):
        print(f"{username} - {messages['sent'] + messages['received']}")

capacity = int(input())
commands_list = []

while True:
    command = input()
    if command == "Statistics":
        break
    commands_list.append(command)

message_manager(capacity, commands_list)