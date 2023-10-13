
import random

# symbolic constants
STARTING_CASH = 100
DAYS_IN_GAME = 10
NUMBER_OF_STOCKS = 8

# initialize game variables
stock_names = []
share_prices = [0] * NUMBER_OF_STOCKS
shares_owned = [0] * NUMBER_OF_STOCKS
cash = STARTING_CASH

# generate stock names
while len(stock_names) < NUMBER_OF_STOCKS:
    ticker_length = random.randint(3,5)
    new_ticker = ""
    for i in range(ticker_length):
        new_letter = chr(random.randint(ord("A"),ord("Z")))
        new_ticker += new_letter
    if not new_ticker in stock_names:
        stock_names.append(new_ticker)

for day in range(DAYS_IN_GAME):

    for i in range(len(share_prices)):
        share_prices[i] = random.randint(1,6)+random.randint(1,6)

    while True:

        # status update
        print(f"*****Day {day+1}*****")
        for i in range(NUMBER_OF_STOCKS):
            print(f"{stock_names[i]}: ${share_prices[i]} ({shares_owned[i]} owned)")
        print(f"Cash on hand: ${cash}")
        print()

        # input
        print("Enter your transaction or nothing to end day.")
        print("Example: BUY 50 FOO")
        user_input = input("> ").upper()
        tokens = user_input.split()
        # no input -> end day
        if len(tokens) == 0:
            break
        # invalid input: <> 3 tokens
        elif len(tokens) != 3:
            print("Invalid transaction!")
        # invalid input: not buy or sell
        elif tokens[0] != "BUY" and tokens[0] != "SELL":
            print(f"Invalid transaction type {tokens[0]}, please BUY or SELL!")
        # invalid input: negative quantity
        elif int(tokens[1]) < 0:
            print("Negative transactions not allowed!")
        # invalid input: stock doesn't exist
        elif not tokens[2] in stock_names:
            print(f"Invalid stock name {tokens[2]}!")
        # valid input
        else:
            transaction_type = tokens[0]
            transaction_qty = int(tokens[1])
            stock_index = stock_names.index(tokens[2])
            if transaction_type == "BUY":
                trns_cost = transaction_qty * share_prices[stock_index]
                # can't afford purchase
                if trns_cost > cash:
                    print(f"Can't afford {transaction_qty} shares of {stock_names[stock_index]}!")
                    print(f"(Would cost ${trns_cost}, only have ${cash}!")
                else:
                    cash -= trns_cost
                    shares_owned[stock_index] += transaction_qty
            elif transaction_type == "SELL":
                # don't have enough to sell
                if shares_owned[stock_index] < transaction_qty:
                    print(f"Can't sell {transaction_qty} shares of {stock_names[stock_index]}!")
                    print(f"Only have {shares_owned[stock_index]} shares!")
                else:
                    shares_owned[stock_index] -= transaction_qty
                    cash += transaction_qty * share_prices[stock_index]

print("Game over!")
for i in range(len(share_prices)):
    share_prices[i] = random.randint(1,6)+random.randint(1,6)
final_score = -STARTING_CASH
for i in range(NUMBER_OF_STOCKS):
    print(f"Owned {shares_owned[i]} shares of {stock_names[i]} @ ${share_prices[i]}")
    final_score += shares_owned[i] * share_prices[i]
print(f"Final cash: ${cash}")
final_score += cash
print(f"Final score: {final_score}")

            
