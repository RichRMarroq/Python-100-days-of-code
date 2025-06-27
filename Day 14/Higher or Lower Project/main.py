import art
import random
import os
from game_data import data

#Global Variables
score = 0

def pick_person():
    """Picks a random person from the game data"""
    return data[random.randint(0,len(data)-1)]

def display_persons():
    """Displays the current person_a and person_b details to choose"""
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
    print(art.vs)
    print(f"Compare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")

def check_input(choice):
    """Checks which person has the higher follower count based on user choice"""
    person_a_selected = False
    person_b_selected = False
    if choice.upper() == "A":
        person_a_selected = True
    elif choice.upper() == "B":
        person_b_selected = True
    return (person_a_selected and (person_a['follower_count'] > person_b['follower_count'])) or (person_b_selected and (person_b['follower_count'] > person_a['follower_count']))


#Build main game loop
winning = True
person_a = pick_person()
person_b = pick_person()
while winning:
    print(art.logo)
    if score > 0:
        print(f"You guessed correctly! Your Score: {score}") #Print the score after the first turn if they guessed correctly
    display_persons()
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if check_input(choice):
        if choice.upper() == "B":
            person_a = person_b
        person_b = pick_person()
        score += 1
        
    else:
        winning = False
    os.system('cls||clear')

print(f"Sorry, you guessed incorrectly. Your score: {score}")