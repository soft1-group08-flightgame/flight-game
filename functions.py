
# get airports for each tournament (large_airports that match the country/city)
# play_tournament(skill_points, tc_id)

# Queries de Database using the db connection and the SQL query as parameters
def run_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# print(run_query(connection, "SELECT * FROM tournaments WHERE name LIKE '%tralia%'"))

# Intro of the game
def print_game_intro(user_name, nation, age, heritage):
    print("---------TENNIS PRO 2026---------")
    print("Complete a full tennis season and finish  ranked number one in the world ranking")

    print("Winning tournaments grants ranking points and prize money. The accumulated points determine the player's ranking position")

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
