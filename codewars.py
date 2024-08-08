# Fix string case
def solve(s):
    if len([i for i in s if i.islower()]) > len([i for i in s if i.isupper()]): return s.lower()
    elif len([i for i in s if i.islower()]) < len([i for i in s if i.isupper()]): return s.upper()
    else: return s.lower()

# Maximum Length Difference
def mxdiflg(a1, a2):
    if not a1 or not a2:  return -1

    len_a1, len_a2 = [len(s) for s in a1], [len(s) for s in a2]

    max_len_a1 = max(len_a1)
    min_len_a1 = min(len_a1)
    max_len_a2 = max(len_a2)
    min_len_a2 = min(len_a2)

    return max(abs(max_len_a1 - min_len_a2), abs(max_len_a2 - min_len_a1))

# Largest 5 digit number in a series
def solution(digits):
    return int(max([i for i in [digits[i-5:i] for i in range(4, len(digits)+1)]]))

# Are the numbers in order?
def in_asc_order(arr):
    return arr == list(sorted(arr))

# Triangular Treasure
def triangular(n):
    return n*(n+1) // 2 if n > 0 else 0

# Number of Decimal Digits
def digits(n):
    return len(str(n))

# Flatten and sort an array
def flatten_and_sort(array):
    res = []
    
    for i in array:
        if type(i) != list: res.append(i)
        else: 
            for x in i:
                res.append(x)
    
    return list(sorted([i for i in res if i!=[]]))
# or:
def flatten_and_sort(array):
    return sorted(x for i in array for x in (i if isinstance(i, list) else [i]))