expenses = []
total_expenses = 0
categories = []

def add_expense(expense, amount, category):
    global total_expenses
    expenses.append({"expense": expense, "amount": amount, "category": category})
    total_expenses += amount
    if category not in categories:
        categories.append(category)


def view_expenses():
    if len(expenses) == 0:
        print("No expenses added yet.")
        return
    print("\n--- Expenses ---")
    print("Expense Name:\tAmount:\tCategory:")
    i = 1
    for expense in expenses:
        print(i, ". ", expense["expense"], "\t\t", expense["amount"], "\t", expense["category"])
        i += 1

def view_category_summary():
    if len(expenses) == 0:
        print("No expenses added yet.")
        return
    for category in categories:
        TotalExpByCat = 0
        for expense in expenses:
            if expense["category"] == category:
                TotalExpByCat += expense["amount"]
        print(category, ":", TotalExpByCat)


def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. View Category Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            expense = input("Enter Expense Name: ")
            amount = float(input("Enter Amount: "))
            category = input("Enter Category: ")
            add_expense(expense, amount, category)
            print("Expense added successfully!")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("\nTotal Expenses: $", total_expenses)
        elif choice == "4":
            print("\n--- Category Summary ---")
            view_category_summary()
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu() 
