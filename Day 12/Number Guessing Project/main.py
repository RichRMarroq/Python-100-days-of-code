from art import logo
import random
#Guess the number program
#Display the text
#Ask what difficulty 'easy' or 'hard'
#Easy gets 10 guesses and hard gets 5 guesses
#Generate a random number between 1-100
#Ask user to guess number and display if it is too low or too high
#loop for number from difficulty

#Global variables to hold difficulty
EASY = 5
HARD = 10
NUMBER = random.randint(1,100)

def play_game(easy_or_hard):
    guesses = EASY if easy_or_hard == 'easy' else HARD
    for _ in range(guesses):
        print(f'You have {guesses} guesses remaining!')
        player_guess = int(input('Make your guess: '))
        if player_guess < NUMBER:
            print('Too Low')
        elif player_guess > NUMBER:
            print('Too High')
        elif player_guess == NUMBER:
            print(f'You got it! The number was {NUMBER}')
            print('You win! Please re run the program to play again.')
            return
        guesses -= 1
    print('You have ran out of guesses please re run the program to try again')
    return

print(logo)
difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ")
play_game(difficulty)