coins = [['$100 bills', 10000], ['$50 bills', 5000], ['$10 bills', 1000], ['$5 bills', 500], ['$1 bills', 100], ['Quarters', 25], ['Dimes', 10], ['Nickels', 5], ['Pennies', 1]]

def calculate_coins(cents):
    for name, val in coins:
        num_coins = cents // val
        print(f'{num_coins} {name}')
        cents %= val


while (True):
    try:
        cents = input('Please enter number of cents to make change from: ')
        cents = int(cents)
        if cents < 0:
            print("Exiting.")
            break
        calculate_coins(cents)

    except:
        print("Input not valid. Please enter a valid integer")