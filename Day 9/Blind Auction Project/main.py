from art import logo

print(logo)

print("Welcome to the secret auction program.")

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bidder = max(bidding_record, key=bidding_record.get)
        winner = bidder
        highest_bid = bidding_record[bidder]
    print(f"The winner is {winner}. With a bid of ${highest_bid}.")

# TODO-4: Compare bids in dictionary
def find_the_highest_bidder(bidder_record):
    highest_bid = 0
    winner = ""
    for bidder in bidder_record:

        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The wim=nner is: {winner}. With a bid of ${highest_bid}.")

continue_bidding = True
bids = {}

while continue_bidding:
    # TODO-1: Ask the user for input
    name = input("What's your name?: ")
    bid =int(input("What's your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid
    # TODO-3: Whether if new bids need to be added
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_bidding == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif continue_bidding == "yes":
        print("\n" * 50)
