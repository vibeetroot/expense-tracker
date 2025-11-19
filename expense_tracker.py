
file_name = "expenses.txt"

def add_expense():
    try:
        amount = float(input("Enter expense amount: ₹"))
        category = input("Enter category: ")

        with open(file_name, "a") as file:
            file.write(f"{amount},{category}\n")
        print("Expense added successfully!\n")

    except ValueError:
        print("Invalid input! Please enter a numeric amount.\n")


def view_expenses():
    print("\nAll Expenses: ")
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No expenses recorded yet!")
            else:
                for line in lines:
                    amount, category = line.strip().split(",")
                    print(f"₹{amount}  -  {category}")
    except FileNotFoundError:
        print("No expenses recorded yet!")
    print()


def total_spent():
    total = 0
    try:
        with open(file_name, "r") as file:
            for line in file:
                amount, _ = line.strip().split(",")
                total += float(amount)
        print(f"\nTotal Spent: ₹{total}\n")
    except FileNotFoundError:
        print("\nNo expenses to calculate!\n")


def main():
    while True:
        print("    Expense Tracker    ")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-4.\n")

if __name__ == "__main__":
    main()




