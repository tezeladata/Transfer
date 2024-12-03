import matplotlib.pyplot as plt
import numpy as np

n = int(input("Enter number of rows: "))

def generate_pascals_triangle():
    print("Hello, this is Pascal's Triangle")
    a = []

    for i in range(n):
        a.append([]) 
        a[i].append(1)  
        for j in range(1, i):
            a[i].append(a[i-1][j-1] + a[i-1][j])
        if n != 0: 
            a[i].append(1)
    
    return a

res = generate_pascals_triangle()

for i in range(len(res)):
    plt.plot([sum(res[i])], [i], marker='o', color='green', label="Row sums" if i == 0 else "")  

x = range(n**4)
y = np.log2(x)  
plt.plot(x, y, label=r'$y = \log_2(x)$', color='blue')


plt.legend()
plt.show()