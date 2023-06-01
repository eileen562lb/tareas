# Random number generation -- blackjack
#
# In the game of blackjack, the goal is to get as close to 21 as possible
# without going over.  In this game, the dealer will draw a random number
# between 1 and 10, and the player will draw a random number between 1 and 10.
# 
# The player can draw as many times as they want, but if they go over 21, they 
#   lose.  If they get closer to 21 than the dealer, they win.
# 
# Write a program that will play blackjack with the user.
# 
# The program should give the user and the dealer two cards to start.
# 
# That means two random numbers between 1 and 10 for the player
#   and two random numbers for the dealer.
# 
# That means you'll have two variables to start with. 
#
# You will need to keep track of the user's total, and the dealer's total.
# 
# The user should be told the cards they have, as well as the total.
# 
# Each turn:
#     The user has a choice to draw first.
# 
#     The user should be asked if they want to draw another card. If they say 'yes',
#       the program should draw a random number between 1 and 10 and add it to the
#       player's total.
# 
#     If the user's total for their cards is greater than 21, they have lost, and the
#         dealer automatically wins.
#     If the dealer's total is less than 17, will always should draw another card. 
# 
#     If the dealer's total is greater than or equal to 17, the dealer should not
#        draw another card.
#
#     If the dealer's total is greater than 21, the dealer game has ended.
# 
# After each turn, if user says 'no' or goes over 21, the game should end.
# At the end, the program should print out the user's total, the dealer's total,
# 
# You will need a while loop that checks two variables. Checking the dealer's total, and
#   checking if the user wants to draw another card, if they're over 21, or the dealer
#   is over 17. (Why? If the dealer is over 17, they've either lost or they won't draw.)
# 
# If you need documentation for while loops, you can find it here:
# https://www.w3schools.com/python/python_while_loops.asp
# 
# You will also need to use the input function, which you can find documentation for here:
# https://www.w3schools.com/python/python_user_input.asp
# 
# You can use the random.randint function to generate random numbers.
# If you need documentation on random int generation, you can
# find it here:
# https://www.w3schools.com/python/ref_random_randint.asp
# 
# I've started the code for you already.

from random import *
# draw the player's first card
player_total = randint(1,10)
# draw the player's second card, and add it to the player's total
player_total = player_total + randint(1,10)

# draw the dealer's first card
dealer_total = randint(1,10)
# draw the dealer's second card
dealer_total = dealer_total + randint(1,10)

player_response = 'yes'

while dealer_total < 17 and player_total < 21 and player_response == 'yes':
    if player_total < 20:
        # you should add code before they're asked to draw another card
        # that print the player's total, something like "You currently have 15 points."
        # that way they know before they're asked if they should draw another card
    
        player_response = input("Do you want to draw another card? ")
    
        # Add code here to check if the user said 'yes',
        #   and if they did, add another card to the player's
        #   total (a random number between 1 and 10)

        # Add code here to check the dealer's total
        #    and if it's less than 17, add another card to their total

if player_total > 21:
    print("You lose!")

elif dealer_total > 21:
    print("You win!")

elif player_total > dealer_total and player_total <= 21:
    print("You win!")
