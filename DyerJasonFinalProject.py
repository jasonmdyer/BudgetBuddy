# DyerJasonFinalProject.py
# Purpose: BudgetBuddy application for managing income and expenses using a Tkinter GUI

import tkinter as tk
from tkinter import messagebox

# Validation Module
# Purpose: Handles input validation for BudgetBuddy
def validate_input(amount, category):
    # Purpose: Validate transaction inputs, return error message if invalid
    if not amount:
        return "Amount cannot be empty."
    if not category:
        return "Category cannot be empty."
    try:
        amount = float(amount)  # Convert amount to float
        if amount <= 0:
            return "Amount must be positive."
    except ValueError:
        return "Amount must be a valid number."
    return None  # No errors

# Logic Module
# Purpose: Manages transaction storage and calculations for BudgetBuddy
class BudgetLogic:
    def __init__(self):
        # Purpose: Initialize an empty list to store transactions
        self.transactions = []  # List of dictionaries: {type, amount, category, description}

    def add_transaction(self, trans_type, amount, category, description):
        # Purpose: Add a transaction to the list
        transaction = {
            "type": trans_type,  # Income or Expense
            "amount": amount,  # Transaction amount
            "category": category,  # Transaction category
            "description": description  # Optional description
        }
        self.transactions.append(transaction)

    def get_transactions(self):
        # Purpose: Return the list of transactions
        return self.transactions

    def calculate_summary(self):
        # Purpose: Calculate total income and expenses
        income = sum(trans["amount"] for trans in self.transactions if trans["type"] == "Income")
        expenses = sum(trans["amount"] for trans in self.transactions if trans["type"] == "Expense")
        return income, expenses

# GUI Module
# Purpose: Defines the Tkinter GUI for BudgetBuddy, including main and secondary windows
class BudgetBuddyGUI:
    def __init__(self, root):
        # Purpose: Initialize the main window and set up the application
        self.root = root  # Main Tkinter window
        self.root.title("BudgetBuddy")  # Window title
        self.root.geometry("400x300")  # Window size
        self.logic = BudgetLogic()  # Initialize logic for calculations
        self.create_main_window()  # Create the main dashboard

    def create_main_window(self):
        # Purpose: Create the main dashboard window with summary and navigation
        self.clear_window()  # Remove existing widgets

        # Labels for financial summary
        self.income_label = tk.Label(self.root, text="Total Income: $0.00")  # Display total income
        self.income_label.pack(pady=10)
        self.expense_label = tk.Label(self.root, text="Total Expenses: $0.00")  # Display total expenses
        self.expense_label.pack(pady=10)
        self.balance_label = tk.Label(self.root, text="Balance: $0.00")  # Display remaining balance
        self.balance_label.pack(pady=10)

        # Buttons with callbacks
        tk.Button(self.root, text="Add Transaction", command=self.open_transaction_window).pack(pady=5)
        tk.Button(self.root, text="View Transactions", command=self.view_transactions).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.exit_app).pack(pady=5)

        self.update_summary()  # Update financial summary

    def clear_window(self):
        # Purpose: Clear all widgets from the current window
        for widget in self.root.winfo_children():
            widget.destroy()

    def open_transaction_window(self):
        # Purpose: Open the secondary window for adding transactions
        self.clear_window()
        self.root.geometry("400x400")  # Adjust window size for form

        tk.Label(self.root, text="Add Transaction").pack(pady=10)

        # Transaction type dropdown
        tk.Label(self.root, text="Type:").pack()
        self.transaction_type = tk.StringVar(value="Income")  # Dropdown selection for transaction type
        tk.OptionMenu(self.root, self.transaction_type, "Income", "Expense").pack()

        # Amount entry
        tk.Label(self.root, text="Amount:").pack()
        self.amount_entry = tk.Entry(self.root)  # Entry field for amount
        self.amount_entry.pack()

        # Category entry
        tk.Label(self.root, text="Category:").pack()
        self.category_entry = tk.Entry(self.root)  # Entry field for category
        self.category_entry.pack()

        # Description entry
        tk.Label(self.root, text="Description (Optional):").pack()
        self.description_entry = tk.Entry(self.root)  # Entry field for description
        self.description_entry.pack()

        # Buttons
        tk.Button(self.root, text="Save Transaction", command=self.save_transaction).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_window).pack(pady=5)

    def save_transaction(self):
        # Purpose: Validate and save a transaction, then return to main window
        amount = self.amount_entry.get()  # Get amount input
        category = self.category_entry.get()  # Get category input
        description = self.description_entry.get()  # Get description input
        trans_type = self.transaction_type.get()  # Get transaction type

        # Validate inputs
        error = validate_input(amount, category)
        if error:
            messagebox.showerror("Input Error", error)
            return

        # Save transaction
        self.logic.add_transaction(trans_type, float(amount), category, description)
        messagebox.showinfo("Success", "Transaction saved!")
        self.create_main_window()

    def view_transactions(self):
        # Purpose: Display all transactions in the secondary window
        self.clear_window()
        self.root.geometry("400x400")  # Adjust window size

        tk.Label(self.root, text="Transaction History").pack(pady=10)
        transactions = self.logic.get_transactions()
        if not transactions:
            tk.Label(self.root, text="No transactions yet.").pack()
        else:
            for trans in transactions:  # Display each transaction as a label
                tk.Label(self.root, text=f"{trans['type']}: ${trans['amount']} - {trans['category']}").pack()

        tk.Button(self.root, text="Back", command=self.create_main_window).pack(pady=10)

    def update_summary(self):
        # Purpose: Update the financial summary labels
        income, expenses = self.logic.calculate_summary()
        self.income_label.config(text=f"Total Income: ${income:.2f}")
        self.expense_label.config(text=f"Total Expenses: ${expenses:.2f}")
        self.balance_label.config(text=f"Balance: ${(income - expenses):.2f}")

    def exit_app(self):
        # Purpose: Safely exit the application
        if messagebox.askokcancel("Exit", "Do you want to exit Budget Buddy?"):
            self.root.quit()

# Main Module
# Purpose: Entry point for the BudgetBuddy application
def main():
    root = tk.Tk()
    app = BudgetBuddyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
