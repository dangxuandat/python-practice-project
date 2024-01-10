import math
import random


lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)

print("\n\tYou've only ", round(math.log(upper - lower + 1 , 2)), " chances to guess the integer!\n")

count = 0

while count < math.log2(upper - lower + 1):
    count += 1
    guess = int(input("Guess a number:- "))
    
    if x == guess: 
        print("Congratulations you dit it in ", count, " try")
        break;
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("You guess too high!")

if count >= math.log2(upper - lower + 1):
    print("\nThe number is ", x)