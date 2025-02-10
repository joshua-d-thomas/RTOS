def atm_simulation():
    # Welcome Message
    print("Welcome to the ATM Simulation Program!")
    
    # Account Balance Initialization
    account_balance = 1000
    pin = 1234
    max_attempts = 3
    
    # PIN Verification
    for attempt in range(max_attempts):
        try:
            entered_pin = int(input("Enter your 4-digit PIN: "))
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        if entered_pin == pin:
            print("PIN verified successfully!")
            break
        else:
            print(f"Incorrect PIN. {max_attempts - attempt - 1} attempts remaining.")
    else:
        print("Too many incorrect attempts. Exiting program.")
        return
    
    # Main Menu
    while True:
        print("\nMain Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        try:
            choice = int(input("Select an option (1-4): "))
        except ValueError:
            print("Invalid input. Please select a valid option.")
            continue
        
        # Check Balance
        if choice == 1:
            print(f"Your current account balance is: ${account_balance:.2f}")
        
        # Deposit Money
        elif choice == 2:
            try:
                deposit_amount = float(input("Enter the amount to deposit: "))
                if deposit_amount > 0:
                    account_balance += deposit_amount
                    print(f"${deposit_amount:.2f} has been deposited. New balance: ${account_balance:.2f}")
                else:
                    print("Invalid amount. Deposit amount must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        
        # Withdraw Money
        elif choice == 3:
            try:
                withdrawal_amount = float(input("Enter the amount to withdraw: "))
                if withdrawal_amount > 0:
                    if withdrawal_amount <= account_balance:
                        account_balance -= withdrawal_amount
                        print(f"${withdrawal_amount:.2f} has been withdrawn. New balance: ${account_balance:.2f}")
                    else:
                        print("Insufficient balance. Transaction denied.")
                else:
                    print("Invalid amount. Withdrawal amount must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        
        # Exit
        elif choice == 4:
            print("Thank you for using this ATM. Goodbye!")
            break
        
        # Invalid Option
        else:
            print("Invalid option. Please select a valid choice (1-4).")


# Run the program
atm_simulation()
