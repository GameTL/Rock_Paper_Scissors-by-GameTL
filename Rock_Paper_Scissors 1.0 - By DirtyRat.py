import random
import os
bot_weapon = ''
player_score = 0
combo_power = 1
weapons = ['Rock', 'Paper', 'Scissor']
rock = ['Rock', 'r', 'R', 'rock']
paper = ["Paper", 'R', 'p', 'paper']
scissor = ["Scissor", 'S', 's', 'scissor']
keep_playing = True

# Bot Dependant-------------------------------------------------------
#  using or selects the whole line not just the string
def bot_is_rock():
    global status
    if user_weapon in paper:
        status = 'win'
    elif user_weapon in scissor:
        status = 'lose'
    elif user_weapon in rock:
        status = 'draw'

def bot_is_paper():
    global status
    if user_weapon in scissor:
        print()
        status = 'win'
    elif user_weapon in rock:
        status = 'lose'
    elif user_weapon in paper:
        status = 'draw'
    
def bot_is_scissor():
    global status
    if user_weapon in rock:
        status = 'win'
    elif user_weapon in paper:
        status = 'lose' 
    elif user_weapon in scissor:
        status = 'draw'


#  -------------------------------------------------------
#  Picker
# global is pass by reference
def divider():
    print()
    print('----------------------------------------------------')
    print()

def rando_gen_weapon(weapons):
    global bot_weapon
    bot_weapon = weapons[random.randint(0,2)]


def input_and_check_user_weapon():
    global status
    global user_weapon
    print("What's your weapon?")
    print("r or rock for Rock")
    print("p or paper for Paper")
    print("s scissor for Scissor")
    user_weapon = input()
    if user_weapon in rock + paper + scissor:
        if bot_weapon == 'Rock':
            bot_is_rock()
        elif bot_weapon == 'Paper':
            bot_is_paper()
        elif bot_weapon == 'Scissor':
            bot_is_scissor()
    else: 
        divider()
        print("C'mon! Do you know how to play rock paper scissor?")
        input_and_check_user_weapon()


def replay_function():
    global keep_playing
    yea_or_nae = input()
    if yea_or_nae == 'y':
        keep_playing = True
    elif yea_or_nae == 'n':
        keep_playing = False
    else:
        print('Please only enter [y/n]')
        replay_function()
        # Work on the loop incase the user input shit-input

# End of function definition -----------------------------

divider()
print('Rock Paper Scissor Python or RPSP, By DirtyRat')
divider()
while keep_playing is True:

    print('---------------------------------- Score: ' + str(player_score))
    rando_gen_weapon(weapons)
    input_and_check_user_weapon()
    
    if status == 'win':
        player_score = player_score + (100 * (2)**combo_power)
        combo_power = combo_power + 1
    if status == 'lose':
        pass
    print()
    divider()
    print("Bot's Weapon is " + bot_weapon)
    print('Your Weapon is ' + user_weapon)
    print('So you ' + status)
    print('---------------------------------- Score: ' + str(player_score))
    divider()
    print('You want to keep playing?')
    print('If you lose the game ends')
    print('[y/n]')
    replay_function()


print('Thanks for playing ')
with open('User_Score.txt', 'w') as User_Score :
    print('Saved')
    User_Score.write('You Score is saved')
    User_Score.write('Score is ' + str(player_score))