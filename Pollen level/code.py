import pandas as pd
import matplotlib.pyplot as plt
# Read data from CSV
data = pd.read_csv("pollen_levels.csv")
# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
# Plot line chart
ax.plot(data["Time"], data["Pollen Level"], label="Pollen Level", color='black', lw=2)
times = pd.date_range(start="08:00", end="20:00", freq="30T").time
# Add background colour bands based on y-axis pollen levels
ax.axhspan(0, 5, color='#05f525', alpha=0.3, label='Low (0-5)')      # Green for low pollen levels
ax.axhspan(5, 10, color='#f5ed05', alpha=0.3, label='Moderate (5-10)')  # Yellow for moderate levels
ax.axhspan(10, 20, color='#f59505', alpha=0.3, label='High (10-20)')    # Orange for high levels
ax.axhspan(20, 25, color='#f50509', alpha=0.3, label='Extreme (>20)')      # Red for extreme levels
# Format x-axis to show every 30 minutes and rotate for better readability
ax.set_xticks(data["Time"])  # Show all time labels (every 30 minutes)
ax.set_xticklabels([t.strftime("%H:%M") for t in times], rotation=45)  # Rotate for clarity
# Labels and title
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("Pollen level", fontsize=12)
ax.set_title("Pollen levels throughout the day", fontsize=14)
# Show legend and plot
plt.tight_layout()
plt.legend()
plt.show()
