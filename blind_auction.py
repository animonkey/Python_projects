
#To store bids
bids = {

}


want_bid = True

while want_bid:
    name = input("What is your name?: \n")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid

    other_players = input("Any other bidders? Type 'yes' or 'no': ").lower()

    if other_players == 'no':
        want_bid = False
    else:
        #To clear screen
        print("\n" * 100)
greatest = 0
winner = ""
for x in bids:
    bid_amount = bids[x]
    if bid_amount > greatest:
        greatest = bid_amount
        winner = x

        
print(f"The winner is {winner} with a bidding amount ${bid_amount}")

