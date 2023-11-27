while True:
    string = input()

    if string.lower() == "end":
        break

    print(f'{string} = {string[::-1]}')