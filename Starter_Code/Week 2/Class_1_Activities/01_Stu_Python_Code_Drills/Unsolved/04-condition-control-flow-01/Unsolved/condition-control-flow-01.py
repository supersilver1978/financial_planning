
# Declare a variable budget and assign it a value of 5000.
budget = 5000

# Declare a variable rent_cost and assign it a value of 1500.
rent_cost = 1500

# Declare a variable utilities_cost and assign it a value of 150.
utilities_cost = 150

# Declare a variable food_cost and assign it a value of 250.
food_cost = 250

# Declare a variable transportation_cost and assign it a value of 350.
transportation_cost = 350

# Declare a variable computer_cost and assign it a value of 2000.
computer_cost = 2000

# Declare a variable called total_cost that takes the sum of all costs above (excluding budget).
total_costs = rent_cost + utilities_cost + food_cost + transportation_cost + computer_cost
print(total_costs)
total_list = [rent_cost, utilities_cost, food_cost, transportation_cost, computer_cost]
total_cost2 = sum(total_list)
print(total_list)

# Write an if statement that checks w hether the sum of all our costs i within the budget.
# If so, print "You're total cost is " concatenated with the `total_cost` variable.
# Else, print "You're over budget by " concatenated with the difference between `budget` and `total_cost`.

if total_costs <= budget:
    print("Your total cost is ", total_costs)

# Write an if statement that checks whether the rent_cost is larger than the sum of the `utilities_cost`, `food_cost`,
# and `transportation_cost`. If so, print a string that says "The rent is too darn high!".
# Else, print a string that says "Ahhh just right!"
# YOUR CODE HERE!
