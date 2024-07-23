import random
while True:
    level=input("Level:")
    if level.isdigit():
        level=int(level)
        if level>1:
            x=random.randint(1,level)
            break

while True:
    guess=input("Guess:")
    if guess.isdigit():
        guess=int(guess)
        if guess<=level:
            if guess<x:
                print("Too small!")
            elif guess>x:
                print("Too large!")
            else:
                print("Just right!")
                break
