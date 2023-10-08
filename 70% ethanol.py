
# Prompt the user for the initial percentage of ethanol
initial_percentage = float(input("Enter the initial percentage of ethanol: "))

# Prompt the user for the required volume in milliliters
required_volume_ml = float(input("Enter the required volume in milliliters: "))

# Prompt the user for the desired percentage of the final solution
desired_percentage = float(input("Enter the desired percentage of the final solution: "))

# Calculate the volume of ethanol needed in milliliters
ethanol_volume_ml = (required_volume_ml * desired_percentage) / initial_percentage

# Calculate the volume of water needed in milliliters
water_volume_ml = required_volume_ml - ethanol_volume_ml


# Print the volumes of ethanol and water needed
print(f"Volume of ethanol needed: {ethanol_volume_ml:.2f} mL")
print(f"Volume of water needed: {water_volume_ml:.2f} mL")
