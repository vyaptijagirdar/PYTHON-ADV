
import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    'Name': ['Aarav', 'Diya', 'Rahul', 'Priya', 'Neha', 'Karan', 'Riya', 'Aman'],
    'Age': [22, 25, 28, 24, 30, 27, 23, 35],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'IT'],
    'Salary': [30000, 35000, 40000, 32000, 38000, 45000, 33000, 150000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Calculate salary statistics
print("\nMean:", df['Salary'].mean())
print("Median:", df['Salary'].median())
print("Standard Deviation:", df['Salary'].std())

# Calculate IQR
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Remove outliers
df = df[(df['Salary'] >= lower) & (df['Salary'] <= upper)]

print("\nDataFrame after removing outliers:")
print(df)

# Plot boxplot
plt.boxplot(df['Salary'])
plt.title("Salary Boxplot")
plt.ylabel("Salary")
plt.show()

# Plot histogram
plt.hist(df['Salary'], bins=5, edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
