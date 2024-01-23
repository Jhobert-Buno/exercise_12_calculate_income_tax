# Exercise 12: Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000     0
# Next $10,000	    10
# The remaining	    20

#functions
def income_tax(income):
    #first 10,000
    if income <= 10000:
        tax = 0

    #next 10000
    elif income <= 20000:
        tax = (income - 10000) * 10/100

    #remaining
    else:
        tax = 10000 * 10/100 + (income-20000) * 20/100

    return tax
    