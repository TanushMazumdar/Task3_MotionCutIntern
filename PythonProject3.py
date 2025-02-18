import os
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.txt"

# Function to load expenses from file
def load_expenses():
    expenses = []
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as file:
            for line in file:
                date, amount, category, description = line.strip().split("|")
                expenses.append({
                    "date": date,
                    "amount": float(amount),
                    "category": category,
                    "description": description
                })
    return expenses

# Function to save expense to file
def save_expense(expense):
    with open(EXPENSE_FILE, "a") as file:
        file.write(f"{expense['date']}|{expense['amount']}|{expense['category']}|{expense['description']}\n")

# Function to add a new expense
def add_expense():
    try:
        amount = float(input("Enter the amount spent: "))
        category = input("Enter the category (e.g., food, transport, entertainment, other): ").lower()
        description = input("Enter a brief description: ")
        date = datetime.now().strftime("%Y-%m-%d")

        expense = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        save_expense(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

# Function to view all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for expense in expenses:
        print(f"Date: {expense['date']}, Amount: ₹{expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
    print("\n")

# Function to view expense summary by month
def monthly_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for expense in expenses:
        month = expense['date'][:7]  # YYYY-MM format
        summary[month] = summary.get(month, 0) + expense['amount']

    print("\n--- Monthly Summary ---")
    for month, total in summary.items():
        print(f"{month}: ₹{total:.2f}")
    print("\n")

# Function to view expense summary by category
def category_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for expense in expenses:
        category = expense['category']
        summary[category] = summary.get(category, 0) + expense['amount']

    print("\n--- Category-wise Summary ---")
    for category, total in summary.items():
        print(f"{category.capitalize()}: ₹{total:.2f}")
    print("\n")

# Main function to run the expense tracker
def expense_tracker():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Expense Summary")
        print("4. Category-wise Expense Summary")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            category_summary()
        elif choice == '5':
            print("Exiting... Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    expense_tracker()
