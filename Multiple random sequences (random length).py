from random import choice
from random import randint
number_of_sequences=5
lengths=[randint(5,10)for i in range (number_of_sequences)]
print(lengths)
def generate_sequence(length):
    bases = ['A', 'T', 'C', 'G']
    sequence = [choice(bases) for i in range(length)]
    return sequence
sequences=[generate_sequence(length) for length in lengths]
print(sequences)
