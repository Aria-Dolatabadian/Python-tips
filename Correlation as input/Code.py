import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import scipy.stats as stats


# Read data from CSV
data = pd.read_csv("data.csv")
# Display the variable names in the CSV file
print("Variable Names in the CSV file:")
print(data.columns)
# Prompt the user to enter the variable names
variable1_name = input("Enter the name of Variable 1: ")
variable2_name = input("Enter the name of Variable 2: ")
# Select the variables of interest
x = data[variable1_name]
y = data[variable2_name]
# Perform linear regression
model = LinearRegression()
model.fit(x.values.reshape(-1, 1), y)
y_pred = model.predict(x.values.reshape(-1, 1))
# Calculate R-squared value
r2 = r2_score(y, y_pred)
# Print the equation of the regression line and R-squared value
equation = "y = {:.2f}x + {:.2f}".format(model.coef_[0], model.intercept_)
print("Equation: ", equation)
print("R-squared: {:.4f}".format(r2))
# Calculate the Pearson correlation coefficient and p-value
corr, p_value = stats.pearsonr(x, y)
# Print the correlation coefficient and p-value
print("Correlation Coefficient:", corr)
print("P-value:", p_value)
# Create scatter plot with regression line
sns.regplot(x=x, y=y, ci=None, line_kws={'color': 'red'})
plt.xlabel(variable1_name)
plt.ylabel(variable2_name)
plt.title("Scatter plot with regression line")
plt.show()

