# 21/9/2020, Blue, Nicolas Keck, This program runs a text-based storefront for vacuum cleaners
# Extension: Program takes part in dishonest business practice and will raise the prices of cheaper vacuums to be closer
# to the maximum price. I have basically turned this vacuum store into a commercial airline. 
from copy import deepcopy

# Arrays are pre-sorted to make working with them easier
costs = [37, 48, 60, 75, 83, 92, 130]
models = ["CheapMaster™ 1200", "Handheld-Roomba", "SuperSuck™ 1060", "VacPack™", "Good'Nuff™",
          "Suction Specialists Select™ 2", "Supremo Mk. XV 2300-Enhanced Edition™"]
features = ["Very cheap, comes with a plethora of spare parts. 2-day warranty, warranty void if spare parts utilized.",
            "Very high-quality vacuum, but difficult to use. Best way we've found is to push it around on the floor, "
            "would work wonders with some wheels.",
            "Middle of the line-quality vacuum, performs as well as you'd expect for its price-range.",
            "Incredible suction power for the price paid, very bulky and exceptionally LOUD however.",
            "'Nuff said",
            "Our own Suction Specialists™ brand vacuum, performs at least 2% better than most name brands!",
            "For the true suction fanatics out there, this vacuum is a cut above the rest. Twin-nozzle suction power,\n"
            "Turbo-mode for sucking up the toughest dust, quantum dust bag which can go 100 years without emptying, and"
            "\na clean silver finish, this vacuum is the best of the best made for the best of the rest."]

# Program takes input of customer name and max price
customer = input("Welcome valued customer! Please input customer name: ")
print(f"Welcome back to the Suction Specialists Suction Selector™, {customer}!")
cash = float(input("Please input your budget for today: ").strip("$"))

# Sorts through costs and adds ones which could be within an increased budget to revised costs.
# Also removes any costs which are above even a revised budget. It's inconvenient to keep the
# revised costs in costs, but I still need to reference relevant model and features as well.
revised_costs = []
remove_list = []
for a in range(len(costs)):
    if costs[a] > round(cash*1.1):
        remove_list.append(a)
    elif costs[a] > cash:
        revised_costs.append(costs[a])
for a in reversed(remove_list):
    costs.remove(costs[a])
    models.remove(models[a])
    features.remove(features[a])

# "Revises" prices so that the customer pays more than they should. Basically checks the budget and
# then shifts prices up to be closer to that budget.
for cost in reversed(costs):
    if cost not in revised_costs:
        adjustment = (round(cash)-5) - cost
        if adjustment < 0:
            adjustment = 0
        break
for a in range(len(costs)):
    if costs[a] not in revised_costs:
        costs[a] += adjustment
    else:
        costs[a] = round(cash*1.1)

# This changes the revised cost so it is exactly 10% higher than the customer's budget. Since there will only every be
# one of these values, I could just use the first reference in the array, but sometimes it's empty. It's also done
# above to keep values consistent.
for a in range(len(revised_costs)):
    revised_costs[a] = round(cash*1.1)

# Now we continue with the actually interface itself
if costs:
    outstring = ""
    outstring += f"Here are the models we found within your budget of ${'{:.2f}'.format(cash)}:\n"
    revised_costs_index = 0
    for a in range(len(costs)):
        if costs[a] not in revised_costs:
            outstring += f"{a+1}: ${round(costs[a]-0.01, 2)} {models[a]}\n"
        else:
            revised_costs_index = a
    if revised_costs == costs:
        outstring = "Sorry, but none of our stock is within your budget."
        outstring += f"\nHowever, if you are willing to pay ${round(revised_costs[0] - cash, 2)} more, " \
                     f"you could get:\n"
        outstring += f"The {models[revised_costs_index]} at ${'{:.2f}'.format(revised_costs[0])}!\n"
    elif revised_costs:
        outstring += f"\nAdditionally, if you are willing to pay ${round(revised_costs[0]-cash, 2)} more, " \
                     f"you could also get:\n"
        outstring += f"The {models[revised_costs_index]} at ${'{:.2f}'.format(revised_costs[0])}!\n"

    # Until a purchase is made, the interface continues looping
    purchase = None
    while purchase !=  "Y":
        print(outstring)
        if revised_costs:
            selection = int(input("Type in the number of a product to learn more/purchase(0 for "
                                  "the over-budget product): "))
        else:
            selection = int(input("Type in the number of a product to learn more/purchase: "))
        if selection == 0:
            print(f"{models[revised_costs_index]}: {features[revised_costs_index]}")
        else:
            print(f"{models[selection-1]}: {features[selection-1]}")
        purchase = input("Would you like to purchase this product?(Y/N)")
else:
    print("Sorry, but there is nothing in our store that would fit your budget")

# This creates the receipt
if costs:
    outstring = "Thank you for shopping at Suction Specialists™!\n-------------\n"
    outstring += f"Customer name: {customer}\n-------------\n"
    if selection == 0:
        outstring += f"Model name: {models[revised_costs_index]}\n"
        outstring += f"Cost: ${'{:.2f}'.format(revised_costs[0])}"
    else:
        outstring += f"Model name: {models[selection-1]}\n"
        outstring += f"Cost: ${round(costs[selection-1]-0.01, 2)}"
    print(outstring)
else:
    print("Please leave, browsing is not permitted unless there is intent to purchase")
