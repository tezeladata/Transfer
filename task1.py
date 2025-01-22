def task1(a, b, c):
    if b > a and ((b%c == 0 or a%c == 0) == False): return (b-a) // c
    else: return (b-a) // c + 1

print(task1(3, 20, 3))
print(task1(3, 21, 3))
print(task1(4, 20, 3))
print(task1(4, 21, 3))