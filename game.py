import random
print("Welcome to Prince's Number guessing game!")
#Generate a number betwwn 1 and 100
number = random.randint(1, 100)

#Trial attempts
number_of_atempts = 5

# Loop through until the user runs out of tries
while number_of_atempts > 0:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number:
        print("Congratulations! You've guessed the right number.")
        break
    elif guess < number:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")
    number_of_atempts -= 1
    print("You have", number_of_atempts, "attempts left.")

# If the user runs out of tries, print the answer
if number_of_atempts == 0:
    print("Sorry, you ran out of attempts. The number was", number)