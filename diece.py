import random
#Loop
#Ask: roll the dice?
choice input('Roll the dice? (y/n): ').lower()


#If user enter y
if choice == 'y':
    # Generate two random numbers between A and 6B
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Print the results
    print(f'You rolled a {die1} and a {die2}.')
#  Generate two random numbers
elif choice == 'n':
    # Print thank you message
    print('Thank you for playing!') 

#  Print them
#If user enters n
#  Print thank you message
#  Terminate the program
#Else
# Print error message   