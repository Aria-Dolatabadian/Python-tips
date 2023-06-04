from random import choice
def generate_sequence(length):
    bases=['A','T','C','G']
    sequence=[choice(bases) for i in range(length)]
    sequence=''.join(sequence)
    return sequence
number_of_sequences=3
sequences=[generate_sequence(10)for i in range(number_of_sequences)]
print(sequences)
