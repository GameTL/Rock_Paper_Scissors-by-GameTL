# os.system('cls') for Windows
# os.system('clear') for Unix
import random, os, csv, time
bot_weapon = ''
player_score = 0
combo_power = 1
rock = 'Rock 🗿'
paper = 'Paper 🧻'
scissor = 'Scissor ✂️'
input_rock = ['Rock', 'r', 'R', 'rock']
input_paper = ["Paper", 'R', 'p', 'paper']
input_scissor = ["Scissor", 'S', 's', 'scissor']

weapons = [rock, paper, scissor]
keep_playing = True
player_name = ''

#  ---------------------------------Fucntion---------------------------------


def replay_function():
    global keep_playing
    yea_or_nae = input()
    if yea_or_nae == 'y':
        keep_playing = True
        os.system('clear')
    elif yea_or_nae == 'n':
        keep_playing = False
        os.system('clear')
    else:
        print('Please only enter [y/n]')
        replay_function()
        # Work on the loop incase the user input shit-input


def normalise_input():
    global user_weapon
    if user_weapon in input_paper:
        user_weapon = paper
    elif user_weapon in input_scissor:
        user_weapon = scissor
    elif user_weapon in input_rock:
        user_weapon = rock


def divider():
    print('----------------------------------------------------')
    print()


# global is pass by reference
def random_gen_bot_weapon(weapons):
    global bot_weapon
    bot_weapon = weapons[random.randint(0,2)]


def input_check_and_route_user_weapon():
    global player_status
    global user_weapon
    print("""What's your weapon?
    r or rock for Rock
    p or paper for Paper
    s scissor for Scissor
    """)
    user_weapon = input()
    if user_weapon in rock + paper + scissor:
        normalise_input()
        if bot_weapon == rock:
            bot_is_rock()
        elif bot_weapon == paper:
            bot_is_paper()
        elif bot_weapon == scissor:
            bot_is_scissor()
    else: 
        os.system('clear')
        divider()
        print("C'mon! Do you know how to play rock paper scissor?")
        input_check_and_route_user_weapon()


def enter_or_update_username():
    global player_name
    print('Please enter your name')
    player_name = input()


def display_score():
    print()
    print('---------------------------------- Score: ' + str(player_score))


def write_score_csv():  
    with open('player_file.csv', mode='a') as player_file:
        player_writer = csv.writer(player_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        player_writer.writerow([player_name,player_score])


def read_score_csv():
    with open('player_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)


# ---------------------------------Bot Dependant---------------------------------


# From function input_and_check_user_weapon(), program makes decision here
def bot_is_rock():
    global player_status
    if user_weapon == paper:
        player_status = 'win'
    elif user_weapon == scissor:
        player_status = 'lose'
    elif user_weapon == rock:
        player_status = 'draw'

def bot_is_paper():
    global player_status
    if user_weapon == scissor:
        player_status = 'win'
    elif user_weapon == rock:
        player_status = 'lose'
    elif user_weapon == paper:
        player_status = 'draw'
 
def bot_is_scissor():
    global player_status
    if user_weapon == rock:
        player_status = 'win'
    elif user_weapon == paper:
        player_status = 'lose' 
    elif user_weapon == scissor:
        player_status = 'draw'

#  ---------------------------------End-Fucntion---------------------------------


os.system('clear')
print('Rock Paper Scissor Python or RPSP, By DirtyRat')
while keep_playing is True:
    display_score()
    random_gen_bot_weapon(weapons)
    input_check_and_route_user_weapon()
    
    os.system('clear')
    divider()
    print("Bot's Weapon is " + bot_weapon)
    print('Your Weapon is ' + user_weapon)
    print('You ' + player_status + '!')
    
    if player_status == 'win':
        player_score = player_score + (100 * (2)**combo_power)
        combo_power = combo_power + 1
    if player_status == 'lose':
        time.sleep(0.5)
        print('U disaapointment')
        time.sleep(0.5)
        print('U Lost HAHA')
        time.sleep(0.5)
        print('U Lost HAHA')
        time.sleep(0.5)
        print('TM by Tony Xu')
        divider()
    display_score()
    divider()
    print('You want to keep playing?')
    print('If you lose the game ends')
    print('[y/n]')
    replay_function()
enter_or_update_username()
write_score_csv()
read_score_csv()
