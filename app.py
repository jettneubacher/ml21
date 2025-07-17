from flask import Flask, request, jsonify
from flask_cors import CORS

# returns features["player_total", "is_soft", "dealer_card"]
from utils import preprocess_input
# receives features, returns action
from bot2 import bot2_decision
from bot3 import bot3_decision
from bot5 import bot5_decision
#receives player_hand, dealer_card, num_simulations=100
# returns action
from bot4 import bot4_decision


app = Flask(__name__)

CORS(app)

def handle_bot_request(bot_function):
    data = request.json
    player_hand = data.get("player_hand")
    dealer_card = data.get("dealer_hand")

    if not player_hand or not dealer_card:
        return jsonify({"error": "Missing input"}), 400

    features = preprocess_input(player_hand, dealer_card)
    print(features)
    action = bot_function(features)
    return jsonify({"action": action})


# BOT 1
# hit on 16's regardless of what dealer is showing
# does not consider soft scores
@app.route('/bot1', methods=['POST'])
def bot1():
    print("SERVICING BOT 1")
    data = request.json
    player_hand = data.get("player_hand")  # e.g., ["8", "8"]
    dealer_card = data.get("dealer_hand")  # e.g., "10"
   
    print(f"received player hand: {player_hand}")
   
    processedInput = preprocess_input(player_hand, dealer_card)
    total = processedInput["player_total"]
    print(f"total: {total}")
    action = "hit" if total <= 16 else "stand"
    print(f"action: {action}")
    return jsonify({"action": action})

# BOT 2
# Searches a move table (pro-dataset)
@app.route('/bot2', methods=['POST'])
def bot2():
    print("SERVICING BOT 2")
    return handle_bot_request(bot2_decision)

# BOT 3
# Linear Classification (hard-coded)
@app.route('/bot3', methods=['POST'])
def bot3():
    print("SERVICING BOT 3")
    return handle_bot_request(bot3_decision)

# BOT 4
# Simulation 
# no input preprocessing needed, decision logic needs to know both player cards
@app.route('/bot4', methods=['POST'])
def bot4():
    print("SERVICING BOT 4")
    num_simulations = 5000
    data = request.json
    player_hand = data.get("player_hand")
    dealer_card = data.get("dealer_hand")

    if not player_hand or not dealer_card:
        return jsonify({"error": "Missing input"}), 400

    action = bot4_decision(player_hand.copy(), dealer_card, num_simulations)
    return jsonify({"action": action})

# BOT 5
# Q-learning
@app.route('/bot5', methods=['POST'])
def bot5():
    print("SERVICING BOT 5")
    return handle_bot_request(bot5_decision)

if __name__ == '__main__':
    app.run(debug=False)


