import random

top_of_range = input('Type a number: ')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0
print(random_number)

while True:
    user_guesses = input('Make a guess: ')
    guesses += 1
    print(user_guesses)

    if user_guesses.isdigit():
        user_guesses = int(user_guesses)
    else:
        print('Please type a number.')
        continue

    if user_guesses == random_number:
        print('Correct!')
        break
    elif user_guesses not in [0, top_of_range]:
        print('Uou are not in quiz range!')
    elif user_guesses > random_number:
        print('You were above the number!')
    else:
        print('You were below the number!')

print(f'You got this in {guesses} guesses.')
