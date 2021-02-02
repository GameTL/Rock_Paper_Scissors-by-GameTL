
# os.system('cls') for Windows
# os.system('clear') for Unix
import random
import os
import csv
import time
from os import path
from sys import platform
if platform == ('linux', 'linux2', 'darwin'):
    clear = 'clear'
    platform = 'Unix'
elif platform == 'win32':
    clear = 'cls'
    platform = 'Windows'
#  -------------------------------ASCII-HANDS--------------------------------
ascii_player_rock = ('''
     _______
----'   ____)
       (_____)
       (______)
       (_____)
----.__(___)
    Player''')
ascii_player_paper = ('''
      _______
----'    ____)___
           ______)
          ________)
          _______)
----._ ________)
    Player''')
ascii_player_scissor = ('''
     _____
----'  ___)______
         ________)
       ___________)
       (____)
----.__(___)
    Player''')

ascii_bot_rock = ('''
                        _______
                       (____   '----
                     (_____)
                    (______)
                     (_____)
                        (___)__.----
                            Bot''')
ascii_bot_paper = ('''
                          _______
                      ___(____    '----
                     (______
                    (________
                     (_______
                        (_______ _.----
                            Bot''')

ascii_bot_scissor = ('''
                             _____
                      ______(___  '----
                     (________
                    (___________
                          (____)
                           (___)__.----
                            Bot''')
#  -------------------------------VARIABLES--------------------------------
bot_weapon = ''
player_score = 0
combo_power = 1
player_rock = 'Rock' + ascii_player_rock
player_paper = 'Paper' + ascii_player_paper
player_scissor = 'Scissor' + ascii_player_scissor
bot_rock = 'Rock' + ascii_bot_rock
bot_paper = 'Paper' + ascii_bot_paper
bot_scissor = 'Scissor' + ascii_bot_scissor
input_rock = ['Rock', 'r', 'R', 'rock']
input_paper = ["Paper", 'R', 'p', 'paper']
input_scissor = ["Scissor", 'S', 's', 'scissor']
bot_weapon_list = [bot_rock, bot_paper, bot_scissor]
keep_playing = True
player_name = ''

#  ---------------------------------Fucntion---------------------------------


def time_pause():
    time.sleep(0.5)


def introduction():
    print('Rock Paper Scissor Python or RPSP, By DirtyRat')
    divider()
    print('''
      Rock                  Paper                   Scissor
     _______                 _______                    _____
----'   ____)          ----'    ____)___           ----'  ___)______
       (_____)                    ______)                   ________)
       (______)                  ________)                ___________)
       (_____)                   _______)                 (____)
----.__(___)           ----._ _______)            ----.__(___)
    ''')
    divider()
    print('System: ' + platform)
    print()


def replay_function():
    global keep_playing
    yea_or_nae = input()
    if yea_or_nae == 'y':
        keep_playing = True
        os.system(clear)
    elif yea_or_nae == 'n':
        keep_playing = False
        os.system(clear)
    else:
        print('Please only enter [y/n]')
        replay_function()
        # Work on the loop incase the user input shit-input


def normalise_input():
    global player_weapon
    if player_weapon in input_paper:
        player_weapon = player_paper
    elif player_weapon in input_scissor:
        player_weapon = player_scissor
    elif player_weapon in input_rock:
        player_weapon = player_rock


def divider():
    print('**********************************************')


# global is pass by reference
def random_gen_bot_weapon(bot_weapon_list):
    global bot_weapon
    bot_weapon = bot_weapon_list[random.randint(0, 2)]


def input_check_and_route_player_weapon():
    global player_status
    global player_weapon
    print("""What's your weapon?
    r or rock for Rock
    p or paper for Paper
    s scissor for Scissor
    """)
    player_weapon = input()
    if player_weapon in input_rock + input_paper + input_scissor:
        normalise_input()
        if bot_weapon == bot_rock:
            bot_is_rock()
        elif bot_weapon == bot_paper:
            bot_is_paper()
        elif bot_weapon == bot_scissor:
            bot_is_scissor()
    else:
        os.system(clear)
        divider()
        print("C'mon! Do you know how to play rock paper scissor?")
        input_check_and_route_player_weapon()


def enter_or_update_username():
    global player_name
    print('Please enter your name')
    player_name = input()


def display_score():
    print()
    print('---------------------------------- Score: ' + str(player_score))


def initalise_csv_file():
    if str(path.exists('player_file.csv')) == 'False':
        with open('player_file.csv', 'w', newline='') as player_file:
            player_writer = csv.writer(player_file, delimiter=',')
            player_writer.writerow(['Player', 'Score'])
    if str(path.exists('player_file.csv')) == 'True':
        pass


def write_score_csv():
    with open('player_file.csv', 'a', newline='') as player_file:
        player_writer = csv.writer(player_file, delimiter=',')
        player_writer.writerow([player_name, player_score])


def read_score_csv():
    with open('player_file.csv') as player_file:
        player_reader = csv.reader(player_file, delimiter=',')
        row_count = sum(1 for row in player_reader)
        row_count_minus = row_count - 1
    os.system(clear)
    print('Your score is saved')
    with open('player_file.csv') as player_file:
        player_reader = csv.reader(player_file, delimiter=',')
        for row in list(player_reader)[row_count_minus:row_count]:
            print(row)


# ------------------------------Bot Dependant------------------------------


# From function input_and_check_player_weapon(), program makes decision here
def bot_is_rock():
    global player_status
    if player_weapon == player_paper:
        player_status = 'win'
    elif player_weapon == player_scissor:
        player_status = 'lose'
    elif player_weapon == player_rock:
        player_status = 'draw'


def bot_is_paper():
    global player_status
    if player_weapon == player_scissor:
        player_status = 'win'
    elif player_weapon == player_rock:
        player_status = 'lose'
    elif player_weapon == player_paper:
        player_status = 'draw'


def bot_is_scissor():
    global player_status
    if player_weapon == player_rock:
        player_status = 'win'
    elif player_weapon == player_paper:
        player_status = 'lose'
    elif player_weapon == player_scissor:
        player_status = 'draw'


#  ---------------------------------End-Fucntion---------------------------------
os.system(clear)
introduction()
input('Press enter to play the game')
while keep_playing is True:
    os.system(clear)
    display_score()
    random_gen_bot_weapon(bot_weapon_list)
    input_check_and_route_player_weapon()
    os.system(clear)
    divider()
    print('Your Weapon is ' + player_weapon)
    time_pause()
    print("Bot's Weapon is " + bot_weapon)
    print('You ' + player_status + '!')
    if player_status == 'win':
        player_score = player_score + (100 * (2)**combo_power)
        combo_power = combo_power + 1
    if player_status == 'lose':
        time_pause()
        print('U disaapointment')
        time_pause()
        print('U Lost HAHA')
        time_pause()
        print('U Lost HAHA')
        time_pause()
        print('TM by Tony Xu')
        divider()
    display_score()
    divider()
    print('You want to keep playing?')
    print('If you lose the game ends')
    print('[y/n]')
    replay_function()
enter_or_update_username()
initalise_csv_file()
write_score_csv()
read_score_csv()
