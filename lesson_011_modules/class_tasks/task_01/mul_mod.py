from add_mod import add

def mul(a, b):
    result = 0
    for _ in range(abs(b)):
        result = add(result, abs(a))

    if (a < 0 and b > 0) or (a > 0 and b < 0):
        result = -result

    return result
