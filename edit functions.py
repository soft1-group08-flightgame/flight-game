import random


# 1. [NEW] run_query: The Database Engine
# This handles the communication between Python and MySQL.
# It takes a "query" (the question) and "params" (the specific details) to get data.
def run_query(conn, query, params=None):
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result


# 2. [NEW] get_player_data: The Identity Creator
# Collects user input to build the player's profile (Name, Country, Age).
def get_player_data(test_vals=None):
    data = test_vals or {
        'user_name': input("👤 Enter your name: "),
        'nation': input("🌍 Enter your Nation: "),
        'age': int(input("🎂 Enter your age: "))
    }
    return data


# 3. [NEW] format_tournament: The Data Translator
# SQL returns data as a list (Row). This function maps that list into a
# Dictionary (Key: Value) so the code is easier to read (e.g., t['name'] vs t[5]).
def format_tournament(tournament_list):
    return {
        "id": tournament_list[0],
        "week": tournament_list[1],
        "month": tournament_list[2],
        "day": tournament_list[3],
        "points": tournament_list[4],
        "name": tournament_list[5],
        "surface": tournament_list[6],
        "city": tournament_list[7],
        "iso_country": tournament_list[8],
        "continent": tournament_list[9],
        "prize_money": tournament_list[10],
        "country": tournament_list[11]
    }


# 4. [NEW] get_tournaments_of_the_month: The Calendar Filter
# Uses an SQL INNER JOIN to find tournaments that happen in a specific month.
def get_tournaments_of_the_month(conn, month):
    sql = f"""select tournaments.*, country.name 
                     from tournaments
                     inner join country on tournaments.iso_country = country.iso_country where tournaments.month = %s;"""
    raw_list = run_query(conn, sql, (month,))
    clean_list = []
    if raw_list:
        for t in raw_list:
            t_dict = format_tournament(t)
            clean_list.append(t_dict)
    return clean_list


# 5. [NEW] add_tournament_fees: The Financial Calculator
# Calculates the entry fee for each tournament (2% of the prize money).
def add_tournament_fees(tournament_list, tournament_fee_rate):
    for t in tournament_list:
        t['fee'] = round(t['prize_money'] * tournament_fee_rate, 2)


# 6. [NEW] add_tournament_categories_and_difficulty: The Difficulty Scaler
# Assigns difficulty multipliers (diff_coef). Higher points = Harder matches.
def add_tournament_categories_and_difficulty(tournament_list):
    for t in tournament_list:
        if t['points'] == 250:
            t['category'] = 'ATP250'
            t['diff_coef'] = 1.0
        elif t['points'] == 500:
            t['category'] = 'ATP500'
            t['diff_coef'] = 1.15
        elif t['points'] == 1000:
            t['category'] = 'M1000'
            t['diff_coef'] = 1.25
        elif t['points'] == 2000:
            t['category'] = 'GS'
            t['diff_coef'] = 1.4


# 7. [NEW] show_tournaments: The User Menu
# Iterates through the list and prints a numbered menu for the player to choose from.
def show_tournaments(t_list):
    for index, t in enumerate(t_list, start=1):
        print(f"{index}. {t['name']} ({t['iso_country']})")


# 8. [NEW] play_tournament: The Match Simulator
# Combines Skill and Randomness (Luck), then divides by difficulty to get a score.
def play_tournament(skill_points, tournament_diff_coef):
    base_result = (random.randint(30, 70) + (skill_points * 0.5))
    tournament_result = base_result / tournament_diff_coef
    return tournament_result


# 9. [NEW] get_tournament_position: The Result Decider
# Compares the match score against the POSITIONS dictionary to see how far you got.
def get_tournament_position(tournament_res: int, asc_positions: dict):
    for position, data in reversed(asc_positions.items()):
        if tournament_res >= data['min_score']:
            return position, data['reward_perc']


# 10. [NEW] print_game_intro: The Storyteller
# Improved with ANSI colors and emojis for better human engagement.
def print_game_intro(user_name, nation, age, heritage):
    # UI Colors
    G = "\033[92m"  # Green
    C = "\033[96m"  # Cyan
    Y = "\033[93m"  # Yellow
    B = "\033[1m"  # Bold
    W = "\033[0m"  # Reset

    print(f"{C}{'=' * 50}{W}")
    print(f"{B}{Y}{'🎾 TENNIS PRO 2026 🎾':^50}{W}")
    print(f"{C}{'=' * 50}{W}\n")

    print(f"{B}🎯 MISSION:{W} Finish the season ranked {G}#1{W} in the world!")
    print(f"💰 Win tournaments to earn {G}Prize Money{W} and {Y}Ranking Points{W}.\n")

    print(f"{C}{'-' * 50}{W}")
    print(f"{B}📖 THE STORY OF {user_name.upper()}{W}")
    print(f"{C}{'-' * 50}{W}")

    print(f"Born in {B}{nation}{W}, {age} years ago, you grew up in a humble coal-mining family. ⚒️")
    print(f"In a dusty storage room, you found your father's old, weathered racket... 🎾")
    print(f"You trained in every free moment, driven by a passion that poverty couldn't kill.")

    print(f"\nSuddenly, a miracle: An inheritance of {G}{heritage} euros{W} arrives! 💶")
    print(f"It's not enough to retire, but it's enough to {B}DREAM{W}.")

    print(f"\nA scout spotted your talent and invited you to the World Circuit. ✈️")
    print(f"With your father's racket in hand and your savings in your pocket,")
    print(f"it is time to prove you are the {B}{Y}BEST IN THE WORLD.{W}\n")
    print(f"{C}{'=' * 50}{W}")
    input(f"\n{B}Press Enter to start your journey...{W}")