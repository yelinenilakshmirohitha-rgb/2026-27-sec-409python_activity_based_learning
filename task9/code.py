# Multi-Currency Travel Budget Analysis

exchange_rate = float(input("Enter exchange rate: "))
expense = float(input("Enter travel expense in foreign currency: "))
fee = float(input("Enter conversion fee: "))
budget = float(input("Enter total budget in rupees: "))

converted_amount = expense * exchange_rate
total_expense = converted_amount + fee

print("Converted Amount:", converted_amount)
print("Total Expense:", total_expense)

if total_expense <= budget:
    print("Within Budget")
else:
    print("Budget Exceeded")
