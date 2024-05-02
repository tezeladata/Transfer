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

