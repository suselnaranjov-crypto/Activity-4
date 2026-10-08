# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: Susel Naranjo Vega
# Date: October 7th, 2026

# SCENARIO
# You are wanting to save money for a particular purchase.
# Write a program that estimates how long it will take to grow your money to your desired amount.
# Consider 


# TODO 1: Create inputs for the following information 
#         - Your desired savings goal
#         - The amount of money as your base investment
#         - The annual interest rate
#         - The amount of money you want to deposit into the account every month (if any)
savings_goal = float(input("Enter your savings goal: $"))
base_investment = float(input("Enter your starting investment: $"))
annual_interest_rate = float(input("Enter the annual interest rate (%): ")) / 100
monthly_deposit = float(input("Enter your monthly deposit: $"))
# TODO 2: Create variables to hold number of months and current balance of the account
months = 0
current_balance = base_investment
# TODO 3: Create a loop that will run until you have made at least your desired savings goal
while current_balance < savings_goal:
    # TODO 4: Calculate amount of money earned that month through interest on your base investment and monthly deposit
    monthly_interest = current_balance * (annual_interest_rate / 12)
    current_balance = current_balance + monthly_interest + monthly_deposit
    # TODO 5: Increment the number of times the loop has run so you can track how many months it takes to hit your goal
    months = months + 1
# TODO 6:  Print how long it will take for your investment to mature.  
#          If the duration is longer than 12 months, print your result in years.  Otherwise, print the result in months.
if months > 12:
    years = months / 12
    print(f"Number of Months: {months}")
    print(f"Number of Years: {years:.2f}")
else:
    print(f"Number of Months: {months}")

print(f"Total Investment: ${current_balance:,.2f}")

# EXPECTED OUTPUT
# GOAL: $1,000,000
# INTEREST: 4%
# BASE: $1,000
# MONTHLY DEPOSIT: $100
#
# Number of Months: 177
# Number of Years: 87.75
# Total Investment: $1,034,906.36

