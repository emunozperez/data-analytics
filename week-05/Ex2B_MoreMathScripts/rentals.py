# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay). How many vans do you need? How
# much will it cost to rent vans? What is the cost if you split it per person?

people = int(input("Enter the number of people going on the tour: "))
vans_needed = (people + 14) // 15  # Round up to the nearest whole number of vans
total_cost = vans_needed * 250
cost_per_person = total_cost / people if people > 0 else 0
print(f"You will need {vans_needed} vans.")
print(f"The total cost to rent the vans is: ${total_cost:.2f}.")
print(f"The cost per person is: ${cost_per_person:.2f}.")