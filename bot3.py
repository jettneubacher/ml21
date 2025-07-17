# Bot 3 decision logic
def bot3_decision(features):
    total = features["player_total"]
    is_soft = features["is_soft"]
    dealer = features["dealer_card"]

    weights = {
        "total": 1.449,
        "soft_mod": -6.875,
        "dealer": -0.564,
        "bias": -14.379
    }

    score = (
        weights["total"] * total +
        (weights["soft_mod"] if is_soft else -weights["soft_mod"]) +
        weights["dealer"] * dealer +
        weights["bias"]
    )
    return "stand" if score >= 0 else "hit"


