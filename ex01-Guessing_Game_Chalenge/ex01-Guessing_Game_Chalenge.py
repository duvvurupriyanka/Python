#Guessing Game Challenge:

#Generate the random number

from random import randint
random_number = randint(1,100)

#To print the game rules
with open('guessing_game.txt', mode = 'r') as f:
    print(f.read())

guesses_list = [0]

#Take the input from the player

while random_number != guesses_list[-1]:
    guess = int(input('Please enter the guess number:'))

    # Validating the input

    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
    else:
        guesses_list.append(guess)
        for num in guesses_list:
            if len(guesses_list) == 2:
                if abs(guesses_list[1] - random_number) == 0:
                    print("your guess is correct")
                    print("You have taken {} attempts".format(len(guesses_list)-1))
                    break
                elif abs(guesses_list[1] - random_number) < 10:
                    print("WARM")
                    break
                else:
                    print("COLD")
                    break
            else:
                if abs(guesses_list[-1] - random_number) == 0:
                    print("your guess is correct")
                    print("You have taken {} attempts".format(len(guesses_list)-1))
                    break
                elif abs(guesses_list[-1] - random_number) < 10:
                    print("WARMER")
                    break
                else:
                    print("COLDER")
                    break
                
print(guesses_list[1:])
