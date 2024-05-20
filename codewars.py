# Meeting
def meeting(s):
    names = [name.upper().split(":") for name in s.split(";")]
    
    names.sort(key=lambda x: (x[1], x[0]))
    
    return "".join(["({}, {})".format(last, first) for first, last in names])

# Dashatize it
def dashatize(n):
    res = ''.join(['-' + ch + '-' if int(ch) % 2 != 0 else ch for ch in str(abs(n))])
    
    dashatized_str = res.replace('--', '-').strip('-')
    
    return dashatized_str
# or:
def dashatize(n):
    return ''.join(['-' + ch + '-' if int(ch) % 2 != 0 else ch for ch in str(abs(n))]).replace('--', '-').strip('-')

# Lottery Ticket
def bingo(ticket,win):
    all_ord = []
    
    for i in ticket:
        res = []
        for char in i[0]:
            res.append(ord(char))
        all_ord.append([res, i[1]])
        
    final = 0
    
    for i in all_ord:
        for x in i[0]:
            if x == i[1]:
                final += 1
    
    if final >= win:
        return "Winner!"
    return "Loser!"
# or:
def bingo(ticket, win):
    return "Winner!" if sum(any(ord(char) == num for char in chars) for chars, num in ticket) >= win else "Loser!"

# If you can read this...
def to_nato(words: str) -> str:
    d = {
        'A': 'Alfa',  'B': 'Bravo',   'C': 'Charlie',
        'D': 'Delta',  'E': 'Echo',    'F': 'Foxtrot',
        'G': 'Golf',   'H': 'Hotel',   'I': 'India',
        'J': 'Juliett','K': 'Kilo',    'L': 'Lima',
        'M': 'Mike',   'N': 'November','O': 'Oscar',
        'P': 'Papa',   'Q': 'Quebec',  'R': 'Romeo',
        'S': 'Sierra', 'T': 'Tango',   'U': 'Uniform',
        'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }
    
    return " ".join([d[char] if char in d else char for char in words.upper() if char in d or char in ",.!?"])
# or:
from preloaded import NATO

def to_nato(words):
    return " ".join([NATO[char] if char in NATO else char for char in words.upper() if char in NATO or char in ",.!?"])

# Statistics for an Athletic Association
def stat(strg):
    if strg == "":
        return ''
    
    data_list = []
    for runner_time in strg.split(", "):
        times = convert_to_seconds([int(time) for time in runner_time.split("|")])
        data_list.append(times)
    data_list.sort()
    
    
    return f"Range: {stat_range(data_list)} Average: {stat_mean(data_list)} Median: {stat_median(data_list)}"


# Funcs for convertions
def convert_to_seconds(time):
    return time[0] * 3600 + time[1] * 60 + time[2]

def convert_to_hms(seconds):
    hours = int(seconds / 3600 // 1)
    minutes = int((seconds - hours * 3600) / 60 // 1)
    seconds = int(seconds - hours * 3600 - minutes * 60)
    
    return f"{hours:02d}|{minutes:02d}|{seconds:02d}"


# Funcs for range, mean, median
def stat_range(data):
    return convert_to_hms(data[-1] - data[0])

def stat_mean(data):
    return convert_to_hms(sum(data) / len(data))
    
def stat_median(data):
    data_length = len(data)
    middle = data_length // 2
    
    if data_length % 2 == 0:
        return convert_to_hms((data[middle - 1] + data[middle]) / 2)
    return convert_to_hms(data[middle])

# Difference of 2
def twos_difference(list): 
    res = []
    
    list.sort()
    for i in range(len(list)-1):
        for x in range(i+1, len(list)):
            if list[i] +2 == list[x]:
                res.append((list[i], list[x]))
                
    return res
# or:
def twos_difference(lst):
    lst.sort()
    return [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i + 1, len(lst)) if lst[j] - lst[i] == 2]

# Find the Mine!
def mine_location(field):
    res = [[field.index(arr), arr.index(1)] for arr in field if 1 in arr]
    return [res[0][0], res[0][1]]

# Transform To Prime
def minimum_number(numbers):
    return sorted([i for i in range(sum(numbers), sum(numbers) + 35) if is_prime(i)])[0] - sum(numbers)
    
def is_prime(val):
    is_prime = True
    
    for i in range(2, int(val**0.5) + 1):
        if val % i == 0:
            is_prime = False
    
    return is_prime

# Moves in squared strings (II)
def rot(string):
    words = string.replace("\n", " ").split()
    reversed_words = [word[::-1] for word in words]
    return "\n".join(reversed(reversed_words))
    
    return string

def selfie_and_rot(string):
    words = string.replace("\n", " ").split()
    selfie = "\n".join([word + "." * len(word) for word in words])
    
    rotated_words = rot(string).split("\n")
    selfie_rotated = "\n".join(["." * len(word) + word for word in rotated_words])
    
    return selfie + "\n" + selfie_rotated
    
def oper(fct, s):
    return fct(s)
# or:
def rot(string):
    return "\n".join(reversed([word[::-1] for word in string.replace("\n", " ").split()]))

def selfie_and_rot(string):
    return "\n".join([word + "." * len(word) for word in string.replace("\n", " ").split()]) + "\n" + "\n".join(["." * len(word) + word for word in rot(string).split("\n")])
    
def oper(fct, s):
    return fct(s)
# or:
def rot(string):
    return string[::-1]

def selfie_and_rot(string):
    return "\n".join([word + "." * len(word) for word in string.replace("\n", " ").split()]) + "\n" + "\n".join(["." * len(word) + word for word in rot(string).split("\n")])
    
def oper(fct, s):
    return fct(s)

# Hamming Distance
def hamming(a,b):
    return len([1 for i in range(len(a)) if a[i] != b[i]])

# All Star Code Challenge #15
def rotate(s):
    if not s:
        return []
    
    res = []
    length = len(s)
    
    for i in range(length):
        rotated = s[i:] + s[:i]
        res.append(rotated)
        
    return res[1:] + [res[0]]

# How many pages in a book?
def amount_of_pages(summary):
    res = ""
    
    original = 1
    while len(res) != summary:
        res += str(original)
        original += 1
        
    return original - 1

# Paginating a huge book
def page_digits(pages):
    digits = 0
    length = len(str(pages))
    
    for i in range(1, length):
        digits += i * 9 * 10**(i-1)
    
    digits += length * (pages - 10**(length-1) + 1)
    
    return digits