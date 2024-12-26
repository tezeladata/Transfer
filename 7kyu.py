# Array Leaders (Array Series #3)
def array_leaders(numbers):
    res = []
    for i in range(len(numbers)):
        if numbers[i] > sum(numbers[i+1:]): 
            res.append(numbers[i])
    
    return res

# Nth power rules them all!
def modified_sum(a, n):
    return sum([i**n for i in a]) - sum(a)

# Evens and Odds
def evens_and_odds(n):
    return bin(n)[2:] if n%2 == 0 else hex(n)[2:]

# Return the closest number multiple of 10
def closest_multiple_10(i):
    return (i // 10)*10 if i%10 < 5 else (i // 10 + 1)*10

# Basic JS - Calculating averages
class Calculator:
    @staticmethod
    def average(*args):
        return sum(args) / len(args) if len(args) > 0 else 0
    
# Selective fear of numbers
def am_I_afraid(day,num):
    match day:
        case "Monday": return False if num != 12 else True
        case "Tuesday": return False if num <= 95 else True
        case "Wednesday": return False if num != 34 else True
        case "Thursday": return False if num != 0 else True
        case "Friday": return False if num %2 == 1 else True
        case "Saturday": return False if num != 56 else True
        case "Sunday": return False if num != 666 and num != -666 else True

# Numbers to Letters
def switcher(arr):
    alp, res = 'zyxwvutsrqponmlkjihgfedcba!? ', ""
    return "".join([alp[int(i) - 1] for i in arr])

# Difference Of Squares
def difference_of_squares(n):
    return sum(range(n+1))**2 - sum([i**2 for i in range(n+1)])

# String Reordering
def sentence(lst):
    renewed = []
    for diction in lst:
        for key, value in diction.items(): renewed.append([int(key), value])
    return " ".join(i[1] for i in sorted(renewed, key = lambda x: x[0]))