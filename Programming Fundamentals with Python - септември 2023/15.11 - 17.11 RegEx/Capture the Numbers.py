import re

def extract_numbers_from_text(text):
    pattern = r'\d+'
    numbers = re.findall(pattern, text)
    return numbers

def main():
    extracted_numbers = []
    while True:
        user_input = input("Enter a string (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        extracted_numbers.extend(extract_numbers_from_text(user_input))

    print("Extracted numbers:", ' '.join(extracted_numbers))

if __name__ == "__main__":
    main()