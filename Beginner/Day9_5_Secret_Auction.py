from Day9_art import logo
# from replit import clear

print(logo)

all_bids = {}
auction_end = False

def highest_bidder(bidder):
	winner = ""
	highest_bid = 0
	for bids in bidder:
		if highest_bid > bids:
			highest_bid = bids
			winner = bidder
	print(f"The highest bid is {highest_bid}")

while not auction_end:
	name = input("What is your name?\n")
	bid = int(input("What is your bid price?\n"))
	all_bids[name] = bid
	other_bids = input("Are there other users who want to bid? Type 'Yes' or 'No'\n").lower()
	if other_bids == "no":
		auction_end = True
		highest_bidder(all_bids)
