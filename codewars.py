# Sort the Gift Code
def sort_gift_code(code):
    return "".join(sorted(code))

# Alphabet war
def alphabet_war(fight):
    left = "".join([i for i in fight if i in "wbps"]).replace("w", "4").replace("p", "3").replace("b", "2").replace("s", "1")
    right = "".join([i for i in fight if i in "mqdz"]).replace("m", "4").replace("q", "3").replace("d", "2").replace("z", "1")
    left, right = sum(int(i) for i in left), sum(int(i) for i in right)
    
    if left > right: return "Left side wins!"
    elif right > left: return "Right side wins!"
    return "Let's fight again!"

# Simple beads count
def count_red_beads(n):
    return (n-1)*2

# Filter the number
def filter_string(st):
    return int("".join([i for i in st if i.isdigit()]))

# Sum of Triangular Numbers
def sum_triangular_numbers(n):
    if n <= 0: return 0
    
    total_sum = 0
    for i in range(1, n + 1):
        triangular_number = i * (i + 1) // 2
        total_sum += triangular_number
    
    return total_sum

# Minimize Sum Of Array (Array Series #1)
def min_sum(arr):
    sorted_arr = sorted(arr)
    sum_result = 0
    for i in range(len(arr) // 2):
        sum_result += sorted_arr[i] * sorted_arr[-1 - i]
    return sum_result

# Maximum Triplet Sum (Array Series #7)
def max_tri_sum(numbers):
    return sum(sorted(set(numbers))[-3:])

# Sort arrays - 1
def sortme(names):
    return sorted(names)

# Most digits
def find_longest(numbers):
    return max(numbers, key=lambda x: len(str(x)))

# Divide and Conquer
def div_con(x):
    return sum([i for i in x if type(i) == int]) - sum([int(i) for i in x if type(i) == str])

# Convert an array of strings to array of numbers
def to_float_array(arr): 
    return [int(i) if "." not in i else float(i) for i in arr]

# Ordered Count of Characters
def ordered_count(inp):
    result = []
    seen = set()
    
    for char in inp:
        if char not in seen:
            result.append((char, inp.count(char)))
            seen.add(char)
    
    return result

# Simple remove duplicates
def solve(arr):
    seen = set()
    result = []
    
    for i in reversed(arr):
        if i not in seen:
            seen.add(i)
            result.append(i)
    
    return list(reversed(result))