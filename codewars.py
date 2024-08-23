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

# How many pages in a book?
def amount_of_pages(summary):
    total_digits = 0
    page = 0
    
    while total_digits < summary:
        page += 1
        total_digits += len(str(page))
    
    return page

# Positions Average
def pos_average(s):
    substrings = s.split(", ")
    n = len(substrings)
    length = len(substrings[0])
    total_positions = n * (n - 1) // 2 * length
    matching_positions = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(length):
                if substrings[i][k] == substrings[j][k]:
                    matching_positions += 1

    return (matching_positions / total_positions) * 100

# What's A Name In?
def name_in_str(strng, name):
    strng = strng.lower()
    name = name.lower()
    name_index = 0
    
    for char in strng:
        if char == name[name_index]:
            name_index += 1
        if name_index == len(name):
            return True
    
    return False

# Are we alternate?
def is_alt(s):
    for i in range(len(s[:-1])):
        if s[i] in "aeiou":
            if s[i+1] in "aeiou": return False
        if s[i] not in "aeiou":
            if s[i+1] not in "aeiou": return False
    
    return True

# Arrays Similar
def arrays_similar(seq1, seq2):
    def count_elements(seq):
        element_count = {}
        for element in seq:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1
        return element_count
    
    return count_elements(seq1) == count_elements(seq2)

# Shortest steps to a number
def shortest_steps_to_num(num):
    steps = 0
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps

# Custom FizzBuzz Array
def fizz_buzz_custom(string_one="Fizz", string_two="Buzz", num_one=3, num_two=5): 
    res = []
    
    for i in range(1, 101):
        if i%num_one == 0 and i%num_two == 0: res.append(string_one + string_two)
        elif i%num_one == 0 and i%num_two != 0: res.append(string_one)
        elif i%num_one != 0 and i%num_two == 0: res.append(string_two)
        else: res.append(i)
    
    return res

# Alphabet war - airstrike - letters massacre
def alphabet_war(fight):
    fight_list = list(fight)
    for i in range(len(fight)):
        if fight[i] == '*':
            if i > 0:
                fight_list[i-1] = '_'
            fight_list[i] = '_'
            if i < len(fight) - 1:
                fight_list[i+1] = '_'
    
    fight = ''.join(fight_list)
    left_side_power, right_side_power = {'w': 4, 'p': 3, 'b': 2, 's': 1}, {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_score, right_score = sum(left_side_power.get(ch, 0) for ch in fight), sum(right_side_power.get(ch, 0) for ch in fight)
    
    if left_score > right_score: return "Left side wins!"
    elif right_score > left_score: return "Right side wins!"
    else: return "Let's fight again!"

# Simple Sentences
def make_sentences(parts):
    res = parts[0]
    
    for i in parts[1:]:
        if i == ',': res += ','
        else: res += ' ' + i
    return res.rstrip(' .') + '.'

# Only Duplicates
def only_duplicates(st):
    return "".join([i for i in st if st.count(i) > 1])

# Find within array
def find_in_array(seq, predicate):
    for index, value in enumerate(seq):
        if predicate(value, index):
            return index
    return -1

# Most Frequent Weekdays
from datetime import datetime, timedelta

def most_frequent_days(year):
    days_count = {day: 0 for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
    
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    num_days = 366 if is_leap else 365
    
    current_date = datetime(year, 1, 1)
    
    for _ in range(num_days):
        weekday = current_date.strftime('%A')
        days_count[weekday] += 1
        current_date += timedelta(days=1)
    
    max_count = max(days_count.values())
    
    most_frequent = [day for day, count in days_count.items() if count == max_count]
    
    return most_frequent

# Ackermann Function
def Ackermann(m, n, calls=[0]):
    calls[0] += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return Ackermann(m - 1, 1, calls)
    else:
        inner_result = Ackermann(m, n - 1, calls)
        return Ackermann(m - 1, inner_result, calls)

def get_ackermann_result(m, n):
    calls = [0]
    result = Ackermann(m, n, calls)
    return result, calls[0]

# Error correction #1 - Hamming Code
def encode(string):
    ascii = [ord(i) for i in string]
    binary = [bin(i)[2:] for i in ascii]
    eight = ["0"*(8-len(i))+i for i in binary]
    triples = []
    for i in eight:
        res = ""
        for x in i:
            res += 3*x
        triples.append(res)
    return "".join(triples)

def decode(s):
    triples = [s[i:i+3] for i in range(0, len(s), 3)]
    corrected = [0 if str(i).count("0") > str(i).count("1") else 1 for i in triples]
    bytes = [corrected[i:i+8] for i in range(0, len(corrected), 8)]
    bytes_upt = []
    for i in bytes: bytes_upt.append("".join([str(x) for x in i]))
    ascii = [int(i, 2) for i in bytes_upt]
    chars = [chr(i) for i in ascii]
    return "".join(chars)

# Prime Factors
def prime_factors(num):
    if num < 2:
        return []
    
    factors = []
    n = 2

    while n**2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    
    if num > 1:
        factors.append(num)

    return factors

# More Zeros than Ones
def more_zeros(s):
    binary, filtered = [bin(ord(i))[2:] for i in s], []
    for i in binary:
        if i.count("0") > i.count("1"): filtered.append(i)
    res = [chr(int(i, 2)) for i in filtered]
    fin = []
    for i in res:
        if i not in fin: fin.append(i)
    return fin

# Simple Simple Simple String Expansion
def string_expansion(s):
    res = []
    num = 1
    for i in s:
        if i.isdigit():
            num = int(i)
        else:
            res.append(num * i)
    return ''.join(res)