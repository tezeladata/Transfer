# capitalize(string)
def capitalize(*args):
    if not args: raise TypeError("Capitalize takes exactly one argument (0 given)")

    return list(args)[0][0].upper() + list(args)[0][1:]