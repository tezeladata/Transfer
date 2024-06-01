# Pair of gloves
def number_of_pairs(gloves):
    return sum([gloves.count(i) // 2 for i in list(set(gloves))])

# Handshake problem
def get_participants(handshakes):
    if handshakes == 0: return 0

    n = 2 
    while True:
        if n * (n - 1) // 2 >= handshakes:
            return n
        n += 1

# Multi-tap Keypad Text Entry on an Old Mobile Phone
def presses(phrase):
    comb = {
            '1ADGJMPTW *#': 1,
            'BEHKNQUX0': 2,
            'CFILORVY': 3,
            '23456S8Z': 4,
            '79': 5
        }
    
    return sum(value for char in phrase.upper() for key, value in comb.items() if char in key)