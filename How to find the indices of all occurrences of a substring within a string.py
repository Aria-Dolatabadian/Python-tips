DNA = "UTCATCGATACAUTCTGACATGACATATAUTCTAGACATGAUTC"
substring = "UTC"
import re
matches = re.finditer(substring, DNA)
matches_positions = [match.start() for match in matches]

print(matches_positions)
