import random
from ui_colors import G,R,Y,C,B,W # These are ANSI escape codes used to change terminal text colors for better UX


# 1. run_query: The Database Engine
# This handles the communication between Python and MariaDB.
# It takes a "query" (the question) and "params" (the specific details) to get data.
def run_query(conn, query, params=None):
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result


# 2. get_player_data: The Identity Creator
# Collects user input to build the player's profile (Name, Country, Age).
def get_player_data(test_vals=None):
    data = test_vals or {
        'user_name': input("👤 Enter your name: "),
        'nation': input("🌍 Enter your Nation: "),
        'age': int(input("🎂 Enter your age: "))
    }
    return data


# 3. format_tournament: The Data Translator
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


# 4. get_tournaments_of_the_month: The Calendar Filter
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


# 5. add_tournament_fees: The Financial Calculator
# Calculates the entry fee for each tournament (2% of the prize money).
def add_tournament_fees(tournament_list, tournament_fee_rate):
    for t in tournament_list:
        t['fee'] = round(t['prize_money'] * tournament_fee_rate, 2)


# 6. add_tournament_categories_and_difficulty: The Difficulty Scaler
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


# 7. show_tournaments: The User Menu
# Iterates through the list and prints a numbered menu for the player to choose from.
def show_tournaments(t_list):
    for index, t in enumerate(t_list, start=1):
        print(f"{index}. {t['name']} ({t['iso_country']})")


# 8. play_tournament: The Match Simulator
# Combines Skill and Randomness (Luck), then divides by difficulty to get a score.
def play_tournament(skill_points, tournament_diff_coef):
    base_result = (random.randint(30, 70) + (skill_points * 0.5))
    tournament_result = base_result / tournament_diff_coef
    return tournament_result


# 9. get_tournament_position: The Result Decider
# Compares the match score against the POSITIONS dictionary to see how far you got.
def get_tournament_position(tournament_res: int, asc_positions: dict):
    for position, data in reversed(asc_positions.items()):
        if tournament_res >= data['min_score']:
            return position, data['reward_perc']


# 10. print_game_intro: The Storyteller
def print_game_intro(user_name, nation, age, heritage):
    print(f"{C}" + "=" * 40 + f"{W}")
    print(f"{B}{Y}" + "{:^40}".format(
        "🎾 TENNIS PRO 2026 🎾") + f"{W}")
    print(f"{C}" + "=" * 40 + f"{W}\n")

    print(
        f"🫵  {B}Complete a full tennis season{W} and finish ranked {G}number one{W} in the world ranking.",
        end="\n\n")

    print(
        f"Winning tournaments grants {Y}ranking points{W} and {G}prize money{W}. The accumulated points determine the player's ranking position.",
        end="\n\n")
    print(f"{C}" + "=" * 40 + f"{W}\n")

    print(
        f"{user_name} was born in {B}{nation}{W} {age} years ago into a very {R}poor family{W}. 🏚️\n"
        f"He was the youngest of six siblings.\n"
        f"Since childhood, he had to work in a {B}coal mine{W} to help his family survive. ⚒️\n"
        f"One day, in the storage room of his house, he found an {Y}old tennis racket{W} that had belonged to his father, a former amateur tennis player.\n"
        f"From that moment on, he decided to learn how to play tennis under his father's supervision. 🎾\n"
        f"{user_name} was very talented and grew up with a {R}passion for tennis{W} in his heart, playing and training at every free moment after work.\n"
        f"As time passed, he grew older, and so did his talent.\n"
        f"He married a wonderful woman, but he still didn’t manage to escape {R}poverty{W}.\n"
        f"One day, he received news that a distant aunt had died, leaving him an {G}inheritance of {heritage} euros{W}. 💶\n"
        f"This was a small amount of money.\n"
        f"Unfortunately, it was not enough to change his economic situation, but it gave him temporary relief.\n"
        f"Randomly, {Y}fortune{W} seemed to turn in his favor. 🍀\n"
        f"During a tennis match, he attracted the attention of a {B}tennis scout{W}, who invited him to substitute as a guest player in the World Tennis Championship after one of the players was injured.\n"
        f"{user_name} packed so the {Y}tennis racket{W} that had belonged to his father and started his {B}trip{W}. ✈️\n"
        f"He decided to {G}invest the money{W} he had to join the world tennis circuit and {B}become the best player in the world{W}. 👑")