import re

def is_valid_password(password):
    pattern = r'^(.+?)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$'
    match = re.match(pattern, password)
    return match is not None

def encrypt_password(password):
    pattern = r'^.+?>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<.+$'
    match = re.match(pattern, password)
    if match:
        numbers, lower_case, upper_case, symbols = match.groups()
        encrypted_password = numbers + lower_case + upper_case + symbols
        return encrypted_password
    else:
        return "Invalid password format"

def main():
    n = int(input())
    inputs = [input() for _ in range(n)]

    for password in inputs:
        if is_valid_password(password):
            encrypted_password = encrypt_password(password)
            print(f"Password: {encrypted_password}")
        else:
            print("Try another password!")

if __name__ == "__main__":
    main()