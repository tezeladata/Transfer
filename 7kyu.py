# Looking for a benefactor
def new_avg(arr, newavg):
    result = round(newavg * (len(arr) + 1) - sum(arr))
    if result <= 0: raise ValueError("The result must be a positive value.")
        
    return result + 1 if (sum(arr) + result) / (len(arr)+1) < newavg else result

# Interactive Dictionary
class Dictionary():
    def __init__(self):
        self.d = {}
        
    def newentry(self, word, definition):
        self.d[word] = definition
        return self.d
        
    def look(self, key):
        return self.d[key] if key in self.d.keys() else f"Can't find entry for {key}"
    
# Check for prime numbers
def is_prime(n):
    if n in [0, 1]: return False
    for i in range(2, int(n*0.5)):
        if n%i == 0: return False
    return True

# Previous multiple of three
def prev_mult_of_three(n):
    res = str(n)
    for i in range(len(res)):
        if int(res) %3 == 0: return int(res)
        else: res = res[:-1]
    return None

# Filter Long Words
def filter_long_words(sentence, n):
    return [i for i in sentence.split(" ") if len(i) > n]

# Basic Math (Add or Subtract)
def calculate(s):
    s = s.replace("plus", "+").replace("minus", "-")
    tokens = []
    num = ""
    for char in s:
        if char in "+-":
            if num:
                tokens.append(num)
                num = ""
            tokens.append(char)
        else:
            num += char
    if num:
        tokens.append(num)

    start = int(tokens[0])
    for i in range(1, len(tokens), 2):
        op, num = tokens[i], int(tokens[i + 1])
        if op == "+":
            start += num
        elif op == "-":
            start -= num
    return str(start)

# Dictionary from two lists
def create_dict(keys, values):
    res = {}
    for i in range(len(keys)):
        res[f"{keys[i]}"] = values[i] if i < len(values) else None
    
    return res

# Number Pairs
def get_larger_numbers(a, b):
    return [a[i] if a[i] > b[i] else b[i] for i in range(len(a))]

# Float Precision
def solution(n):
    return round(n, 2)

# String Merge!
def string_merge(string1, string2, letter):
    start = string1.split(letter)[0] + letter
    for i in range(len(string2)):
        if string2[i] == letter:
            start += string2[i+1:]
            break
    
    return start

# Multiples!
def multiple(x):
    if x%3 == 0 and x%5 == 0: return "BangBoom"
    elif x%3 == 0: return "Bang"
    elif x%5 == 0: return "Boom"
    return "Miss"

# Trimming a string
def trim(string, max_length):
    if max_length <= 3:
        return string[:max_length] + "..." if len(string) > max_length else string
    return string[:max_length - 3] + "..." if len(string) > max_length else string

# last digits of a number
def solution(n,d):
    return [int(i) for i in str(n)[-d:]] if d > 0 else []

# Find all occurrences of an element in an array
def find_all(arr, n):
    return [i for i in range(len(arr)) if arr[i] == n]

# Find sum of top-left to bottom-right diagonals
def diagonal_sum(array):
    return sum(array[i][i] for i in range(len(array)))

# Return a sorted list of objects
def sort_list(sort_by, lst):
    return sorted(lst, key=lambda x: x[sort_by], reverse=True)