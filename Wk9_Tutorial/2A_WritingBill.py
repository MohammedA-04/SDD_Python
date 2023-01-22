# 2A Write you've finished eating at a restaurant and received this bill

"""
Cost of meal: £44.50
Restaurant tax: 6.75%
Tip: 15%
- Apply the tip to the overall cost of the meal
"""

Meal = 44.50
Tax = 6.75 / 100
Variable_Tax = Tax
Tip = 15.0 / 100

Meal = Meal + Meal*Tax
Total =  Meal + Meal*Tip
print("Your Meal was = £%.2f" %Total )

# NB = %.2f is 2 Decimal Point Formatter
