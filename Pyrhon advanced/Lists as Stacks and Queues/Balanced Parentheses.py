parentheses = input()

stack = []
opening_brackets = {'(': ')', '[': ']', '{': '}'}

for bracket in parentheses:
    if bracket in opening_brackets:
        stack.append(bracket)
    else:
        if not stack or opening_brackets[stack.pop()] != bracket:
            print("NO")
            break
else:
    if not stack:
        print("YES")