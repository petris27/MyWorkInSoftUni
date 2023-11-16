def all_the_ch(first: str, second: str) -> list:
    characters = []
    for current_ch in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_ch))
    return characters


f_ch = input()
s_ch = input()
final_result = all_the_ch(f_ch, s_ch)
print(" ".join(final_result))