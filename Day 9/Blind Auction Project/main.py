import art
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# Bids Dictionary will contain a Key "Name" and Value $$$$ from user input
bids = {}

#helper function to determine winner
def calculate_winner(bid_dictionary):
    highest_bidder = ""
    highest_amount = 0
    for bidder in bid_dictionary:
        if bid_dictionary[bidder] > highest_amount:
            highest_amount = bid_dictionary[bidder]
            highest_bidder = bidder
    print(f"{highest_bidder} has won the auction with a ${highest_amount} bid! Congratulations")

# Main Program Loop
print(art.logo)
while True:
    #Ask for Bidders Name and store value in variable
    name = input("Please enter your name for the bid: ")
    #Ask for their bid and store value in variable
    bid_amount = int(input("Please enter you bid amount:$"))
    #Add the new bid to bids dictionary
    bids[name] = bid_amount
    #Ask if there are other bidders
    more_bidders = input("Are there more bidders? Please type 'yes' or 'no': ").lower() == "yes"
    #If no, calculate winner and break loop
    if not more_bidders:
        calculate_winner(bids)
        break
    #clear terminal for next bidder
    print('\n' * 100)

