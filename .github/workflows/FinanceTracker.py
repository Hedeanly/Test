class ExpenseTracker:
    def __init__(self):
        self.expenses = []  # List to store expenses as tuples (name, amount)

    def add_expense(self, name, amount):
        """Adds a new expense."""
        try:
            amount = float(amount)
            if not name or amount <= 0:
                raise ValueError("Expense name must not be empty, and amount must be positive.")
            self.expenses.append((name, amount))
        except ValueError as e:
            raise ValueError("Invalid expense name or amount.") from e

    def get_expenses(self):
        """Returns the list of expenses."""
        return self.expenses

    def delete_expense(self, index):
        """Deletes an expense by its index."""
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
        else:
            raise IndexError("Invalid expense index.")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Add Expense
            name = input("Enter expense name: ").strip()
            amount = input("Enter expense amount: ").strip()
            try:
                tracker.add_expense(name, amount)
                print("Expense added successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            # View Expenses
            expenses = tracker.get_expenses()
            if expenses:
                print("\nExpenses:")
                for idx, (name, amount) in enumerate(expenses, start=1):
                    print(f"{idx}. {name}: ${amount:.2f}")
            else:
                print("No expenses found.")

        elif choice == "3":
            # Delete Expense
            expenses = tracker.get_expenses()
            if not expenses:
                print("No expenses to delete.")
                continue

            print("\nExpenses:")
            for idx, (name, amount) in enumerate(expenses, start=1):
                print(f"{idx}. {name}: ${amount:.2f}")

            try:
                index = int(input("Enter the expense number to delete: ")) - 1
                tracker.delete_expense(index)
                print("Expense deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")

        elif choice == "4":
            # Exit Program
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()
