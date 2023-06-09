# Ask for quantities per reaction
fprimer_volume = float(input("Enter the volume of F-Primer per reaction (in uL): "))
rprimer_volume = float(input("Enter the volume of R-Primer per reaction (in uL): "))
dna_volume = float(input("Enter the volume of DNA per reaction (in uL): "))
mastermix_volume = float(input("Enter the volume of Mastermix per reaction (in uL): "))
water_volume = float(input("Enter the volume of Water per reaction (in uL): "))
reaction_volume =fprimer_volume + rprimer_volume +dna_volume+mastermix_volume+water_volume
print(f"Reaction volume:{reaction_volume} ul")
# Define the number of reactions
num_reactions = float(input("Enter the number of reactions: "))
# Calculate the total volumes for each component
total_fprimer_volume = fprimer_volume * num_reactions
total_rprimer_volume = rprimer_volume * num_reactions
total_dna_volume = dna_volume * num_reactions
total_mastermix_volume = mastermix_volume * num_reactions
total_water_volume = water_volume * num_reactions
# Print the PCR mix
print(f"PCR Mix for {num_reactions} reactions:")
print(f"F-Primer: {total_fprimer_volume} uL")
print(f"R-Primer: {total_rprimer_volume} uL")
print(f"Mastermix: {total_mastermix_volume} uL")
print(f"Water: {total_water_volume} uL")
print(f"DNA: {dna_volume} ul for each reaction")
