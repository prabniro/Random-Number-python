import random

def Userguess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess!= random_num:
        guess = int(input(f"guess a random number between 1 and {x}: "))
        if (guess < random_num):
            print("the number is too low")
        elif(guess > random_num):
            print("the number is too high")
    
    print("Yay you have guess right")

Userguess(10)