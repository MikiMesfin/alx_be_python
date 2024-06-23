# Defining variables
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

#Calculate monthly income
monthly_savings = monthly_income - monthly_expenses

# Simple annual interest of 5%
annual_interest_rate = 0.05

#calculating projected savings
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * annual_interest_rate)

#Printing
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
