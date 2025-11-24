ncome = 0
expense = 0

while True:
    print("\n--- Personal Finance Manager ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = float(input("Enter income amount: "))
        income += amt
        print("Income added!")

    elif choice == "2":
        amt = float(input("Enter expense amount: "))
        expense += amt
        print("Expense added!")

    elif choice == "3":
        balance = income - expense
        print("\n---- Summary ----")
        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Balance:", balance)

    elif choice == "4":
        print("Exiting... Goodbye!")
        break
