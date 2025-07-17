# Bot 2 decision logic
def bot2_decision(features):
    total = features["player_total"]
    is_soft = features["is_soft"]
    dealer_card = features["dealer_card"]

    if(total, is_soft) in total_based:
        return total_based[(total, is_soft)]
    
    return strategy_table.get((total, is_soft, dealer_card), "stand")

# (total, is_soft, dealer_card): action
strategy_table = {
    (18, True, 2): "stand",
    (18, True, 3): "stand",
    (18, True, 4): "stand",
    (18, True, 5): "stand",
    (18, True, 6): "stand",
    (18, True, 7): "stand",
    (18, True, 8): "stand",
    (18, True, 9): "hit",
    (18, True, 11): "hit",
    (18, True, 10): "hit",

    (16, False, 2): "stand",
    (16, False, 3): "stand",
    (16, False, 4): "stand",
    (16, False, 5): "stand",
    (16, False, 6): "stand",
    (16, False, 7): "hit",
    (16, False, 8): "hit",
    (16, False, 9): "hit",
    (16, False, 10): "hit",
    (16, False, 11): "hit",

    (15, False, 2): "stand",
    (15, False, 3): "stand",
    (15, False, 4): "stand",
    (15, False, 5): "stand",
    (15, False, 6): "stand",
    (15, False, 7): "hit",
    (15, False, 8): "hit",
    (15, False, 9): "hit",
    (15, False, 10): "hit",
    (15, False, 11): "hit",

    (14, False, 2): "stand",
    (14, False, 3): "stand",
    (14, False, 4): "stand",
    (14, False, 5): "stand",
    (14, False, 6): "stand",
    (14, False, 7): "hit",
    (14, False, 8): "hit",
    (14, False, 9): "hit",
    (14, False, 10): "hit",
    (14, False, 11): "hit",

    (13, False, 2): "stand",
    (13, False, 3): "stand",
    (13, False, 4): "stand",
    (13, False, 5): "stand",
    (13, False, 6): "stand",
    (13, False, 7): "hit",
    (13, False, 8): "hit",
    (13, False, 9): "hit",
    (13, False, 10): "hit",
    (13, False, 11): "hit",

    (12, False, 2): "hit",
    (12, False, 3): "hit",
    (12, False, 4): "stand",
    (12, False, 5): "stand",
    (12, False, 6): "stand",
    (12, False, 7): "hit",
    (12, False, 8): "hit",
    (12, False, 9): "hit",
    (12, False, 10): "hit",
    (12, False, 11): "hit",
}

total_based = {
    (20, True): "stand",
    (19, True): "stand",
    (17, True): "hit",
    (16, True): "hit",
    (15, True): "hit",
    (14, True): "hit",
    (13, True): "hit",
    (20, False): "stand",
    (19, False): "stand",
    (18, False): "stand",
    (17, False): "stand",
    (11, False): "hit",
    (10, False): "hit",
    (9, False): "hit",
    (8, False): "hit",
    (7, False): "hit",
    (6, False): "hit",
    (5, False): "hit",
}