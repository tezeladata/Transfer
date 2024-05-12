# Binary to Text (ASCII) Conversion
import math
def binary_to_string(binary):
    if binary == "":
        return ""
    else:
        result = []
        listn = []
        string = ""
        for i in binary:
            string += str(i)
            if len(string) % 8 == 0:
                listn.append(string)
                string = ''
        for i in listn:
            dec = binaryToDecimal(i)
            dec = chr(dec)
            result.append(dec)
        return "".join(result)

def binaryToDecimal(n):
    dec_num = 0
    power = 0
    while (int(n) > 0):
        if (int(n) % 10 == 1):
            dec_num += (1 << power)
        power = power + 1
        n = math.floor(int(n) / 10)

    return dec_num

def binary_to_string(binary):
    if not binary:
        return ''

    listn = []
    string = ""
    for i in binary:
        string += str(i)
        if len(string) % 8 == 0:
            listn.append(string)
            string = ''
    return ''.join([chr(int(binary_str, 2)) for binary_str in listn])

# Find The Parity Outlier
def find_outlier(integers):
    even_count = 0
    for i in range(3):
        if integers[i]%2==0:
            even_count += 1
            
    if even_count == 3 or even_count == 2:
        return [i for i in integers if i%2!=0][0]
    else:
        return [i for i in integers if i%2==0][0]
    
# Playing with digits
def dig_pow(n, p):
    sum = 0
    starting_power = p
    
    for i in range(len(str(n))):
        sum += int(str(n)[i]) ** starting_power
        starting_power += 1
        
    if sum%n == 0:
        return sum / n
    return -1

# Decode the Morse code
def decode_morse(morse_code):
    morse_code_dictionary = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', '"': '.-..-.', 
        ':': '---...', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', 
        '=': '-...-', '+': '.-.-.', '@': '.--.-.', " ": " ", "$": "...-..-", "SOS": "...---...", ";": "-.-.-.", "_": "..--.-"
    }
    
    morse_code = morse_code.strip().split("   ")  # Split words
    
    res_list = []
    for word in morse_code:
        chars = word.split(" ")
        decoded_word = ""
        for char in chars:
            if char in morse_code_dictionary.values():
                decoded_word += list(morse_code_dictionary.keys())[list(morse_code_dictionary.values()).index(char)]
        res_list.append(decoded_word)
                
    return " ".join(res_list)

# Two Sum
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for x in range(i+1, len(numbers)):
            if numbers[i] + numbers[x] == target:
                res = (i, x)
    return res

# Character with longest consecutive repetition
def longest_repetition(s):
    if not s:
        return ("", 0)

    max_char = s[0]
    max_count = 1
    current_char = s[0]
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                max_char = current_char
        else:
            current_char = s[i]
            current_count = 1

    return (max_char, max_count)

# Remove the parentheses
def remove_parentheses(s):
  result = ''
  count = 0
  for char in s:
    if char == '(':
      count += 1
    if char == ')':
      count -= 1
    if not count and not char in '()':
      result += char

  return result

# Clocky Mc Clock-Face
from math import floor

def what_time_is_it(angle):
    mins = floor(angle * 2)
    h = mins // 60
    m = mins % 60
    if h == 0:
        h = "12"
    if int(h) < 10:
        h = "0" + str(int(h))
    if m < 10:
        m = "0" + str(m)
    return str(h) + ":" + str(m)

# Format words into a sentence
def format_words(words):
    if words == [] or words is None or words == [""]:
        return ""
    
    words = [i for i in words if i.isalnum()]
    
    if len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return " and ".join(words)
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]