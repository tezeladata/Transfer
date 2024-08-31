# Sum Strings as Numbers - 4kyu
def sum_strings(x, y):
    if x == '0' and y == '0': return '0'
    
    res_list = []
    carry = 0
    i, j = len(x) - 1, len(y) - 1
    
    while i >= 0 or j >= 0 or carry:
        digit_x = int(x[i]) if i >= 0 else 0
        digit_y = int(y[j]) if j >= 0 else 0

        total = digit_x + digit_y + carry
        carry = total // 10
        res_list.append(str(total % 10))
        
        i -= 1
        j -= 1
    
    res = ''.join(res_list[::-1]).lstrip("0")
    return res if res != "" else "0"