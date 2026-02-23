def main():
    print("Hi there, Welcome to your Personal Financial Assistant!")
    
    # 1 Budget Initialization
    while True:
        try:
            budget = float(input("Enter your budget for this period: "))
            if budget < 0:
                print("Budget must be a non-negative value. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    expenses = []
    total_spent = 0.0
    
    print("\n--- Transaction Logging ---")
    print("Enter your expenses. Type 'done' when finished.\n")
    
    # 2 Transactional Logging 
    while True:
        description = input("Enter expense description (or 'done' to finish): ")
        if description.lower() == "done":
            break
        # Validate description: must contain letters and spaces only, and cannot be empty
        cleaned_description = description.strip()
        if not cleaned_description or any(char.isdigit() for char in cleaned_description) or not all(
            char.isalpha() or char.isspace() for char in cleaned_description
        ):
            print("Description must contain letters and spaces only. please try again.")
            continue
        
        try:
            amount = float(input("Enter your expense amount: "))
            if amount < 0:
                print("Expense cannot be a negative figure. Try again.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        
        expenses.append((description, amount))
        total_spent += amount
        
        # 3 Real-time Fiscal Oversight
        if total_spent > budget:
            print(" Warning: You have exceeded your budget!")
        else:
            print(f"Remaining balance: {budget - total_spent:.2f}")
    
    # 4 Final Financial Summary
    print("\n--- Financial Summary ---")
    print(f"Initial Budget: {budget:.2f}")
    print(f"Total Expenses: {total_spent:.2f}")
    
    if total_spent > budget:
        print(f"Deficit: {total_spent - budget:.2f}")
    else:
        print(f"Remaining Balance: {budget - total_spent:.2f}")
    
    print("\nTransaction Log:")
    for i, (desc, amt) in enumerate(expenses, start=1):
        print(f"{i}. {desc} - {amt:.2f}")


if __name__ == "__main__":
    main()
