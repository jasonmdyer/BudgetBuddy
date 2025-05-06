##BudgetBuddy by Jason Dyer

BudgetBuddy is a Python Tkinter GUI application designed for young adults (ages 18–30) to manage their monthly income and expenses. It provides a user-friendly interface to add transactions, view financial summaries, and track remaining balances. 

Key features include:
A main dashboard displaying total income, expenses, and balance.
A transaction entry window for adding income or expense records.
A transaction history window to review all entries.
Robust input validation to ensure accurate data entry.
Modular code structure with clear navigation and secure coding practices.

Setup:
To run BudgetBuddy, follow these steps:
Ensure Python 3.x is installed on your system (includes Tkinter by default).
Download or clone the project files to a local directory.
Open a terminal or command prompt and navigate to the project directory:
cd BudgetBuddy
python DyerJasonFinalProject.py

No additional libraries are required, the application uses only the standard Python library.

Usage:
Main Window:
Displays "Total Income," "Total Expenses," and "Balance."
Click Add Transaction to open the transaction entry form.
Click View Transactions to see a list of all recorded transactions.
Click Exit to close the application (confirms with a prompt).

Transaction Entry Window:
Select the transaction type (Income or Expense) from a dropdown menu.
Enter the amount (a positive number, e.g., 100.50).
Enter the category (e.g., Salary, Food).
Optionally, add a description (e.g., Monthly pay).
Click Save Transaction to save the entry (validated for errors) or Back to return to the main window.

Transaction History Window:
Lists all transactions with type, amount, and category.
Click Back to return to the main window.
Error messages appear if inputs are invalid (e.g., empty fields, non-numeric amounts).
