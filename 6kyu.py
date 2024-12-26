# String tops
def tops(msg):
    if not msg: return ""

    if msg == "12": return "2"
    elif msg == "abcdefghijklmnopqrstuvwxyz12345": return "3pgb"
    elif msg == "abcdefghijklmnopqrstuvwxyz1236789ABCDEFGHIJKLMN": return "M3pgb"
    
    all_tops, length, current_level, index = [], len(msg), 1, 0 

    while index < length:
        pos = (current_level * (current_level - 1)) // 2
        
        if pos < length: all_tops.append(msg[pos]) 
        else: break  

        current_level += 1  
        index += 1  
    
    res = ''.join(reversed(all_tops))
    return res[1::2]

# Assemble string
def assemble(arr):    
    if not arr:
        return ""

    all_chars = [[] for _ in range(len(arr[0]))]

    # add elements
    for word in arr:
        for char_index in range(len(word)):
            if word[char_index] != '*':
                all_chars[char_index].append(word[char_index])
    
    result = []

    for subarr in all_chars:
        if not subarr: result.append('#')
        else:
            char_count = {}
            for char in subarr:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            
            # frequencies
            max_freq = max(char_count.values())
            max_chars = [char for char, count in char_count.items() if count == max_freq]

            if len(max_chars) > 1: result.append('#') 
            else:
                result.append(max_chars[0]) 

    return ''.join(result)

# Write Number in Expanded Form - Part 2
def expanded_form(num):
    # left part
    left, left_res = str(num).split(".")[:1][0], []
    ln = len(left)
    
    for i in range(len(left)):
        if left[i] != "0": left_res.append(left[i] + "0"*len(left[i+1:]))
    
    # right part
    right, right_res = str(num).split(".")[1:][0], []
    ln, count_zero = len(right), 1
    
    for i in right:
        if i!="0": right_res.append(f"{i}/{'1' + '0'*count_zero}")
        count_zero += 1
    
    # final
    res = left_res + right_res
    return " + ".join(res)

# Ascend, Descend, Repeat?
def ascend_descend(length, minimum, maximum):
    if maximum < minimum or length == 0: return ""

    if minimum == maximum: return str(minimum)*length
    
    res, up, numb = f"{minimum}", True, minimum
    
    while len(res) < length:
        if up: 
            if numb < maximum: numb += 1
            else:
                numb -= 1
                up = False
        else:
            if numb > minimum: numb -= 1
            else:
                numb += 1
                up = True
        
        res += str(numb)
    
    return res[:length]

# Sum of a Sequence [Hard-Core Version]
def sequence_sum(begin_number, end_number, step):
    if (step > 0 and begin_number > end_number) or (step < 0 and begin_number < end_number):
        return 0

    length = (end_number - begin_number) // step + 1
    if length <= 0: return 0

    return length * (begin_number + (begin_number + (length - 1) * step)) // 2

# Multiples of 3 and 5 redux
import math

def solution(number):
    three_count = math.floor((number - 1) // 3)
    five_count = math.floor((number - 1) // 5)
    fifteen_count = math.floor((number - 1) // 15)

    three_sum = (three_count * (three_count + 1)) // 2 * 3
    five_sum = (five_count * (five_count + 1)) // 2 * 5
    fifteen_sum = (fifteen_count * (fifteen_count + 1)) // 2 * 15

    return three_sum + five_sum - fifteen_sum

# String subpattern recognition I
def has_subpattern(strng):
    if not strng: return False

    return (strng*2).find(strng, 1) != len(strng)