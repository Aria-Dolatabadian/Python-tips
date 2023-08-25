# Create a dictionary where values are lists
Genes = {
    'Rlm1': ['ACGAVCACTAGACGACATAGACGAT', 'CGACAGCAGATAGACAC', 'CGACGACGACATATCA'],
    'Rlm2': ['CGACGACGATACATATA', 'CACACAGCAGTATACA', 'CGACACACGATATAA'],
    'Rlm6': ['CGACGACATTACTATATATATA', 'CAGCAGCAGCAGACCA']
}

# Access and print values in the dictionary
print(Genes.get('Rlm1')[2])
