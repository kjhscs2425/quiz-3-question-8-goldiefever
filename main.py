import json

# read `expenses.json`
with open ("expenses.json", "r") as f:
    stores_and_prices = json.load(f)

username = input("What is your name?")

# get and print total "price" for all expenses at the "pet store"
def expenses_per_store(store):
    expenses = 0
    for key in stores_and_prices:
        if key == store:
            for item in range(len(((stores_and_prices[store])))):
                expenses += stores_and_prices[store][item]["price"]
        else:
            pass

    print(f"You have spent ${expenses} at the {store}")
    if expenses >= 100:
        print("Time to start saving ... 😥")
    else:
        print(f"Wow {username}, you are a good saver! 💰💰💰 Go buy yourself a little treat")

expenses_per_store(input("Which store would you like to check your expenses at?\nThe options are pet store, grocery store, and office supply store.\n"))

