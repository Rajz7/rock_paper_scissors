#ROCK PAPER SCISSORS GAME
import random

def computer():
    choice = ['rock', 'paper', 'scissors']
    compChoice = random.choice(choice)
    print("Computers move: " + compChoice)
    return compChoice

def checkWinner(playerChoice, compChoice):
    if playerChoice == compChoice:
        print("Its a TIE!")
    
    elif playerChoice == 'rock' and compChoice == 'paper':
       print("You LOSE")
    
    elif playerChoice == 'rock' and compChoice == 'scissors':
       print("You WIN")

    elif playerChoice == 'paper' and compChoice == 'scissors':
        print("You LOSE")

    elif playerChoice == 'paper' and compChoice == 'rock':
        print("You WIN")

    elif playerChoice == 'scissors' and compChoice == 'rock':
        print("You LOSE")

    elif playerChoice == 'scissors' and compChoice == 'paper':
        print("You WIN")


playerChoice = input("Enter you choice: ").lower()

if playerChoice != "rock" or "paper" or "scissors":
    print("Invalid Choice")
    
else:
   print("Your move: " + playerChoice)
   compChoice = computer()
   checkWinner(playerChoice, compChoice)



