import  random

top_of_range = input('Type a number:  ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number greater than 0 next')
        quit()
else:
    print('Invalid')
    print('Please type a number next time')
    quit()

random_number = random.randrange(top_of_range)
print(str(random_number))

guesses = 0

while True:
    guesses += 1
    user_guess = input('Guess a number between 1 and '+str(top_of_range)+': ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Invalid, type a number next time!')
        continue

    if user_guess == random_number:
        print('Congratulations! You got it.')
    else:
        if user_guess > random_number:
            print('Sorry, You got it wrong! try a lower number')
            continue
        else:
            print('Sorry, You got it wrong! try a higher number')
        continue
    break

print('You guessed in ', guesses, ' guesses')