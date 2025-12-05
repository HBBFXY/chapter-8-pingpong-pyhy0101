import random
def simulate_one_game(p_A):
    score_A = 0
    score_B = 0
    while True:
        r = random.random()
        if r &lt; p_A:
            score_A += 1
        else:
            score_B += 1
        if (score_A &gt;= 11 and score_A - score_B &gt;= 2) or (score_B &gt;= 11 and score_B - score_A &gt;= 2):
            break
        if score_A == 10 and score_B == 10:
            while True:
                r = random.random()
                if r &lt; p_A:
                    score_A += 1
                else:
                    score_B += 1
                if abs(score_A - score_B) &gt;= 2:
                    break
    return score_A &gt; score_B

def simulate_match(p_A, num_games):
    wins_A = 0
    wins_B = 0
    while wins_A &lt; (num_games + 1) // 2 and wins_B &lt; (num_games + 1) // 2:
        if simulate_one_game(p_A):
            wins_A += 1
        else:
            wins_B += 1
    return wins_A &gt; wins_B

N = 1000
p_A = 0.6
num_games = 5
wins_A_count = 0
for _ in range(N):
    if simulate_match(p_A, num_games):
        wins_A_count += 1
P_A = wins_A_count / N
print(f"选手A的获胜概率: {P_A}")
