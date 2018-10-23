# import random package so that we can generate random numbers
from random import randint

# choices is an array => a contaienr that can hold multiple items 
# arrays are 0-nased  -> the first item is 0, the second is 1, etc
choices =["Rock", "Paper", "Scissors"]
player = False
# make the compputer choose a weapon from the choices at random
computer_choice = choices[randint(0,2)]

# print the choice to the terminal window
print("computer chooses: ", computer_choice)

 # set up our loop
while player is False:
	# set player to True by making a selection
	print("choose your weapon!")
	player = input("Rock, Paper or Scissors?")

	print(player, "\n")


	# check for a tie = choices are the same
	if player == computer_choice:
		print("Tie! You live to shoot again")
	# check to see if the computer choice beats our choice or not	
	elif player == "Rock":
		if computer_choice == "Paper":
			# computer won. crap!!
			print("You Lose! paper covers rock")
		else:
			# we win! such winning
			print("You Win!", player, "smashes", computer_choice)
	elif player == "paper":
		if computer_choice == "Scissors":
			print("You Lose!", computer_choice, "cut", player)
		else:
			print("You Won! Would ya just look at it", player, "covers", computer_choice)	

	elif player == "scissors":
		if computer_choice == "rock":
			print("You Lose!", computer_choice, "smashes", player)
		else:
			print("you win!", player, "Cut", computer_choice)
	elif player == "quit":
		exit()
	else:
		print("check your spelling.. thats not a valid choice\n")

		player = False
		computer_choice = choices[randint(0, 2)]	