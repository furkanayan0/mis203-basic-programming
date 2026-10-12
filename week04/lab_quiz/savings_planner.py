# lab04_savings_planner.py

# 1. Input Validation using while loops
while True:
    balance = float(input("Enter starting balance: "))
    if balance >= 0:
        break
    print("Error: Starting balance cannot be negative.")

while True:
    deposit = float(input("Enter monthly deposit: "))
    if deposit > 0:
        break
    print("Error: Monthly deposit must be positive.")

while True:
    rate = float(input("Enter monthly interest rate (%): "))
    if rate >= 0:
        break
    print("Error: Interest rate cannot be negative.")

while True:
    goal = float(input("Enter savings goal: "))
    if goal > 0:
        break
    print("Error: Savings goal must be positive.")

# 2. Simulation Logic
total_interest = 0.0
months = 0

# Check if the starting balance already meets the goal
if balance >= goal:
    print(f"\nGoal already reached! 0 months.")
    print(f"Final balance: {balance:.2f}")
    print(f"Total interest earned: 0.00")
else:
    print(f"\n{'Month':<10} | {'Interest':<10} | {'Balance':<10}")
    print("-" * 35)

    # Loop up to 60 months
    for month in range(1, 61):
        # Calculate monthly interest and update totals
        interest = balance * (rate / 100)
        total_interest += interest
        balance += interest + deposit
        months = month

        # Print monthly row
        print(f"{month:<10} | {interest:<10.2f} | {balance:<10.2f}")

        # Break early if goal is reached
        if balance >= goal:
            break

    # 3. Final Output
    if balance >= goal:
        print(f"\nGoal reached in {months} months!")
    else:
        print(f"\nGoal NOT reached after 60 months.")
        
    print(f"Final balance: {balance:.2f}")
    print(f"Total interest earned: {total_interest:.2f}")
