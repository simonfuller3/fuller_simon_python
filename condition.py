# print a message to the terminal window
print("rules that govern the state of water")

# set up a variable to hold the tempterature we input
current_temp = False

while current_temp is False:
		current_temp = input("enter a temperature:\n")
		# see what current temp is 
		print("you input:", current_temp)

		# if the current temp is at freezing or below, water is a solid
		if (int(current_temp) < 0 or (int(current_temp) ==0)):
			print("water is a solid! cuz it's at or below freezing")
			current_temp = False
			# else check another condition.  If its not freezing , is below boiling?
		elif (int(current_temp) < 100):
				print("water is a liquid, beuase its above freezing and below boiling")
				current_temp = False

		elif (int(current_temp) > 100 or (int(current_temp) == 100)):
				print("water us a gas. CUz its like, really hot")
				current_temp = False
