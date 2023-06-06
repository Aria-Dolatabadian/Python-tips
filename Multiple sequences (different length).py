from random import choice
def generate_sequence(length):
    bases=['A','T','C','G']
    sequence=[choice(bases) for i in range(length)]
    sequence=''.join(sequence)
    return sequence
lengths=[6,5,4,3,2,1]
sequences=[generate_sequence(length) for length in lengths]
print(sequences)
