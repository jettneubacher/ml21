import random

# num_simulations is how many times bot will test each action
def bot4_decision(player_hand, dealer_card, num_simulations=500):
    safe_hits, stand_win = simulate_action(player_hand, dealer_card, num_simulations)
    return "hit" if safe_hits >= stand_win else "stand"


def simulate_action(player_hand, dealer_card, num_simulations=500):

    safe_hits, stand_wins = 0, 0

    for _ in range(num_simulations):
        result = simulate_game(player_hand.copy(), dealer_card, "hit")
        if result == 1:
            safe_hits += 1
    for _ in range(num_simulations):
        result = simulate_game(player_hand.copy(), dealer_card, "stand")
        if result == 1:
            stand_wins += 1
    safe_hit_rate = safe_hits / num_simulations
    stand_win_rate = stand_wins / num_simulations
    #print(f"HIT win rate: {hit_win_rate:.2f}, STAND win rate: {stand_win_rate:.2f}")
    return safe_hit_rate, stand_win_rate

def simulate_game(hand, dealer, action):
    # create deck
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    known_cards = hand + [dealer]
    for card in known_cards:
        deck.remove(card)

    random.shuffle(deck) #CHECK

    # actions
    if action == "hit":
        hand.append(deck.pop())
    # if stand do nothing        

    # dealer turn
    dealer_hand = [dealer, deck.pop()]
    while dealer_should_hit(dealer_hand):
        dealer_hand.append(deck.pop())

    # check winner
    player_score, _ = hand_value(hand)
    dealer_score, _ = hand_value(dealer_hand)

    if action == "hit":
        if player_score <= 21:
            return 1
        else:
            return 0
    else:
        if dealer_score > 21:
            return 1
        elif player_score > dealer_score:
            return 1
        elif player_score < dealer_score:
            return 0
        else:
            return 0
    
def hand_value(hand):
    total = sum(hand)
    aces = hand.count(11)
    is_soft = False

    while total > 21 and aces:
        total -= 10
        aces -= 1

    if 11 in hand and total <= 21:
        is_soft = True

    return total, is_soft

def dealer_should_hit(hand):
    score, is_soft = hand_value(hand)
    return score < 17 or (score == 17 and is_soft)