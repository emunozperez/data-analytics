# Federal taxes are 23% of your salary every month. You make X amount of money.
# How much is withheld for taxes?

salary = float(input("Enter your monthly salary: "))
taxes = salary * 0.23
print("The amount withheld for taxes is: " + str(taxes))

# Make sure not to display partial cents in your results! Experiment with using either the
# round() function or format() method to get results to display to two decimal places.

print("The amount withheld for taxes is: $" + format(taxes, ".2f"))