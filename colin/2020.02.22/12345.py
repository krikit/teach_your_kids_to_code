import random
the_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != the_number:
    if guess > the_number:
        print(guess, "was too high. Try again.")
    if guess < the_number:
        print(guess, "was too low. Try agin.")
    guess = int(input("Guess again: "))
print(guess, "was the number! You win!")    
    
