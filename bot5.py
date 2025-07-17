from static_q_table import Q_TABLE  # just a normal Python import
import random

ACTIONS = ["hit", "stand"]

def bot5_decision(features):
    state = (features["player_total"], features["dealer_card"], features["is_soft"])
    q_values = [(Q_TABLE.get((state, a), 0), a) for a in ACTIONS]
    max_q = max(q_values, key=lambda x: x[0])[0]
    best_actions = [a for q, a in q_values if q == max_q]
    return random.choice(best_actions)