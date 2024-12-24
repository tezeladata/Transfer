import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load dataset
dataset = pd.read_csv('world_tourism_economy_data.csv')

# tourism_receipts and gdp are not NaN and the year is 2019
filtered_data = dataset.loc[
    pd.notna(dataset["tourism_receipts"]) & 
    pd.notna(dataset["gdp"]) & 
    (dataset["year"] == 2019)
]

# Get country GDP
gdp = [[row["gdp"], row["country"]] for _, row in filtered_data.head(50).iterrows() if row['gdp'] < 10**11]
selected_countries = [i[1] for i in gdp]

# Get tourism incomes 
incomes = [row["tourism_receipts"] for _, row in filtered_data.head(50).iterrows() if row["country"] in selected_countries]

# update
gdp = [i[0] for i in gdp]

# np arrays
X = np.array(gdp).reshape(-1, 1)  
y = np.array(incomes)

# linear regression
model = LinearRegression()
model.fit(X, y)

# Get the regression line
regression_line = model.predict(X)

# data 
plt.figure(figsize=(10, 6))
# Scatter 
plt.scatter(gdp, incomes, color='darkgreen', label='Data Points')
# regression line
plt.plot(gdp, regression_line, color='black', label='Linear Regression Line')
# Labeling
plt.title('Tourism income and GDP (2019)', fontsize=16)
plt.xlabel('GDP', fontsize=14)
plt.ylabel('Tourism income', fontsize=14)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()