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


