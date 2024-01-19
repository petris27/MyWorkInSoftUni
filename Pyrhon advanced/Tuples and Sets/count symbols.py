unique_letter = {}
for letter_symbols in input():
    unique_letter[letter_symbols] = unique_letter.get(letter_symbols, 0) + 1 #adding the letter of the given word - in the breckets the function goes like this: if the letter is
    # not found two times or more, the program adds +1 to the 0, but if the letter
    # IS found, the programs adds +1 to the 0, because it appears in the input and
    # then adds as much numbers as it's found in the entire input

for letter, times_founded in sorted(unique_letter.items()):
    print(f"{letter}: {times_founded} time/s")