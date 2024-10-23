# Load necessary libraries
library(ggplot2)
library(scales)

# Read data from CSV
data <- read.csv("pollen_levels.csv")

# Create a base plot with ggplot
p <- ggplot(data, aes(x = Time, y = Pollen.Level, group = 1)) +  # Set group = 1 for continuous line
  geom_line(color = 'black', size = 1) +
  
  # Add background color bands for pollen levels
  annotate("rect", xmin = -Inf, xmax = Inf, ymin = 0, ymax = 5, alpha = 0.3, fill = "#05f525") +  # Green for low pollen levels
  annotate("rect", xmin = -Inf, xmax = Inf, ymin = 5, ymax = 10, alpha = 0.3, fill = "#f5ed05") + # Yellow for moderate levels
  annotate("rect", xmin = -Inf, xmax = Inf, ymin = 10, ymax = 20, alpha = 0.3, fill = "#f59505") + # Orange for high levels
  annotate("rect", xmin = -Inf, xmax = Inf, ymin = 20, ymax = 25, alpha = 0.3, fill = "#f50509") + # Red for extreme levels
  
  # Format x-axis to show time every 30 minutes and rotate labels
  scale_x_discrete(labels = format(strptime(data$Time, "%H:%M"), "%H:%M")) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  
  # Add labels and title
  labs(x = "Time", y = "Pollen Level", title = "Pollen Levels Throughout the Day") +
  
  # Add a legend
  theme(legend.position = "top")

# Show the plot
print(p)
