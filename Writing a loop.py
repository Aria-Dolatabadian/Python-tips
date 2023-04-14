Pathogens = ["Leptosphaeria maculans",
             "Verticillium longisporum",
             "Sclerotinia sclerotiorum",
             "Erwinia carotovora"]

print(Pathogens[0] + " is a fungus")
print(Pathogens[1] + " is a fungus")
print(Pathogens[2] + " is a fungus")
print(Pathogens[3] + " is a bacterium")


#or

DNA = ["GCTACAGACGACT", "ACTACAGACG", "CTTCCA"]
for seq in DNA:
    name_length = len(seq)
    first_letter = seq[0]
    print((seq + " starts with " + first_letter),("and has " + str(name_length) + " bases"))
