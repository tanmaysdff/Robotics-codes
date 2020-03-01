#This program is a fun game to guess a random number.
import random
print("I have thought of a number are you smart enough to guess it?")
print("Guess the number between 1-100:")
guessNumber =  int(input())
thoughtNumber= random.randint(1,100)
counter=1
while(counter<5):  
    if (guessNumber==thoughtNumber):
        print("Player wins!!!!!")
        break
    elif (guessNumber<thoughtNumber):
        print("The number to be guessed is higher try again.")
        
    else:
        print("The number to be guessed is lower try again.")    
    print("You have ",5-counter, " tries remaining.")
    print("Guess the number again:")
    guessNumber =  int(input())
    counter = counter+1
if (counter ==5):
    print ("Computer wins :(")
    print ("The number was ",thoughtNumber)
