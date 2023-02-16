DNA = "UTCATCGATACAUTCTGACATGACATATAUTCTAGACATGAUTC"
Gene = "UTC"

print("The DNA seq (string) is: " + DNA)
print("The Gene (substring) to find is: " + Gene)

res = [i for i in range(len(DNA)) if DNA.startswith(Gene, i)]
print("The start indices of the Gene are: " + str(res))
