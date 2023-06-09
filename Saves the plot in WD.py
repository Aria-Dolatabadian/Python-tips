import matplotlib.pyplot as plt

# Define the treatments and their corresponding data
treatments = ['Treatment A', 'Treatment B', 'Treatment C', 'Treatment D']
data = [10,12,25,21]

# Plot the bar chart
plt.bar(treatments, data)
plt.xlabel('Treatments')
plt.ylabel('Data')
plt.title('Bar Chart')
plt.savefig('chart.jpg', format='jpg')
plt.show()
