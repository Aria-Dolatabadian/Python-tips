import random
ai_choice = random.randint(1,10)
for i in range(3):
    user_input=input('Enter a number:')
    if int(user_input) == ai_choice:
        print('You won')
        break
    else:
        print('Try again')
print(f'The correct answer was {ai_choice}')
