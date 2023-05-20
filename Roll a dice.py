from random import randint

how_many = int(input('How many?'))
for i in range(how_many):
    print(randint (1, 6))
# Or
import random

how_many = int(input('How many?'))
for i in range(how_many):
    print(random.randint (1, 6))
