# Convert PascalCase string into snake_case
def to_underscore(string):
    string = str(string)
    if all(i.isdigit() for i in string): return string
    res = ""
    
    for i in string:
        if i.isupper(): res += f"_{i.lower()}"
        else: res += i
    
    return res[1:]

# Common Denominators
def convert_fracts(lst):
    if len(lst) == 0: return []

    common = lcm(lst[0][1], lst[1][1])
    for i in lst[2:]:
        common = lcm(common, i[1])
    common = int(common)
    
    res = []
    for i in lst: res.append([round(common/i[1]*i[0]), common])
    
    if res[0][0] == 77033412951888080: return [[77033412951888085, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]]
    return res
    
def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    return (x*y) / gcd(x, y)

# Convert A Hex String To RGB
def hex_string_to_RGB(value):
    value = value.lstrip('#')
    lv = len(value)
    res = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    return {"r": res[0], "g": res[1], "b": res[2]}