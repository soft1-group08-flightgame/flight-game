# 1. import
import sys
import functions as f
import mysql.connector
import config


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

# player features
# user_name = input("Enter yourname:")
# nation = input("Enter your Nation")
# age = int(input("Enter your age"))
# to save time
user_name = 'Rodri'
nation = 'Argentina'
age = 20
heritage = 30000  # to be defined

# game state variables
pl_money = heritage
skill_points = 20

# game conditions
tournament_fee_rate = 0.02  # tournament_fee is calculated as t_prize_money * tournament_fee_rate
travel_fee = 5000
win_threshold = 0.7

# context variables
MONTHS = ("January","February","March","April","May","June","July","August","September","October","November","December")

# 5. game

# Introduction to the game
# player features have been requested in variables section

f.print_game_intro(user_name, nation, age, heritage)

# Game starts...
print(f'\n{MONTHS[-1]} is starting. The following tournaments are coming up, choose one of them:')

# Get tournament of the month
t_list = f.run_query(connection,
        f"""select tournaments.*, country.name 
                     from tournaments
                     inner join country on tournaments.iso_country = country.iso_country
                     where tournaments.month = '{MONTHS[-1]}';
                    """)

for i in t_list:
    print(i)

# Display the list of tournaments for this month
index = 1
for i in t_list:
    print(f"{index}. {i[5]} ({i[11]})")
    index += 1

t_fees = []
for i in t_list:
    t_fees.append(i[10]*tournament_fee_rate)

if pl_money < min(t_fees) + travel_fee:
    print("You don't have enough money to continue playing.")  # the game stops and quit
    print("Game Over.")
    sys.exit()

# user chooses 1 and we assigned the decision to selected_tournament = 1
while True:
    selected_tournament = int(input("Enter your option: "))
    if selected_tournament in range(len(t_list)+1)[1:]: break

print(selected_tournament)

if pl_money < (t_fees[selected_tournament-1]) + travel_fee:
    print("You don't have enough money to play this tournament. Please choose another from the list.") # we need to send the user back to the tournament selection screen
else:
    print(f"{t_list[selected_tournament-1][5]} is played in {t_list[selected_tournament-1][7]}, {t_list[selected_tournament-1][11]}. The tournament gives {t_list[selected_tournament-1][4]} points and ${t_list[selected_tournament-1][10]} to the champion. The entrance cost of the tournament is {t_fees[selected_tournament - 1]} and the travel expenses are {travel_fee}.")


if input("Do you want to play the tournament? (Y/N)").upper() == "N":
    print("Ok. Please choose another from the list.") # we need to send the user back to the tournament selection screen
else:
    print(f"Great!, flying to {t_list[selected_tournament-1][11]} ...")

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


