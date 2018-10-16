# import random package so that we can generate random numbers
from random import randint

# choices is an array => a contaienr that can hold multiple items 
# arrays are 0-nased  -> the first item is 0, the second is 1, etc
choices =["Rock", "Paper", "Scissors"]

# make the compputer choose a weapon from the choices at random
computer_choice = choices[randint(0,2)]

# print the choice to the terminal window
print("computer chooses: ", computer_choice)