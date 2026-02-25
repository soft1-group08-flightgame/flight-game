# 1. import
#
# 2. connection
#
# 3. functions
# get airports for each tournament (large_airports that match the country/city)
# play_tournament(skill_points, tc_id)
#
# 4. variables
#
# 5. game

# ---- Tennis Pro 2026 ----
# Intro: Hi! Welcome to Tennis Pro 2026. ...
# Enter your name:
# Enter your nationality:
# Enter age:

# game story. You got the chance to play in a tournament as a guest and your performance draws the attention of the ATP directors, they offer you to enter in the professional circuit in the 250th position of the world ranking. you inherited this much money and a racquet. Do your best to climb all the way up to the top!

# December is starting. The following tournaments are coming up in, choose one of them:
# 1. Brisbane International [t_name]
# 2. Hong Kong Open [t_name]

# user chooses 1 (program checks if pl_money enough for expenses(tournament_fee and travel cost))
#  Brisbane International [t_name] is played in [t_city], [t_country]. It's a ATP250 [tc_id] tournament that gives 250[tc_points] points and 129000[t_money] to the champion. The entrance cost of the tournament is [tc_entry_fee] and the travel expenses are [travel_cost, this variable should be constant at the beginning].
# do you want to play this tournament? Yes/ No    -- no, takes you back to tournament options.
# user answers YES
# Flying to [t_country]...
# The tournament is today! Press enter to start.
# Brisbane International tournament starting!
# [play tournament(skill_points, tc_id)]
# Game 1, QF... you win!    -- QF gives 20% of points and money
# Game 2, SF... you win!    -- SF gives 50% of points and money
# Game 3, F...  you win!   -- F gives 70% of points and money
#  Champion                 -- Champion gives 100% of points and money
# Congratulations! you are the new champion of Brisbane International [t_name]. Earned points: 250 [earned_points: t_points * position]
# New ranking: 210 [pl_ranking]
# Money: 129000 [pl_money]
# Total earned points: 250 [pl_points]
# You are doing a great job! Keep it up!

# January([months[1]]) is now starting. The following tournaments are coming up in, choose one of them:
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


