# 1. import
import random
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
heritage = 50000  # to be defined
skill_points = 20
winning_points = 1500 # the player must reach this points to win the game
# Player Features

# Simulate a test player to save time for tests
test_player = {'user_name': 'Rodri','nation': 'Argentina','age': 20}

# Create player
player = f.get_player_data(test_player)

# Game State variables
player['money'] = heritage
player['skill_points'] = skill_points
player['rank'] = 250

# ranking and points system
# rank, points
# 250 ,0
# 201 ,250
# 125 ,750
# 1   , 1500
# every 6 points you win, you climb 1 ranking position

# game conditions

REWARD_PERCENTAGE = {
    'Champion' : 1,
    'Finals' : 0.7,
    'Semi Finals' : 0.5,
    'Quarter Finals' : 0.35
}
WIN_THRESHOLD = {
    'Champion' : 80,
    'Finals' : 60,
    'Semi Finals' : 35,
    'Quarter Finals' : 0
    }
POSITIONS = {
    'Quarter Finals' :  {'min_score' :  0, 'reward_perc' : 0.35},
    'Semi Finals' :     {'min_score' : 35, 'reward_perc' : 0.50},
    'Finals' :          {'min_score' : 60, 'reward_perc' : 0.70},
    'Champion' :        {'min_score' : 80, 'reward_perc' : 1.00}
}
TOURNAMENT_FEE_RATE = 0.02  # tournament_fee is calculated as t_prize_money * TOURNAMENT_FEE_RATE
TRAVEL_FEE = 5000   # it is going to be a fix value until further change

# context variables
MONTHS = ("January","February","March","April","May","June","July","August","September","October","November","December")

# 5. game

# Introduction to the game

# player features have been requested in get_player_data() section
f.print_game_intro(player['user_name'], player['nation'], player['age'], heritage)

# Game starts...


# TOURNAMENT SELECTION SECTION - it is a loop that breaks when the user confirms the tournament
# Get tournaments of the month



# --- 2. THE SEASON LOOP [NEW] ---
# This loop connects everything. It runs 12 times (once per month).
for month in MONTHS:
    print(f"\n>>> CURRENT MONTH: {month.upper()} is starting. The following tournaments are coming up, choose one of them:'<<<")
    t_list = f.get_tournaments_of_the_month(connection,month)

    f.add_tournament_fees(t_list, TOURNAMENT_FEE_RATE)
    f.add_tournament_categories_and_difficulty(t_list)
    # for t in t_list:
    #     print(t)

    # Check LOSING CONDITION, find the cheapest option vs player money
    t_fees = []
    for t in t_list:
        t_fees.append(t['fee'])

    if player['money'] < min(t_fees) + TRAVEL_FEE:
        print("Oh no! You don't have enough money to continue playing.")  # the game stops and quit
        print("Game Over.")
        sys.exit()

    # Start tournament selection loop
    while True:

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

        if player['money'] < (selected_tournament['fee']) + TRAVEL_FEE:
            print("You don't have enough money to play this tournament 🙃. Please choose another from the list thanks.") # we need to send the user back to the tournament selection screen
            continue

        else:
            print(f"{selected_tournament['name']} is played in {selected_tournament['city']}, {selected_tournament['country']}. The tournament gives {selected_tournament['points']} points and ${selected_tournament['prize_money']} to the champion. The entrance cost of the tournament is {selected_tournament['fee']} and the travel expenses are {TRAVEL_FEE}.")

            user_input = input("Do you want to play the tournament? (Y/N) ").upper()
            while user_input not in ("N", "Y"):
                user_input = input("Invalid answer. Please answer 'Y' or 'N' ").upper()
            if user_input == "N":
                print("Ok. Please choose another from the list.")
                continue# we need to send the user back to the tournament selection screen
            elif user_input == "Y":
                print(f"Great! flying to {selected_tournament['country']} ...")
                player['money'] -= (selected_tournament['fee'] + TRAVEL_FEE) # [NEW] This subtracts the money!
                break# [NEW] Move the break HERE so the loop only ends on a "Y"

    current_tournament = selected_tournament

    # ----------- TOURNAMENT GAMEPLAY SECTION - here the player will play the tournament of the month

    input("The tournament is today! Press enter to start.")
    print(f"{'-'*80}")
    print(f"|          {current_tournament['name'].upper()}             |")
    print(f"{'-'*80}")

    def play_tournament(skill_points, tournament_diff_coef=None):
        tournament_result = random.randint(30,70) + (skill_points * 0.5)
        return tournament_result

    tournament_result = play_tournament(player['skill_points'])
    # tournament_result = 100
    print(f"\nTournament result: {tournament_result}")

    # Get tournament position
    # for position, data in reversed(POSITIONS.items()):
    #     if tournament_result >= data['min_score']:
    #         print(f"{position}")
    #         print(f"{data['reward_perc']} of PM & points")
    #         current_tournament['position'] = position
    #         current_tournament['reward_perc'] = data['reward_perc']
    #         break

    def get_tournament_position(tournament_res: int, asc_positions: dict):
        for position, data in reversed(asc_positions.items()):
            if tournament_res >= data['min_score']:
                return position, data['reward_perc']

    # print("get_tournament_position(tournament_result, reversed(POSITIONS))")
    # print(get_tournament_position(tournament_result, POSITIONS))
    current_tournament['position'], current_tournament['reward_perc'] = get_tournament_position(tournament_result, POSITIONS)

    # Get tournament history (using tournament position)
    t_rounds = list(POSITIONS.keys())
    history = []
    for round in t_rounds:
        if round == current_tournament['position'] and current_tournament['position'] != 'Champion':
            history.append((round, 'Lost'))
            # print(f'{round}... you lost!')
            break
        history.append((round, 'Win'))
        # print(f'{round}... you win!')
        # if round == current_tournament['position']:
        #     history.append((round, 'Champion'))
            # print(f'You won the tournament, congratulations {round}!!!')

    # print(history)

    # User interface - displays the progress of the tournament
    for i, (round, result) in enumerate(history):
        if result == 'Win':
            if round != 'Champion':
                print(f"Playing {round}... you {result}!")
                print(f"Current points: . Current money: ")
                if i < len(history) - 1:
                    input("--> Press enter to play the next round.")
            else:
                print(f'You won the tournament, congratulations {round}!!!')
    earned_money = current_tournament["prize_money"] * current_tournament["reward_perc"]
    earned_points = current_tournament["points"] * current_tournament["reward_perc"]

    print(f'You have made it to the {current_tournament["position"]}, that rewards you with {earned_points} points and ${earned_money}')


# Game 1, QF... you win!    -- QF gives 20% of points and money
# ready for the next game? Press enter to start

# Game 2, SF... you win!    -- SF gives 50% of points and money
# Game 3, F...  you win!   -- F gives 70% of points and money
#  Champion                 -- Champion gives 100% of points and money
# Congratulations! you are the new champion of Brisbane International [t_name]. Earned points: 250 [earned_points: t_points * position]


# ----------- PLAYER STATE UPDATE SECTION - here the attributes of the player will be updated and displayed

# New ranking: 210 [pl_ranking]
# Money: 129000 [pl_money]
# Total earned points: 250 [pl_points]
# You are doing a great job! Keep it up!

    # [NEW] CALCULATE WINNINGS
    earned_money = current_tournament["prize_money"] * current_tournament["reward_perc"]
    earned_points = current_tournament["points"] * current_tournament["reward_perc"]

    # [NEW] UPDATE PLAYER STATE
    player['money'] += earned_money
    if 'total_points' not in player: player['total_points'] = 0
    player['total_points'] += earned_points

    # [NEW] RECALCULATE RANKING (6 points = 1 rank climb)
    # Starting rank 250. Every 6 points subtracts 1 from the rank.
    player['rank'] = max(1, 250 - int(player['total_points'] // 6))

    print(f"\nYou finished at {current_tournament['position']}!")
    print(f"Earned: ${earned_money} | Total Money: ${player['money']}")
    print(f"Current Rank: {player['rank']} (Total Points: {player['total_points']})")
    input("\nPress Enter to proceed to the next month...")

# ... game continues looping every month the same, if you run out of money, you will loose the game. Quit()
#
# ----------- GAME CONCLUSION SECTION
# When 12 months have passed the game is over. It will report the game state.
# Game state:
# Ranking:
# Earned money:
# Total earned points:
# If final ranking is 1, player wins the game. If final ranking is not 1 but money is enough to keep playing and save the player's family, the program celebrates it, and thanks for helping the tennis player to achieve the dream.
# ----------- GAME CONCLUSION SECTION -----------
print("\n" + "="*40)
print("SEASON OVER")
print(f"Final Ranking: {player['rank']}")
print(f"Total Money: ${player['money']}")
if player['rank'] == 1:
    print("CONGRATULATIONS! You are the World Number 1!")
else:
    print(f"You finished the season at Rank {player['rank']}. Your family is proud of you.")

