account = 10000
interest_rate = 6.99
years_to_double = 72 / interest_rate
total = account * 2
print("Your current savings is " + str(account) + ".")
print("At an interest rate of " + str(interest_rate) + "%, it will take approximately " + str(round(years_to_double, 2)) + " years for your savings to double to " 
      + str(total) + ".")