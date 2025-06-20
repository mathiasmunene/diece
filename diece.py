import random
#Loop
#Ask: roll the dice?
while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'You rolled a {die1} and a {die2}.')
    elif choice == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Invalid choice!')

#  Print them
#If user enters n
#  Print thank you message
#  Terminate the program
#Else
# Print error message   