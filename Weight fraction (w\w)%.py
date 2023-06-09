# Prompt the user to enter the mass of solute and the mass of the solution
mass_solute = float(input("Enter the mass of solute (in grams): "))
mass_solution = float(input("Enter the mass of the solution (in grams): "))

# Calculate the weight percentage (w/w) of solute
percentage_w_w = (mass_solute / mass_solution) * 100

# Print the result
print(f"The weight percentage (w/w) of solute in the solution is: {percentage_w_w:.2f}%")
