
# Importing a function called shuffle from a library named random
from random import shuffle

# Creating a list which is gonna be used in this tutorial( any list of your choice )
my_list = [' ', 'O', '']

# Creating a function to shuffle the list and return its value,
# because the using the function shuffle on my list shuffles the list and 
# returns nothing hence if we try to store it in a variable
# it returns the none type
def shuff(my_list):
    shuffle(my_list)
    return my_list

# Creating a function to guess the number within the range of 0 to 3 i.e. 0, 1, 2 and not including 3
# the while loop checks the value of guess each time. Initially the value is kept to empty list so 
# the condition is false and the loop asks the user for input and returns the value as integer.
def guess_num():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Select any one of the index ; 0 , 1 , 2 : ")
    return int(guess)
    
# Creating a function by utilizing both the function above to check whether the input guess number of
# the user which is type casted as integer and it mentioned as the index on the new list shuffled, if 
# the guess index is equal to the index of the Capital 'O' the user had won.
def monte(mylist,guess):
    if mylist[guess] == 'O':
        print("Congrats")
    else:
        print("Better luck next time")
        print(mylist)
        
# Calling the functions in the right order to execute the script in order        
shuffled = shuff(my_list)
guess = guess_num()

# Calling the final function for the game
monte(shuffled,guess)
