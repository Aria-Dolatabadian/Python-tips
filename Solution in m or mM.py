# Ask for user inputs
mol_weight = float(input("Enter the molecular weight: "))
concentration_unit = input("Enter the concentration unit (M or mM): ")
concentration_value = float(input("Enter the concentration value: "))
volume = float(input("Enter the volume in liters: "))

# Convert concentration to Molar if it's in mM
if concentration_unit.lower() == "m":
    concentration = concentration_value
elif concentration_unit.lower() == "mm":
    concentration = concentration_value / 1000
else:
    print("Invalid concentration unit specified. Please use M or mM.")
    exit()
# Calculate the amount of substance needed in grams
amount = concentration * mol_weight * volume

# Print the amount of substance needed
print(f"Amount of substance needed: {amount:.2f} grams")
