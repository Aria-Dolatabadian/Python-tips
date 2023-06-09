# Prompt the user to enter the volume of ethanol and the total volume of the solution
volume_ethanol = float(input("Enter the volume of ethanol (in mL): "))
volume_solution = float(input("Enter the total volume of the solution (in mL): "))

# Calculate the volume percentage (v/v%) of ethanol
percentage_v_v = (volume_ethanol / volume_solution) * 100

# Print the result
print(f"The volume percentage (v/v%) of ethanol in the solution is: {percentage_v_v:.2f}%")
