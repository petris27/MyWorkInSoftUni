def func_executor(*func_data):
    result = []

    for func, args in func_data:
        result.append(f"{func.__name__} - {func(*args)}")

    return "\n".join(result)

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

