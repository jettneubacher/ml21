def preprocess_input(player_hand, dealer_card):
    total = 0
    aces = 0
    for card in player_hand:
        if card == "11" or card == 11:
            aces += 1
        else:
            total += int(card)
    
    is_soft = False
    if aces > 0:
        # Treat one ace as 11 initially
        if total + 11 <= 21:
            total += 11
            is_soft = True
        else:
            total += aces  # All aces as 1

    intTotal = int(total)
    intDealer_card = int(dealer_card)

    return {
        "player_total": intTotal,
        "is_soft": is_soft,
        "dealer_card": intDealer_card
    }
