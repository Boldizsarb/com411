import random
print("please enter the minimum value:")
minimum_value = int(input())
print("Please enter the maximum value:")
maximum_value = int(input())
random_number = random.randrange(minimum_value and maximum_value)
print(f"I am thinking of a number beetwen {minimum_value} and {maximum_value} Can you guess it?")
guessed_correctly = False
while not guessed_correctly:
    print("please enter a number")
    guess = int(input())
    if guess == random_number:
        print("Congratulations! You guessed the correct answer!")
        guessed_correctly = True
    elif guess < random_number:
        print("Guess gigher")
    else:
        print("Guess lower.")

    
print("Game over!")
