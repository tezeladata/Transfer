# Basic Sequence Practice
def sum_of_n(n):
    if n == 1: return [0, 1]
    res = []    
    
    if n >= 1:
        for i in range(n+1): res.append(sum(range(i+1)))
    else:
        for i in range(0, n-2, -1): res.append(sum(range(-1, i, -1)))
    
        return res[1:]
    return res

# Building Strings From a Hash
def solution(pairs):
    return ",".join(f"{i} = {pairs[i]}" for i in pairs)

# All unique
def has_unique_chars(string):
    seen_chars = set()
    for char in string:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True

# Largest Elements
def largest(n, xs):
    return sorted(xs)[-n:] if n!= 0 else []

# Nth Smallest Element (Array Series #4)
def nth_smallest(arr, pos):
    return sorted(arr)[pos-1]

# Return the Missing Element
def get_missing_element(seq): 
    return [i for i in range(10) if i not in seq][0]

# Sum of all arguments
def sum_args(*args):
    return sum(args)

# Nickname Generator
def nickname_generator(name):
    if len(name) < 4: return "Error: Name too short"
    res = name[:3]
    return res if res[-1] not in "aeiou" else name[:4]

# shorter concat [reverse longer]
def shorter_reverse_longer(a,b):
    if len(b) > len(a): a, b = b, a
    
    return f"{b}{a[::-1]}{b}"

# JavaScript Array Filter
def get_even_numbers(arr):
    return list(filter(lambda x: x%2 == 0, arr)) if arr else []

# Incrementer
def incrementer(nums):
    res = []
    for i in range(len(nums)): 
        new = i+1 + nums[i]
        if len(str(new)) > 1: res.append(int(str(new)[-1]))
        else: res.append(new)
    return res

# Substituting Variables Into Strings: Padded Numbers
def solution(value):
    return "Value is " + "0"*(5 - len(str(value))) + str(value)

# Simple string characters
def solve(s):
    return [len([i for i in s if i.isupper()]),len([i for i in s if i.islower()]),len([i for i in s if i.isdigit()]),len([i for i in s if i in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"])]

# Simple consecutive pairs
def pairs(arr):
    return len([i for i in [arr[i:i+2] for i in range(0, len(arr)-1, 2)] if i[0] - i[1] == -1 or i[0] - i[1] == 1])

# Spacify
def spacify(string):
    return "".join([i+" " for i in string])[:-1]

# Alphabetical Addition
def add_letters(*letters):
    return "abcdefghijklmnopqrstuvwxyz"[(sum(["abcdefghijklmnopqrstuvwxyz".index(i) + 1 for i in letters]) - 1) % 26]

# Alternate case
def alternate_case(s):
    return s.swapcase()

# Automorphic Number (Special Numbers Series #6)
def automorphic(n):
    return "Automorphic" if str(n) == str(n**2)[-len(str(n)):] else "Not!!"

# Strong Number (Special Numbers Series #2)
def strong_num(number):
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    
    return "STRONG!!!!" if sum(factorial(int(i)) for i in str(number)) == number else "Not Strong !!"

# Balanced Number (Special Numbers Series #1 )
def balanced_num(number):
    nums = [int(n) for n in str(number)]
    if len(nums) <= 2:
        return "Balanced"
    elif len(nums) % 2 == 0:
        if sum(nums[:len(nums)//2-1]) == sum(nums[len(nums)//2 + 1:]):
            return "Balanced"
        else:
            return "Not Balanced"
    else:
        if sum(nums[:len(nums)//2]) == sum(nums[len(nums)//2 + 1:]):
            return "Balanced"
        else:
            return "Not Balanced"
        
# Sum of integers in string
def sum_of_integers_in_string(s):
    total_sum = 0
    current_number = 0
    in_number = False

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
            in_number = True
        else:
            if in_number:
                total_sum += current_number
                current_number = 0
                in_number = False
    
    if in_number: total_sum += current_number

    return total_sum

# Disarium Number (Special Numbers Series #3)
def disarium_number(number):
    return "Disarium !!" if sum([int(str(number)[i])**(i+1) for i in range(len(str(number)))]) == number else "Not !!"