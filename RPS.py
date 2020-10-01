#! python3
import random
"""
Let's make a game of Rock, Paper, Scissors, where the user will play against 
the computer. 
"""

# Ask the user their name and store it in a variable called name.
name = input('Hello! What\'s your name?')
print ('Okay ' + name + '! Let\'s play Rock, Paper, Scissors.')

print('Rock breaks scissors, scissors beat paper, paper beats rock')

#Making a list
rps = ['r','p','s']

#Two variables for score
player1 = 0	
player2 = 0

print('\n\nR: Rock			 P:Paper			  S:Scissor')
user = input()
user.lower()

python = random.choice(rps)
if user == python:
	print('It\'s a tie!')

while player1 < 5 or player2 < 5:
    
    #Prompt the user to enter their choice and store it in 'user'
    print ('R: Rock,      P: Paper,     S: Scissor')
    user = input('Enter your choice: ')
    
    #Here is the computer's selection is stored in the python variable
    import random #Normally, we import modules at the begining of the script.
    python = random.choice(rps)
    
    #Compare the variables user and py in the if statement. 
    if user == python: 
        print ('It\'s a tie!')
    
    # First case
    elif user == 'p' and python == 'r':
        print ('You entered Paper. I had Rock. You win!') 
        player1 = player1 + 1

    # Second case
    elif user == 's' and python == 'r':
        print ('You entered Scissors. I had Rock. I win!') 
        player2 = player2 + 1

    # Third case
    elif user == 'r' and python == 'p':
        print ('You entered Rock. I had Paper. I win!') 
        player2 = player2 + 1

    #Fourth case
    elif user == 's' and python == 'p':
        print ('You entered Scissors. I had Paper. You win!') 
        player1 = player1 + 1

    #Fifth case
    elif user == 'r' and python == 's':
        print ('You entered Rock. I had Scissors. You win!') 
        player1 = player1 + 1

    # Sixth case
    elif user == 'p' and python == 's':
        print ('You entered Paper. I had Scissors. I win!') 
        player2 = player2 + 1
        
# When someone has reached 5 points:
if player2 == 5:
    print ('Python wins!')
elif player1 == 5:
    print ('You win! Congrats!')
    
