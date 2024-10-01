import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv("housing_sample.csv")

# Scatter plot - quantitative variable plus quantitative variable
plt.scatter(x = df1.beds, y = df1.sqfeet)
plt.xlabel("Beds count")
plt.ylabel("Square feet")
plt.show()
plt.close()


# Covariance can range from negative infinity to positive infinity. A positive covariance indicates that a larger value of one variable is associated with a larger value of the other. A negative covariance indicates a larger value of one variable is associated with a smaller value of the other. A covariance of 0 indicates no linear relationship.
cov1 = np.cov(df1.beds, df1.sqfeet)
print(cov1)


# Stopped at correlation