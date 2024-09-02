# Twice linear
def dbl_linear(n):
    ai, bi, eq = 0, 0, 0
    sequence = [1]
    
    while ai + bi < n + eq:
        y = 2 * sequence[ai] + 1
        z = 3 * sequence[bi] + 1
        if y < z:
            sequence.append(y)
            ai += 1
        elif y > z:
            sequence.append(z)
            bi += 1
        else:
            sequence.append(y)
            ai += 1
            bi += 1
            eq += 1
    
    return sequence[-1]