import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# Load dataset
dataset = pd.read_csv('world_tourism_economy_data.csv')

# tourism_receipts is not NaN
filtered_data = dataset.loc[pd.notna(dataset["tourism_receipts"])]

# yearly income dict
def create_yearly_income_dict(data):
    yearly_income = {}
    for year in range(1999, 2020):  # from 1999 to 2019
        year_data = data.loc[data["year"] == year, "tourism_receipts"].tolist()
        yearly_income[year] = year_data
    return yearly_income

# yearly mean dict
def create_yearly_means_dict(data):
    for key, value in data.items():
        data[key] = np.mean(value).round(2) if value else 0
    return data

# Generate yearly data
yearly_income_dict = create_yearly_income_dict(filtered_data)
yearly_means_dict = create_yearly_means_dict(yearly_income_dict)

# Plot the bar chart
def plot_bar_chart(data):
    years = list(data.keys())
    means = list(data.values())
    
    plt.figure(figsize=(10, 8))
    plt.barh(years, means, color="darkgreen", edgecolor="black") 
    
    for i, v in enumerate(means):
        plt.text(v + 0.01, years[i], str(v), color="white", va='center', fontsize=10)

    plt.xlabel("Average Tourism income", fontsize=14)
    plt.ylabel("Year", fontsize=14)
    plt.title("Average Tourism Receipts per Year (1999-2019)", fontsize=16)
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

# Call the plot function
plot_bar_chart(yearly_means_dict)


# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np 

# # Load dataset
# dataset = pd.read_csv('world_tourism_economy_data.csv')

# # tourism_receipts is not NaN
# filtered_data = dataset.loc[pd.notna(dataset["tourism_receipts"])]

# # yearly income dict
# def create_yearly_income_dict(data):
#     yearly_income = {}
#     for year in range(1999, 2020):  # from 1999 to 2019
#         year_data = data.loc[data["year"] == year, "tourism_receipts"].tolist()
#         yearly_income[year] = year_data
#     return yearly_income

# # yearly mean dict
# def create_yearly_means_dict(data):
#     for key, value in data.items():
#         data[key] = np.mean(value).round(2) if value else 0
#     return data

# # Generate yearly data
# yearly_income_dict = create_yearly_income_dict(filtered_data)
# yearly_means_dict = create_yearly_means_dict(yearly_income_dict)

# # Plot the bar chart
# def plot_bar_chart(data):
#     years = list(data.keys())
#     means = list(data.values())
    
#     plt.figure(figsize=(12, 6))
#     plt.bar(years, means, color="darkgreen", edgecolor="black") 
    


#     plt.ylabel("Average Tourism income", fontsize=14)
#     plt.xlabel("Year", fontsize=14)
#     plt.title("Average Tourism Receipts per Year (1999-2019)", fontsize=16)
#     plt.grid(axis="y", linestyle="--", alpha=0.7)
#     plt.tight_layout()
#     plt.show()

# # Call the plot function
# plot_bar_chart(yearly_means_dict)