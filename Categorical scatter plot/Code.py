import matplotlib.pyplot as plt
import pandas as pd

# Read data from the CSV file
file_path = 'Primer 4.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Create a color map for unique sample names
colors = {'S': 'b', 'Bn': 'g', 'Rs': 'r', 'NC': 'c'}

# Create a scatter plot with different colors for each sample
for sample, group in df.groupby('Sample'):
    plt.scatter(group['X'], group['Y'], label=sample, color=colors[sample])

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(title='Sample Names')

# Show the plot
plt.title('Scatter plot of KASP assays for 16 introgressed B. napus (S), 3 B. napus (Bn), 3 radish (Rs) and negative control (NC).')
plt.show()
