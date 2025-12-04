#importing necessary files
import random

i = 1 #number of guesses so far
listy = [] #list that will print with appended number or X to tell the player whether they got any digits in the right place
guess_i = 1 #denoting a number that the guess can't be so the while statement works, will be user's guess

#getting the computer to choose a random number between 1000 (inclusive) and 10000 (exclusive)
compchoice = random.randint(1000, 10000)

#finding each digit of the computer's number and putting them in a list
compdigitlist = [int(compchoice/1000), int((compchoice%1000)/100) ,int((compchoice%100)/10) ,compchoice%10]

#intro to game
print("""Let's see how fast you can guess my 4-digit number! \n
                    Guesses not in range won't be counted""")

#while loop for whilst guess isn't exactly right yet
while guess_i != compchoice:
    k=0 #denotes the index of the lists being compared
    l=0 #denotes how many digits are currently right
    #asking user for next guess
    guess_i = int(input('Please enter guess ' + str(i) + ':'))
    #making a list from the guess digits
    guessdigitlist = [int((guess_i)/1000), int(((guess_i)%1000)/100) ,int(((guess_i)%100)/10) ,(guess_i)%10]
    
    #checking the guess is 4 digits
    while guess_i<1000 or guess_i>9999:
        guess_i = int(input("That's not in range! Please guess a 4-digit number:"))
    
    #checking whether any digits in the computer's number and guess are the same
    while k<4:
        #appending the digit if it's the same
        if compdigitlist[k] == guessdigitlist[k]:
            listy.append(compdigitlist[k])
            l = l+1
        else:
            #appending an X if it isn't
            listy.append("X")
        k=k+1
    print(listy)
    if l<4:
        print("You got ",l, "correct!")
        i = i+1
    listy.clear()

print("Well done! You guessed my number was",compchoice, "in", i, "guess(es)!")


