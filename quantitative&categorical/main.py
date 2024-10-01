import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

students = pd.read_csv('students.csv', encoding="ISO-8859-1")

#separate out scores for students who live in urban and rural locations:
scores_urban = students.G3[students.address == "U"]
scores_rural = students.G3[students.address == "R"]

# We can use mean and median to differ these two data
scores_urban_mean = scores_urban.mean()
scores_rural_mean = scores_rural.mean()

print('Mean score - students w/ urban address:')
print(scores_urban_mean)
print('Mean score - students w/ rural address:')
print(scores_rural_mean)


#calculate mean difference:
mean_diff = scores_urban_mean - scores_rural_mean

print('Mean difference:')
print(mean_diff)


#calculate medians for each group:
scores_urban_median = scores_urban.median()
scores_rural_median = scores_rural.median()

print('Median score - students w/ urban address:')
print(scores_urban_median)
print('Median score - students w/ rural address:')
print(scores_rural_median)

#calculate median difference
median_diff = scores_urban_median - scores_rural_median

#print median difference
print('Median difference:')
print(median_diff)



# Visual representation:
sns.boxplot(data=students, y="G3", x="address")
plt.show()
plt.close()


# Another way to explore the relationship between a quantitative and categorical variable in more detail is by inspecting overlapping histograms. In the code below, setting alpha = .5 ensures that the histograms are see-through enough that we can see both of them at once. We have also used normed=True make sure that the y-axis is a density rather than a frequency (note: the newest version of matplotlib renamed this parameter density instead of normed)
plt.hist(scores_urban, color='blue', label='Urban', density=True, alpha=0.5)
plt.hist(scores_rural, color='red', label='Rural', density=True, alpha=0.5)
plt.legend()
plt.show()
plt.close()


# Multiple boxes on x axis:
sns.boxplot(data=students, y="G3", x="Fjob")
plt.show()
plt.close()