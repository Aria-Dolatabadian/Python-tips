import pubchempy as pcp
chemical_name = input("Enter chemical name:")

try:
    compound = pcp.get_compounds(chemical_name,'name')[0]
    print(f"IUPAC Name: {compound.iupac_name}")
    print(f"Common Name: {compound.synonyms[0]}")
    print(f"Molecular Weight: {compound.molecular_weight}")
    print(f"Formula: {compound.molecular_formula}")
    print(f"Canonical SMILES: {compound.canonical_smiles}")
    print(f"Isotope atom count: {compound.isotope_atom_count}")

except IndexError:
    print (f"No Information Found for {chemical_name}.")

