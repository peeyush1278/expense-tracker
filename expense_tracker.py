import datetime
import json

# Define file to store data
data_file = "expenses.json"

# Load existing data or create a new file
def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to the file
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Add a new expense entry
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., food, transportation, entertainment): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    
    data = load_data()
    data.append(expense)
    save_data(data)
    print("Expense added successfully!")

# View expenses by month
def view_monthly_summary():
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")
    
    data = load_data()
    monthly_expenses = [expense for expense in data if expense["date"].startswith(f"{year}-{month}")]
    total = sum(expense["amount"] for expense in monthly_expenses)
    
    print(f"\nExpenses for {year}-{month}:")
    for expense in monthly_expenses:
        print(f"{expense['date']} - {expense['category']}: ${expense['amount']} ({expense['description']})")
    print(f"Total: ${total}")

# View expenses by category
def view_category_summary():
    category = input("Enter category to view summary: ")
    
    data = load_data()
    category_expenses = [expense for expense in data if expense["category"].lower() == category.lower()]
    total = sum(expense["amount"] for expense in category_expenses)
    
    print(f"\nExpenses in category '{category}':")
    for expense in category_expenses:
        print(f"{expense['date']} - {expense['category']}: ${expense['amount']} ({expense['description']})")
    print(f"Total in '{category}': ${total}")

# Main user interface
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category Summary")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                add_expense()
            except ValueError:
                print("Error: Invalid input for amount.")
        elif choice == "2":
            view_monthly_summary()
        elif choice == "3":
            view_category_summary()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()