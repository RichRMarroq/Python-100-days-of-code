from art import saw, died, logo
import random
#Set the deck of cards, each card will have an equal chance of being pulled
deck = {
    "A": [1, 11],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

def deal_card():
    """Helper function to randomly draw a single card from the deck. Returns a string (Card key)"""
    return random.choice(list(deck.keys()))

def calculate_score(player_hand: list, dealer: bool):
    """Helper function to calculate the score of a players/dealers hand.
    Dealer stands on soft 17
    Returns an int"""
    score = 0
    #Check for Aces
    hand_has_aces = True if "A" in player_hand else False
    if hand_has_aces:
        low_score, high_score = 0, 0 #Variables to hold score for different Ace values
        for card in player_hand:
            low_score += deck[card] if card != "A" else deck[card][0] #Aces counted as 1
            high_score += deck[card] if card != "A" else deck[card][1] #Aces counted as 11
        if dealer:
            if high_score >= 17 and high_score < 21:
                score = high_score #Dealer must stand on soft 17 (When aces counted as 11)
            else:
                score = low_score
        else:
            if high_score > 21:
                score = low_score #Player takes low score if high score goes past 21
            else:
                score = high_score #Player takes higher score if still in play as it is closest to 21
    else: #if no Aces, just count the card values
        for card in player_hand:
            score += deck[card]
    return score

def play_blackjack():
    """Main game function to handle logic for a game of Blackjack.
    Returns 'win', 'lose', and 'push' depending on outcome."""
    #Deal Player and Dealer hands
    players_hand = []
    dealers_hand = []
    for _ in range(2):
        players_hand.append(deal_card())
        dealers_hand.append(deal_card())

    #Calculate initial scores
    players_score = calculate_score(player_hand=players_hand, dealer=False)
    dealers_score = calculate_score(player_hand=dealers_hand, dealer=True)

    #Players Turn
    players_turn = True
    player_blackjack = False
    while players_turn:
        #Check for Blackjack!
        if players_score == 21 and len(players_hand) == 2:
            players_turn = False
            player_blackjack = True
            print(f"    Your cards: {players_hand} Blackjack! 21")
            continue #We continue to Dealer turn in case Dealer also has blackjack

        print(f"    Your cards: {players_hand}, current score: {players_score}")
        print(f"    Computer's first card: {dealers_hand[0]}")
        get_card = input("Press 'y' to get another card or 'n' to pass: ").lower() == 'y'
        if get_card:
            players_hand.append(deal_card()) # Deal the player a new card
            players_score = calculate_score(player_hand=players_hand, dealer=False)   # Calculate player new score
            if players_score < 21: #Check for win condition
                continue
            elif players_score == 21: #Player hit 21, skip turn
                players_turn = False
            else: #Player bust, dealer wins
                print(f"    Your final cards: {players_hand}, final score: {players_score}")
                print(f"    Computer's cards: {dealers_hand}, final score: {dealers_score}")
                return 'lose'
        else:
            players_turn = False

    #Dealers Turn
    dealers_turn = True
    while dealers_turn:
        # Check for Dealer Blackjack
        if len(dealers_hand) == 2 and dealers_score == 21:
            if player_blackjack: #Push if player also has Blackjack
                print(f"    Computer's cards: {dealers_hand}, Blackjack! 21")
                return 'push'
            else: #Only Dealer has Blackjack, dealer wins
                print(f"    Your final cards: {players_hand}, final score: {players_score}")
                print(f"    Computer's final cards: {dealers_hand}, Blackjack! 21")
                return 'lose'

        #Check for player Blackjack
        elif player_blackjack:
            print(f"    Computer's cards: {dealers_hand}, final score: {dealers_score}")
            return 'win'

        # Play Dealer turn
        elif dealers_score < 17: # Dealer takes a new card if current score < 17
            dealers_hand.append(deal_card())
            dealers_score = calculate_score(player_hand=dealers_hand, dealer=True)
            #Check for dealer bust
            if dealers_score < 17:
                continue
            elif dealers_score <= 21:
                dealers_turn = False
            else: #Dealer bust, player wins
                print(f"    Your final hand: {players_hand}, final score: {players_score}")
                print(f"    Computers final hand: {dealers_hand}, final score: {dealers_score}")
                return 'win'
        else:
            dealers_turn = False
    # Check final win condition
    if players_score == dealers_score:
        print(f"    Your final hand: {players_hand}, final score: {players_score}")
        print(f"    Computers final hand: {dealers_hand}, final score: {dealers_score}")
        return 'push'
    elif players_score < dealers_score:
        print(f"    Your final hand: {players_hand}, final score: {players_score}")
        print(f"    Computers final hand: {dealers_hand}, final score: {dealers_score}")
        return 'lose'
    else:
        print(f"    Your final hand: {players_hand}, final score: {players_score}")
        print(f"    Computers final hand: {dealers_hand}, final score: {dealers_score}")
        return 'win'

#Main Game Loop
wants_to_play = True
while wants_to_play:
    #print("\n" * 20)
    print(saw)
    wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y'
    if not wants_to_play:
        print(died)
        break
    #Play the game
    print("\n" * 20)
    print(logo)
    outcome = play_blackjack()
    if outcome == "win":
        print("You win!!")
    elif outcome == "push":
        print("You and dealer pushed, try again!")
    else:
        print("You lose :(")