# 1. IMPORT SECTION
# Bringing in external modules to extend Python's functionality
import random  # Used to generate random match results
import sys  # Used for sys.exit() to close the game on "Game Over"
import functions as f  # Importing your custom helper functions (database calls, UI, etc.)
import config  # Importing sensitive database credentials
import mysql.connector  # Driver to connect and interact with your MySQL database

# --- COLORS & EMOJIS FOR UI ---
# These are ANSI escape codes used to change terminal text colors for better UX
G = "\033[92m"  # Green: Successful events or earning money
R = "\033[91m"  # Red: Negative events, costs, or losing matches
C = "\033[96m"  # Cyan: Headers and section titles
B = "\033[1m"  # Bold: For emphasizing important text
W = "\033[0m"  # Reset: Reverts text back to the standard white color

# 2. DATABASE CONNECTION
# Establishing a live link to the MySQL server using settings from config.py
connection = mysql.connector.connect(
    host=config.HOST,
    port=config.PORT,
    database=config.DB,
    user=config.USER,
    password=config.PASS,
    autocommit=True  # Ensures every SQL change is saved instantly
)

# 4. INITIAL VARIABLES & GAME STATE
heritage = 50000  # The starting bank balance for the player
skill_points = 20  # Initial player strength; used in the match result formula
player = f.get_player_data()  # Triggers the player creation process/inputs

# Adding gameplay-specific keys to the player dictionary
player['money'] = heritage
player['skill_points'] = skill_points
player['rank'] = 250  # Starting professional ranking

# GAME CONDITIONS & REWARDS
# POSITIONS dictionary defines the "Score" needed to reach a certain round and the prize percentage
POSITIONS = {
    'Quarter Finals': {'min_score': 0, 'reward_perc': 0.35},
    'Semi Finals': {'min_score': 35, 'reward_perc': 0.50},
    'Finals': {'min_score': 60, 'reward_perc': 0.70},
    'Champion': {'min_score': 80, 'reward_perc': 1.00}
}
TOURNAMENT_FEE_RATE = 0.02  # Logic: Fee is 2% of the total prize money
TRAVEL_FEE = 5000  # Fixed cost to fly to any tournament location

# CONTEXT VARIABLES
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December")

# 5. GAME START
# Displaying the "Welcome" screen with the player's initial stats
f.print_game_intro(player['user_name'], player['nation'], player['age'], heritage)

# --- 2. THE MAIN SEASON LOOP ---
# The heart of the game: This iterates through all 12 months of the year
for month in MONTHS:
    print(f"\n{B}{C}📅 --- {month.upper()} ---{W}")

    # FETCH DATA: Querying the database for tournaments specifically in this month
    t_list = f.get_tournaments_of_the_month(connection, month)

    # DATA ENRICHMENT: Adding fees and difficulty levels to the tournament list
    f.add_tournament_fees(t_list, TOURNAMENT_FEE_RATE)
    f.add_tournament_categories_and_difficulty(t_list)

    # BANKRUPTCY CHECK (Losing Condition)
    # If the player has less money than the cheapest tournament + travel, the game ends
    t_fees = [t['fee'] for t in t_list]
    if player['money'] < min(t_fees) + TRAVEL_FEE:
        print(f"\n{R}❌ Oh no! You don't have enough money to continue playing.{W}")
        print(f"{B}Game Over.{W}")
        sys.exit()  # Ends the script execution

    # TOURNAMENT SELECTION LOOP
    # This keeps running until the player makes a valid, affordable choice and confirms it
    while True:
        f.show_tournaments(t_list)  # Displays available tournaments to the user

        # INPUT VALIDATION: Ensuring the user enters a number that exists in the list
        while True:
            user_input = input(f"{B}🎾 Select tournament #: {W}")
            if user_input.isnumeric():
                user_input_num = int(user_input)
                if 1 <= user_input_num <= len(t_list):
                    selected_tournament = t_list[user_input_num - 1]
                    break
                else:
                    print(f"{R}Please enter a number between 1 and {len(t_list)}{W}")
            else:
                print(f"{R}Error: Please enter a numeric value.{W}")

        # AFFORDABILITY CHECK
        if player['money'] < (selected_tournament['fee']) + TRAVEL_FEE:
            print(f"{R}💸 Not enough money. Please pick a cheaper tournament.{W}")
            continue  # Restarts the selection loop

        else:
            # Displaying cost summary to the user
            print(f"\n{B}{selected_tournament['name']}{W} in {selected_tournament['city']}.")
            print(f"💰 Champion Prize: {G}${selected_tournament['prize_money']:.2f}{W}")
            print(f"💳 Total Cost: {R}-${selected_tournament['fee'] + TRAVEL_FEE:.2f}{W} (Fee + ✈️ Travel)")

            # CONFIRMATION: Allowing the user to change their mind before spending money
            user_input = input(f"\n{B}Do you want to play? (Y/N): {W}").upper()
            while user_input not in ("N", "Y"):
                user_input = input(f"{R}Invalid input. Enter 'Y' or 'N': {W}").upper()

            if user_input == "N":
                print("Returning to the list...")
                continue
            elif user_input == "Y":
                print(f"{G}Great! Flying to {selected_tournament['country']}...{W}")
                player['money'] -= (selected_tournament['fee'] + TRAVEL_FEE)  # Deduction
                break  # Exit the selection loop to start the match

    current_tournament = selected_tournament

    # ----------- TOURNAMENT GAMEPLAY SECTION -----------
    input(f"\n{B}Match day! Press enter to start...{W}")

    # TOURNAMENT BOX: Visual decoration for the tournament name
    print(f"\n {C}{'-' * 20}{'-' * len(current_tournament['name'].upper())}{W}")
    print(f"{B}|          {current_tournament['name'].upper()}          |{W}")
    print(f" {C}{'-' * 20}{'-' * len(current_tournament['name'].upper())}{W}")


    # SIMULATION LOGIC: Calculating how well the player did based on skill and tournament difficulty
    def play_tournament(skill_points, tournament_diff_coef):
        # Result = (Random Luck + Skill) adjusted by Difficulty Coefficient
        base_result = (random.randint(30, 70) + (skill_points * 0.5))
        tournament_result = base_result / tournament_diff_coef
        return tournament_result


    tournament_result = play_tournament(player['skill_points'], current_tournament['diff_coef'])


    # POSITION CALCULATION: Checking where the result fits in the POSITIONS dictionary
    def get_tournament_position(tournament_res: int, asc_positions: dict):
        for position, data in reversed(asc_positions.items()):
            if tournament_res >= data['min_score']:
                return position, data['reward_perc']


    current_tournament['position'], current_tournament['reward_perc'] = get_tournament_position(tournament_result,
                                                                                                POSITIONS)

    # TOURNAMENT HISTORY: Creating a chronological list of rounds played (Wins vs Loss)
    t_rounds = list(POSITIONS.keys())
    history = []
    for round in t_rounds:
        if round == current_tournament['position'] and current_tournament['position'] != 'Champion':
            history.append((round, f'{R}Lost ❌{W}'))
            break  # Stop once the loss is recorded
        history.append((round, f'{G}Win! ✅{W}'))

    # USER INTERFACE: Animating the tournament progress
    for i, (round, result) in enumerate(history):
        print(f"🔹 Playing {round}... you {result}!")
        if 'Win' in result:
            if round == 'Champion':
                print(f"{G}{B}🏆 CONGRATULATIONS! You won the tournament!{W}")
            elif i < len(history) - 1:
                input(f"{C}   --> Next Round Ready. Press enter...{W}")

    # CALCULATE REWARDS: Points and money earned are a percentage of the max prize
    earned_money = current_tournament["prize_money"] * current_tournament["reward_perc"]
    earned_points = current_tournament["points"] * current_tournament["reward_perc"]

    # ----------- PLAYER STATE UPDATE SECTION -----------
    # Persisting the monthly winnings into the player's profile
    player['money'] += earned_money
    if 'total_points' not in player: player['total_points'] = 0
    player['total_points'] += earned_points

    # RANKING CALCULATION: (Every 20 points earned improves rank by 1 spot)
    player['rank'] = max(1, 250 - int(player['total_points'] // 20))

    # MONTHLY SUMMARY UI
    print(f"\n{B}{C}📊 MONTHLY SUMMARY{W}")
    print(f"Final Position: {current_tournament['position']}")
    print(f"Earnings: {G}+${earned_money:.2f}{W} 💰 | New Balance: ${player['money']:.2f}")
    print(f"Updated Rank: {B}#{player['rank']}{W} 📈 (Points: {player['total_points']:.2f})")

    # LOOP CONTROL: Choosing the right prompt based on whether it is the last month
    if month != 'December':
        input(f"\nPress Enter to proceed to {MONTHS[MONTHS.index(month) + 1]}...")
    else:
        input(f"\nSeason Complete! Press Enter for final results...")

# ----------- GAME CONCLUSION SECTION -----------
# Triggered once the 12-month loop finishes
print(f"\n{B}{C}{'=' * 40}{W}")
print(f"{B}🏁 SEASON OVER - FINAL RESULTS{W}")
print(f"Final Ranking: {B}#{player['rank']}{W}")
print(f"Final Wealth: {G}${player['money']:.2f}{W}")

# VICTORY CONDITION: If the player reached #1
if player['rank'] == 1:
    print(f"{G}{B}👑 CONGRATULATIONS! You are the World Number 1! 👑{W}")
else:
    print(f"The season is done. Your family is proud of you! ❤️")