import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = 21
terminate_game = False

while not terminate_game:
    first_action = input("Do you want to play a game of Blackjack (y/n) ? ")

    if first_action == "y":

        # VARIABLES
        my_card = []
        my_hand = 0
        my_score = 0
        my_ace = False

        computer_card = []
        computer_hand = 0
        computer_score = 0
        computer_ace = False
        game_ended = False

        # STARTING CARD
        for idx, i in enumerate(range(0, 2)):
            my_card.append(cards[random.randint(0, len(cards) - 1)])
            my_score = my_score + my_card[idx]

        for idx, j in enumerate(range(1)):
            computer_card.append(cards[random.randint(0, len(cards) - 1)])
            computer_score = computer_score + computer_card[idx]
        # GAME START

        my_hand = 1
        computer_hand = 0

        while not game_ended:

            print(art.logo)
            print(f"Your cards: {my_card}, current score: {my_score}")
            print(f"Computer cards: {computer_card}")
            decision = input("Do you want to take another card (y/n) ? ")

            if decision == "y":
                my_score = 0

                my_card.append(cards[random.randint(0, len(cards) - 1)])

                for index, i in enumerate(range(len(my_card))):
                    my_score = my_score + my_card[index]

                if my_score > blackjack:

                    for index, i in enumerate(range(len(my_card))):
                        if i == 11:
                            my_card[index] = 1
                            my_ace = True

                        if not my_ace:
                            game_ended = True
            else:
                while computer_score < blackjack and computer_score < my_score:
                    computer_score = 0

                    computer_card.append(cards[random.randint(0, len(cards) - 1)])

                    for index, i in enumerate(range(len(computer_card))):
                        computer_score = computer_score + computer_card[index]

                    if computer_score <= blackjack and (computer_score > my_score or computer_score == my_score):
                        game_ended = True

                    if computer_score > blackjack:

                        for index, i in enumerate(range(len(computer_card))):
                            if i == 11:
                                computer_card[index] = 1
                                computer_ace = True
                                for index, i in enumerate(range(len(computer_card))):
                                    computer_score = computer_score + computer_card[index]

                            if not computer_ace:
                                game_ended = True
        else:
            print(f"Your final hand {my_card}, final score: {my_score}")
            print(f"Computer final hand {computer_card}, final score: {computer_score}")

            if (my_score > computer_score and my_score <= 21) or (my_score < computer_score and computer_score > 21):
                print("You Won!")
            elif my_score == computer_score:
                print("The game ended with a Draw")
            else:
                print("You Lose!")
    else:
        terminate_game = True

print("\n" * 50)
print("Thank you for playing.")