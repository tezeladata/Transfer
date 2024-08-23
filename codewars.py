# Integer depth
def compute_depth(n):
    res = set()
    count = 0
    
    while len(res) < 10: 
        count += 1
        mult = n * count
        res.update(str(mult)) 
    
    return count

# Simple Fun #79: Delete a Digit
def delete_digit(n):
    all_combinations = []
    n_str = str(n)
    
    for i in range(len(n_str)):
        new_number = int(n_str[:i] + n_str[i+1:])
        all_combinations.append(new_number)
    
    return max(all_combinations)

# Collatz
def collatz(n):
    res = [str(n)]
    
    while n!= 1:
        if n%2 == 0:
            n //= 2
            res.append(str(n))
        else:
            n = n*3 + 1
            res.append(str(n))
    
    return "->".join(res)

# Calculate the area of a regular n sides polygon inside a circle of radius r
import math

def area_of_inscribed_polygon(circle_radius, number_of_sides):
    angle = 2 * math.pi / number_of_sides
    area = 0.5 * number_of_sides * (circle_radius ** 2) * math.sin(angle)
    return area

# Strip Url Params
def strip_url_params(url, params_to_strip=None):
    if '?' not in url:
        return url
    
    base_url, query_string = url.split('?', 1)
    params = query_string.split('&')
    
    seen = {}
    result = []
    
    for param in params:
        key, value = param.split('=')
        if key not in seen:
            if not params_to_strip or key not in params_to_strip:
                seen[key] = value
                result.append(f"{key}={value}")
    
    if result:
        return f"{base_url}?" + "&".join(result)
    else:
        return base_url
    
# Duplicate Arguments
def solution(*args):
    st = list(args)
    for i in st:
        if st.count(i)>1: return True
    return False

# Srot the inner ctonnet in dsnnieedcg oredr
def sort_the_inner_content(words):
    return " ".join([
        word[0] + "".join(sorted(word[1:-1], reverse=True)) + word[-1] if len(word) > 2 else word
        for word in words.split(" ")
    ])

# Round by 0.5 steps
def solution(n):
    n = float(n)  
    int_part = int(n)  
    frac_part = n - int_part  
    
    if 0.25 <= frac_part < 0.75:
        return int_part + 0.5
    elif frac_part >= 0.75:
        return int_part + 1
    else:
        return int_part
    
# Irreducible Sum of Rationals
def gcd(x, y):
    return y == 0 and x or gcd(y, x % y)

def lcm(x, y):
    return abs(x * y) // gcd(x, y)

def sum_fracts(lst):
    if not lst:
        return None


    common_denom = lst[0][1]
    for _, denom in lst[1:]:
        common_denom = lcm(common_denom, denom)
    
    numerator_sum = sum(numer * (common_denom // denom) for numer, denom in lst)
    
    common_divisor = gcd(numerator_sum, common_denom)
    numerator_sum //= common_divisor
    common_denom //= common_divisor


    if common_denom == 1: return numerator_sum
    return [numerator_sum, common_denom]

# Almost Even
def split_integer(num, parts):
    base_size = num // parts 
    remainder = num % parts  
    
    result = [base_size + 1] * remainder + [base_size] * (parts - remainder)
    
    return sorted(result)

# String average
def average_string(s):
    all = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    for i in s.split(" "):
        if i not in all: return "n/a"
    
    res = int(sum([all[i] for i in s.split(" ")]) / len(s.split(" ")))
    
    for key, val in all.items():
        if res == val: return key

# Row of the odd triangle
def odd_row(n):
    start = 2 * (n * (n - 1) // 2) + 1
    return [start + 2 * i for i in range(n)]

# Compare Versions
def compare_versions(version1,version2):
    v1, v2 = calc(version1), calc(version2)
        
    return True if v1>=v2 else False
    
def calc(v):
    start = 1
    res = 0
    
    for i in [int(i) for i in v.split(".")]:
        res += i*start
        start /= 10
    
    return res