import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# get dataset
dataset = pd.read_csv('world_tourism_economy_data.csv')

# year == 2000 and income is not NaN
filtered_data = dataset.loc[(dataset["year"] == 2000) & (pd.notna(dataset["tourism_receipts"]))]

# Income for the year 2000
income_2000 = filtered_data["tourism_receipts"].tolist()

# Related countries
countries_2000 = filtered_data["country"].tolist()

# filter countries
def filter_countries(countries, incomes):
    # Combine countries and incomes, then sort by income
    combined = list(zip(countries, incomes))
    combined_sorted = sorted(combined, key=lambda x: x[1])

    # Median calculation
    incomes_sorted = [i[1] for i in combined_sorted]
    middle = np.median(incomes_sorted)

    # Calculate left and right boundaries
    left = middle / 2
    right = middle * 1.5

    # Dividing incomes into four groups
    lower = [i[0] for i in combined_sorted if i[1] < left]
    middle_left = [i[0] for i in combined_sorted if left <= i[1] < middle]
    middle_right = [i[0] for i in combined_sorted if middle <= i[1] < right]
    upper = [i[0] for i in combined_sorted if i[1] >= right]

    res = {
        "Lower Income": len(lower),
        "Middle left Income": len(middle_left),
        "Middle right Income": len(middle_right),
        "Upper Income": len(upper)
    }

    return res

# filtering result
filter_res = filter_countries(countries_2000, income_2000)

# visualization function
def plot_pie_chart(fortitle, labels, sizes):
    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=["#18392b", "#14452f", "#0a5c36", "#1d2e28"])
    plt.title(fortitle, fontsize=16)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# Call the function with updated parameters
plot_pie_chart("Proportion of countries in four groups by their tourist income", list(filter_res.keys()), list(filter_res.values()))