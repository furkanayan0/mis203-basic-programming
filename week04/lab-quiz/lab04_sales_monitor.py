def main():
    target = float(input("Enter the daily sales target: "))

    total_sales = 0.0
    days_meeting_target = 0
    highest_sale = -1.0 
    highest_day = 0

    for day in range(1, 8):
        
        while True:
            sale = float(input(f"Enter sales for day {day}: "))
            if sale < 0:
                print("Sales cannot be negative. Please enter a valid amount.")
            else:
                break

        total_sales += sale

      
        if sale >= target:
            days_meeting_target += 1

        
        if sale > highest_sale:
            highest_sale = sale
            highest_day = day

    average_sales = total_sales / 7

    print("\n--- Weekly Sales Summary ---")
    print(f"Total sales: {total_sales:.2f}")
    print(f"Average daily sales: {average_sales:.2f}")
    print(f"Number of days meeting the target: {days_meeting_target}")
    print(f"Highest sale: {highest_sale:.2f} on day {highest_day}")

if __name__ == "__main__":
    main()
