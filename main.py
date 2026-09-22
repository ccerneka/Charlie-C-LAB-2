import random


game_number = random.randint(1,10) 
print(game_number)

guess = int(input("enter a number between 1 and 10: "))
if guess > game_number: 
    print("too high")
elif guess < game_number:
    print("too low")
else: 
    print("YOU WIN!")