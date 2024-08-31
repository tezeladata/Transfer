# Play with two Strings
def work_on_strings(a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    switch_a = []
    switch_b = []

    for letter in alphabet:
        switch_a.append(b.lower().count(letter) % 2)
        switch_b.append(a.lower().count(letter) % 2)

    concat = a + b
    output = ''

    for i, letter in enumerate(concat):
        if i < len(a):
            if switch_a[alphabet.index(letter.lower())] == 1: letter = letter.swapcase()
        else:
            if switch_b[alphabet.index(letter.lower())] == 1: letter = letter.swapcase()

        output += letter

    return output

# Closest and Smallest
def closest(strng):
    if not strng:
        return []

    numbers = strng.split()
    weights = [[sum(int(digit) for digit in num), idx, int(num)] for idx, num in enumerate(numbers)]
    weights.sort() 

    min_diff = float('inf')
    result = []

    for i in range(len(weights) - 1):
        diff = abs(weights[i][0] - weights[i + 1][0])
        if diff < min_diff:
            min_diff = diff
            result = [weights[i], weights[i + 1]]

    return result

# Calculate Variance
def variance(numbers): 
    return sum([(i-sum(numbers) / len(numbers)) ** 2 for i in numbers]) / len(numbers)

# flatten()
def list_sorter(lst):
    output = []
    for elem in lst:  
        if type(elem) == list:
            output += list_sorter(elem)
        else:
            output.append(elem)
    return output

def flatten(*args):
    output = []
    for arg in [*args]:
        if type(arg) == list: output += list_sorter(arg)
        else: output.append(arg)
    return output

# Calculating with Functions
def zero(func=None):  return 0 if func is None else func(0)
def one(func=None): return 1 if func is None else func(1)
def two(func=None): return 2 if func is None else func(2)
def three(func=None): return 3 if func is None else func(3)
def four(func=None): return 4 if func is None else func(4)
def five(func=None): return 5 if func is None else func(5)
def six(func=None): return 6 if func is None else func(6)
def seven(func=None): return 7 if func is None else func(7)
def eight(func=None): return 8 if func is None else func(8)
def nine(func=None): return 9 if func is None else func(9)
def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y

# Write out numbers
def number2words(n):
    def one_digit(n):
        switcher = {
            0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
            5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
        }
        return switcher.get(n, "")

    def two_digits(n):
        if 10 <= n < 20:
            switcher = {
                10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
                18: "eighteen", 19: "nineteen"
            }
            return switcher.get(n, "")
        else:
            switcher = {
                20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
                60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
            }
            return switcher.get(n - n % 10, "") + ("" if n % 10 == 0 else "-" + one_digit(n % 10))

    def three_digits(n):
        if n == 0: return ""
        elif n < 100: return two_digits(n)
        else: return one_digit(n // 100) + " hundred" + ("" if n % 100 == 0 else " " + two_digits(n % 100))

    def number_to_words(n):
        if n == 0: return "zero"
        elif n < 1000: return three_digits(n)
        elif n < 1000000: return three_digits(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + three_digits(n % 1000))

    res = number_to_words(n).split(" ")
    res = [i[1:] if i[0] == "-" else i for i in res]
    return " ".join(res)

# 