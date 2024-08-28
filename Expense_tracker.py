import csv
from datetime import datetime


def add_expense():
    date = input("Enter date (MM-DD-YYYY): ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    print("Expense added succesfully!")


def view_expenses():
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\nExpenses:")
            for row in reader:
                date, description, amount = row
                print(f"{date} | {description} | ${amount}")
    except FileNotFoundError:
        print("No expense found. Please add an expense first.")


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Exit")
        choice = input("Choose an option: ")


        if choice =='1':
            add_expense()
        elif choice =='2':
            view_expenses()
        elif choice =='3':
            break
        else:
            print("Invalid Choice. Please Try Again.")

if __name__ == "__main__":
    main()


