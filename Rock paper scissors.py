import random
#defining
r = str('rock')
p = str('paper') 
s = str('scissors')
l = str('You lose!')
w = str('You win!')
d = str('Draw, play again!')
answer = str('y')
listy = [r,p,s]
#letting the user and computer choose rock paper or scissor
while answer == str('y'):
    computerchoice = random.choice(listy)
    userchoice = str(input("Rock, paper, scissors..."))
    print("You:", userchoice, "VS", computerchoice, ":Me")
#telling the computer what happens with each choice
    while computerchoice == userchoice:
        print(d)
        computerchoice = random.choice(listy)
        userchoice = str(input("Rock, paper, scissors..."))
        print("You:", userchoice, "VS", computerchoice, ":Me")
    if computerchoice == r:
        if userchoice == s:
            print(l)
            answer = str(input("Play again? y/n"))
        if userchoice == p:
            print(w)
            answer = str(input("Play again? y/n"))
    if computerchoice == p:
        if userchoice == s:
            print(w)
            answer = str(input("Play again? y/n"))
        if userchoice == r:
            print(l)
            answer = str(input("Play again? y/n"))
    if computerchoice == s:
        if userchoice == r:
            print(w)
            answer = str(input("Play again? y/n"))
        if userchoice == p:
            print(l)
            answer = str(input("Play again? y/n"))
        
print("Thanks for playing!")

