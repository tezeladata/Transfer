# Arabian String
def camelize(str_):
    new = ""
    
    for i in str_:
        if i.isalnum(): new += i
        else: new += " "
    
    return "".join([i.capitalize() for i in new.split()])

# Who has the most money?
def most_money(students):
    res = []
    
    for i in students: res.append([i.name, i.fives*5 + i.tens*10 + i.twenties*20])
    res = sorted(res, key=lambda x: x[1])
    
    is_same = True
    for i in range(1, len(res)):
        if res[i][1] != res[i-1][1]: is_same = False
        
    return "all" if len(res) > 1 and is_same else res[-1][0]

# 1/n- Cycle
def cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1
    remainder = 1
    position = 0
    remainders = {}
    while remainder != 0:
        if remainder in remainders:
            return position - remainders[remainder]
        remainders[remainder] = position
        remainder = (remainder * 10) % n
        position += 1
    return 0

# Harshad or Niven numbers
class Harshad:
    @staticmethod
    def is_valid(number):
        return number % sum([int(i) for i in str(number)]) == 0
    
    @staticmethod
    def get_next(number):
        if number == 0: return 1
        for i in range(number+1, int(number + number*2)):
            if i % sum([int(x) for x in str(i)]) == 0: return i
    
    @staticmethod
    def get_series(count, start=1):
        res = []
        
        if start == 1:
            while len(res) != count:
                if start % sum([int(x) for x in str(start)]) == 0: res.append(start)
                start += 1
        else:
            start += 1
            while len(res) != count:
                if start % sum([int(x) for x in str(start)]) == 0: res.append(start)
                start += 1
        
        return res
    
# Valid string
def valid_word(dictionary, word):
    dp = [False] * (len(word) + 1)
    dp[0] = True 
    
    for i in range(1, len(word) + 1):
        for w in dictionary:
            if i >= len(w) and word[i-len(w):i] == w: dp[i] = dp[i] or dp[i - len(w)]
    
    return dp[len(word)]

# Number of anagrams in an array of words
def anagram_counter(words):
    count = 0
    
    for word in words:
        for another in words:
            if another != word and sorted(word) == sorted(another): count += 1
    
    return count/2

# Zero-plentiful Array
def zero_plentiful(arr):
    arr = [i for i in "".join(["1" if i != 0 else "0" for i in arr]).split("1") if i != ""]
    return len(arr) if all(len(i) >= 4 for i in arr) else 0

# Odd-heavy Array
def is_odd_heavy(arr):
    odd_elements = [x for x in arr if x % 2 != 0]
    even_elements = [x for x in arr if x % 2 == 0]
    
    if not odd_elements: return False
    return min(odd_elements) > max(even_elements) if even_elements else True

# Dbftbs Djqifs
def encryptor(key, message):
    alphabet, res = "abcdefghijklmnopqrstuvwxyz", ""
    
    for i in message:
        if i.isalpha():
            if i.isupper(): res += alphabet[(alphabet.index(i.lower())+key) % 26].upper()
            else: res += alphabet[(alphabet.index(i)+key) % 26]
        else: res += i
    
    return res

# Duplicates. Duplicates Everywhere.
def remove_duplicate_ids(obj):
    letters_used = set()
    for key, lst in sorted(obj.items(), key=lambda x: -int(x[0])):
        new_lst = []
        for letter in lst:
            if letter not in letters_used: new_lst.append(letter)
            letters_used.add(letter)
        obj[key] = new_lst
    return obj

# Framed Reflection
def mirror(text):
    text = text.split(" ")
    ln = len(sorted(text, key=len)[-1])
    
    res = ["*"*(ln+4) + "\n"]
    for i in text:
        res.append(f"* {i[::-1]}{' '*(ln - len(i))} *\n")
    res.append("*"*(ln+4))
    return "".join(res)

# Simple string indices
def solve(st, idx):
    if st[idx] != '(': return -1

    stack = 0
    for i in range(idx, len(st)):
        if st[i] == '(': stack += 1
        elif st[i] == ')': stack -= 1

        if stack == 0: return i

    return -1

# Simple prime streaming
def solve(a, b):
    seq, start = "", 2
    while len(seq) < a + b:
        if is_prime(start): 
            seq += str(start)
            start += 1
        else: start += 1
    
    return seq[a:a+b]
    
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**.5)+1):
        if num%i == 0: return False
    return True

# Life without primes
def solve(n):
    res, start = [], 1
    
    while len(res) <= n:
        if not is_prime(start) and all(not is_prime(int(digit)) for digit in str(start)):
            res.append(start)
        start += 1
    
    return res[n]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Upside down numbers
def solve(a, b):
    nums = {"0": "0", "1": "1", "6": "9", "8": "8", "9":"6"}
    tot = 0
    for i in range(a,b):
        i = str(i)
        m = "".join([nums[x] for x in i[::-1] if x in nums])
        if i == m:
            tot +=1
    return tot

# Fibonacci Reloaded
def fib(n):
    res = [0, 1]
    while len(res) < n: res.append(res[-1]+res[-2])
    return res[-1] if n != 1 else 0

# Numbers of Letters of Numbers
def numbers_of_letters(n):
    digit_to_word, res = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }, []

    while True:
        word_representation = "".join(digit_to_word[int(digit)] for digit in str(n))
        res.append(word_representation)
        
        length_of_word_representation = len(word_representation)
        if word_representation == "four": break
        n = length_of_word_representation
    
    return res

# Rotate Array
def rotate(data, n):
    if not data: return []

    if n >= 0:
        for _ in range(n): data = [data[-1]] + data[:-1]
    else:
        for _ in range(n*-1): data = data[1:] + [data[0]]
    
    return data

# Organise duplicate numbers in list
def group(arr):
    duplicates = {}
    for num in arr:
        if num not in duplicates: duplicates[num] = []
        duplicates[num].append(num)
    return list(duplicates.values())

# Circularly Sorted Array
def circularly_sorted(arr):
    if not arr: return True
    
    n = len(arr)
    count = 0
    
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]: count += 1
    
    return count <= 1
