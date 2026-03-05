# get airports for each tournament (large_airports that match the country/city)
# play_tournament(skill_points, tc_id)

# Queries de Database using the db connection and the SQL query as parameters
def run_query(conn, query, params=None):
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_player_data(test_vals=None):
    data = test_vals or {
    'user_name': input("Enter your name:"),
    'nation': input("Enter your Nation"),
    'age': int(input("Enter your age"))
    }
    return data

def format_tournament(tournament_list):
    # Maps sql tournament data into dict variable
    return {
        "id":           tournament_list[0],
        "week":         tournament_list[1],
        "month":        tournament_list[2],
        "day":          tournament_list[3],
        "points":       tournament_list[4],
        "name":         tournament_list[5],
        "surface":      tournament_list[6],
        "city":         tournament_list[7],
        "iso_country":  tournament_list[8],
        "continent":    tournament_list[9],
        "prize_money":  tournament_list[10],
        "country":      tournament_list[11]
    }

def get_tournaments_of_the_month(conn,month):
    # Get tournament of the month
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

def add_tournament_fees(tournament_list, tournament_fee_rate):
    for t in tournament_list:
        t['fee'] = t['prize_money'] * tournament_fee_rate

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

def show_tournaments(t_list):
    # Display the list of tournaments
    for index, t in enumerate(t_list, start=1):
        print(f"{index}. {t['name']} ({t['iso_country']})")

def print_game_intro(user_name, nation, age, heritage):
    # Intro of the game
    print("=" * 40)
    print("{:^40}".format("🎾TENNIS PRO 2026🎾"))
    print("=" * 40, end="\n\n")
    print("🫵Complete a full tennis season and finish  ranked number one in the world ranking",end="\n\n")

    print("Winning tournaments grants ranking points and prize money. The accumulated points determine the player's ranking position", end="\n\n")
    print("=" * 40, end="\n\n")
    print(f"{user_name} was born in {nation} {age} years ago into a very poor family.\n"
    f"He was the youngest of six siblings.\n"
    f"Since childhood, he had to work in a coal mine to help his family survive.\n"
    f"One day, in the storage room of his house, he found an old tennis racket that had belonged to his father, a former amateur tennis player.\n"
    f"From that moment on, he decided to learn how to play tennis under his father's supervision.\n"
    f"{user_name} was very talented and grew up with a passion for tennis in his heart, playing and training at every free moment after work.\n"
    f"As time passed, he grew older, and so did his talent.\n"
    f"He married a wonderful woman, but he still didn’t manage to escape poverty.\n"
    f"One day, he received news that a distant aunt had died, leaving him an inheritance of {heritage} euros.\n"
    f"This was a small amount of money.\n"
    f"Unfortunately, it was not enough to change his economic situation, but it gave him temporary relief.\n"
    f"Randomly, fortune seemed to turn in his favor.\n"
    f"During a tennis match, he attracted the attention of a tennis scout, who invited him to substitute as a guest player in the World Tennis Championship after one of the players was injured.\n"
    f"{user_name} packed so the tennis racket that had belonged to his father and started his trip.\n"
    f"He decided to invest the money he had to join the world tennis circuit and become the best player in the world.")
