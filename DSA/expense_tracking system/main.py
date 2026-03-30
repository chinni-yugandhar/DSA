#file handing expense tracking system
expenses = []
def export_expenses(expenses):
    with open ("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(expense["name"]+ " " + expense["amount"] + "\n")
def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Export Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter expense name: ")
            amount = input("Enter expense amount: ")
            expenses.append({"name": name, "amount": amount})
        elif choice == "2":
            for expense in expenses:
                print(expense["name"] + ": " + expense["amount"])
        elif choice == "3":
            export_expenses(expenses)
            print("Expenses exported to expenses.txt")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
main()            
