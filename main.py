# 1. import
import sys
import functions as f
import config
import mysql.connector


# 2. connection

connection = mysql.connector.connect(
    host = config.HOST,
    port = config.PORT,
    database = config.DB,
    user = config.USER,
    password = config.PASS,
    autocommit = True
)

# 3. functions

# 4. variables
# Starting variables
heritage = 30000  # to be defined
skill_points = 20
# Player Features

# Simulate a test player to save time for tests
test_player = {'user_name': 'Rodri','nation': 'Argentina','age': 20}

# Create player
player = f.get_player_data(test_player)

# Game State variables
player['money'] = heritage
player['money'] = heritage
player['skill_points'] = skill_points

# game conditions
TOURNAMENT_FEE_RATE = 0.02  # tournament_fee is calculated as t_prize_money * TOURNAMENT_FEE_RATE
TRAVEL_FEE = 5000   # it is going to be a fix value until further change
WIN_THRESHOLD = 0.7 # it is going to be a fix value until further change

# context variables
MONTHS = ("January","February","March","April","May","June","July","August","September","October","November","December")

# 5. game

# Introduction to the game

# player features have been requested in get_player_data() section
f.print_game_intro(player['user_name'], player['nation'], player['age'], heritage)

# Game starts...
print(f'\n{MONTHS[-1]} is starting. The following tournaments are coming up, choose one of them:')

# TOURNAMENT SELECTION SECTION - it is a loop that breaks when the user confirms the tournament
# Get tournaments of the month
t_list = f.get_tournaments_of_the_month(connection,MONTHS[1])

for t in t_list:
    print(t)

# start loop

# Check losing condition, find the cheapest option vs player money
t_fees = []
for t in t_list:
    t['fee'] = t['prize_money'] * TOURNAMENT_FEE_RATE
    t_fees.append(t['fee'])

if player['money'] < min(t_fees) + TRAVEL_FEE:
    print("Oh no! You don't have enough money to continue playing.")  # the game stops and quit
    print("Game Over.")
    sys.exit()

f.show_tournaments(t_list) # Display options

# Assign the decision to 'selected_tournament'
while True:
    user_input = input("Enter your option: ")
    if user_input.isnumeric():
        user_input_num = int(user_input)

        if 1 <= user_input_num <= len(t_list):
            selected_tournament = t_list[user_input_num - 1]
            break
        else:
            print(f"Please enter a valid number of tournament, between 1 and {len(t_list)}")
    else:
        print("Select the tournament with a valid number.")

print(selected_tournament)

if player['money'] < (selected_tournament['fee']) + TRAVEL_FEE:
    print("You don't have enough money to play this tournament. Please choose another from the list.") # we need to send the user back to the tournament selection screen

else:
    print(f"{selected_tournament['name']} is played in {selected_tournament['city']}, {selected_tournament['country']}. The tournament gives {selected_tournament['points']} points and ${selected_tournament['prize_money']} to the champion. The entrance cost of the tournament is {selected_tournament['fee']} and the travel expenses are {TRAVEL_FEE}.")


if input("Do you want to play the tournament? (Y/N)").upper() == "N":
    print("Ok. Please choose another from the list.") # we need to send the user back to the tournament selection screen
else:
    print(f"Great!, flying to {selected_tournament['country']} ...")
#     break

current_tournament = selected_tournament
# The tournament is today! Press enter to start.
# Brisbane International tournament starting!
# [play tournament(skill_points, tc_id)] == 0.95, 0.65 SF, 0,43 QF, 0.3 you lost QF
# Game 1, QF... you win!    -- QF gives 20% of points and money
# Game 2, SF... you win!    -- SF gives 50% of points and money
# Game 3, F...  you win!   -- F gives 70% of points and money
#  Champion                 -- Champion gives 100% of points and money
# Congratulations! you are the new champion of Brisbane International [t_name]. Earned points: 250 [earned_points: t_points * position]
# New ranking: 210 [pl_ranking]
# Money: 129000 [pl_money]
# Total earned points: 250 [pl_points]
# You are doing a great job! Keep it up!

# January([months[1]]) is now starting. The following tournaments are coming up, choose one of them:
# 1.Auckland Open (NZ)   [t_name], ([t_country])
# 2.Adelaide International (Australia)  [t_name], ([t_country])
# 3. Open Sud de France (France)    [t_name], ([t_country])

# ... game continues looping every month the same, if you run out of money, you will loose the game. Quit()
#
# When 12 months have passed the game is over. It will report the game state.
# Game state:
# Ranking:
# Earned money:
# Total earned points:
# If final ranking is 1, player wins the game. If final ranking is not 1 but money is enough to keep playing and save the player's family, the program celebrates it, and thanks for helping the tennis player to achieve the dream.


