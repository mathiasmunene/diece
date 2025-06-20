import random
#Loop
#Ask: roll the dice?
choice = input('Roll the dice? (y/n): ').lower()


#If user enter y
if choice == 'y':
    # Generate two random numbers between A and 6B
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    

#  Print them
#If user enters n
#  Print thank you message
#  Terminate the program
#Else
# Print error message   