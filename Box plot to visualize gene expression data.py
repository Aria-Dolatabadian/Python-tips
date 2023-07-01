import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Gene expression data
genes = ['Gene1', 'Gene2', 'Gene3']
expression_levels = [[2.5, 3.1, 2.8, 4.2, 3.9, 4.5],
                     [1.8, 2.4, 2.1, 3.2, 3.6, 4.1],
                     [2.3, 2.9, 2.6, 3.5, 4.0, 4.4]]

# Create a dataframe from the data
data = pd.DataFrame({'Gene': np.repeat(genes, len(expression_levels[0])),
                     'Expression': np.concatenate(expression_levels)})

# Create a box plot
sns.boxplot(x='Gene', y='Expression', data=data)

# Set labels and title
plt.xlabel('Gene')
plt.ylabel('Expression Level')
plt.title('Gene Expression Box Plot')

# Display the plot
plt.show()
