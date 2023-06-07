import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV file
filename = 'data.csv'
df = pd.read_csv(filename)

# Display column names and numbers
columns = df.columns.tolist()
for i, col in enumerate(columns):
    print(f"{i+1}. {col}")

# Prompt user for column selection
col1 = input("Enter column name or number for X-axis: ")
col2 = input("Enter column name or number for Y-axis: ")

# Convert column input to column names
if col1.isdigit():
    col1 = columns[int(col1) - 1]
if col2.isdigit():
    col2 = columns[int(col2) - 1]

# Perform Pearson correlation
corr_coef = df[[col1, col2]].corr().iloc[0, 1]

# Visualize scatter plot with regression line and equation
sns.lmplot(x=col1, y=col2, data=df)
plt.title(f"Scatter Plot: {col1} vs {col2}\nCorrelation Coefficient: {corr_coef:.2f}")
plt.show()
