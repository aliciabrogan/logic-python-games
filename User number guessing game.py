#import libraries needed
import random
import math
import sys

#asking the user for an upper and lower bound for the range for the computer to pick from
upper = int(input("Please pick an upper bound for your range:"))
lower = int(input("Now, a lower bound:"))
upper1 = upper
lower1 = lower

#the case where the user picks a lower bound greater than the upper bound
while lower > upper:
    print("Lower bound can't be greater than higher bound! Please pick a new range:")
    upper = int(input("Please pick an upper bound for your range:"))
    lower = int(input("Now, a lower bound:"))
    
#denoting two new lists for the numbers 1-upper and 1-lower to go
listy_upper = []
listy_lower = []

#making the lists of all numbers between 1 and the upper bound, same with lower bound
while upper > 0:
    listy_upper.append(upper)
    upper = upper - 1
    
while lower > 0:
    listy_lower.append(lower)
    lower = lower - 1
    
#denoting the list that will hold all the numbers between and including the upper and lower bound
listy_range = []

#adding the lower bound value to this list
listy_range.append(listy_lower[0])

#adding the values between the lower and upper bound, including the upper bound
for item in listy_upper:
    if item not in listy_lower:
        listy_range.append(item)
        
#computer now randomly chooses a value and the guessing can begin
random_choice = random.choice(listy_range)

#denoting each different number the player will choose
choice_i = 0
#creating a counter to check how many guesses the player has had
counter = 0

#Letting the player know how many guesses they have (formula)
print("You have", math.trunc(math.log(upper1 - lower1 + 1, 2)), "guesses or you'll lose!")

#this will keep running while user's guess isn't right until there have been too many guesses and it stops
while choice_i != random_choice:
    counter = counter + 1
    #as soon as the counter gets too high, this final message will print and the script will stop, game over :(
    if counter > math.log(upper1 - lower1 + 1, 2):
        print("Too many guesses! You lose!")
        sys.exit()
    choice_i = int(input("Please guess my number:"))
    if choice_i < random_choice:
        print("Too low!")
    if choice_i > random_choice:
        print("Too high!")
    #as soon as user guesses right, this final message will print
    if choice_i == random_choice:
        print("Well done! You guessed the number in", counter, "guess(es)!")

