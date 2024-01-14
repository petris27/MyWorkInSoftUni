import re

def validate_username(username):
    # Define the pattern for a valid username
    pattern = r'^[a-zA-Z0-9_-]{3,16}$'
    return re.match(pattern, username) is not None

def main():
    # Read the input line containing usernames
    input_line = input("Enter usernames separated by ', ': ")

    # Split the input line into individual usernames
    usernames = input_line.split(', ')

    # Validate and print the valid usernames
    for username in usernames:
        if validate_username(username):
            print(username)

if __name__ == "__main__":
    main()