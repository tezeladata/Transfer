import matplotlib.pyplot as plt

def collatz(n):
    res = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        res.append(n)
    return res

n = int(input("Enter a number: "))
sequence = collatz(n)
x = list(range(len(sequence)))
plt.plot(x, sequence)
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()