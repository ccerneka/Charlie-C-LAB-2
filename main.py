import random

game_number = random.randint(1, 10)
guess_count = 0

while True:
    guess = int(input("enter a number between 1 and 10: "))
    guess_count += 1

    if guess > game_number:
        print("too high")
    elif guess < game_number:
        print("too low")
    else:
        if guess_count <= 5:
            print("you did good")
        else:
            print("it's about time")
        break