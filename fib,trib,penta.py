import matplotlib.pyplot as plt

user_num = int(input("Enter number: "))

def fibonacci(n):
    res = [0, 1]
    while len(res) < n:
        res.append(res[-2] + res[-1])
    return res

x1 = fibonacci(n=user_num)
y1 = range(len(x1))

def tribonacci(n):
    res = [0, 1, 1]
    while len(res) < n:
        res.append(sum(res[-3:]))
    return res

x2 = tribonacci(n=user_num)
y2 = range(len(x2))

def pentabonacci(n):
    res = [0, 0, 1, 1, 2]
    while len(res) < n:
        res.append(sum(res[-5:]))
    return res

x3 = pentabonacci(n=user_num)
y3 = range(len(x3))

plt.plot(y1, x1, label="Fibonacci Sequence")
plt.scatter(y1, x1, color='red')
plt.plot(y2, x2, label="Tribonacci Sequence")
plt.scatter(y2, x2, color='red')
plt.plot(y3, x3, label="Pentabonacci Sequence")
plt.scatter(y3, x3, color='red')
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.legend()
plt.show()