import re
scientific_name = "Brassica napus Westar"
m = re.search("(.+) (.+) (.+)", scientific_name)
if m:
    genus = m.group(1)
    species = m.group(2)
    variety = m.group(3)
    print("Genus is " + genus + ", species is " + species + ", variety is " + variety)
