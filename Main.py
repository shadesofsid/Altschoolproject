from Expense import Expense
from Expense_db import ExpenseDB

# Create ExpenseDB instance
db = ExpenseDB()

# Create expenses
expense1 = Expense("Groceries", 50.25)
expense2 = Expense("Electricity Bill", 120.75)
expense3 = Expense("Internet", 45.99)
expense4 = Expense("Fuel", 30.00)
expense5 = Expense("Rent", 500.00)
expense6 = Expense("Water Bill", 25.50)  
expense7 = Expense("Transport", 60.00) 

# Add expenses to database
db.add_expense(expense1)
db.add_expense(expense2)
db.add_expense(expense3)
db.add_expense(expense4)
db.add_expense(expense5)
db.add_expense(expense6)
db.add_expense(expense7)

# Display expenses
print("All Expenses:")
for exp in db.to_dict():
    print(exp)

# Search by title
print("\nSearching for 'Internet' expense:")
print(db.get_expense_by_title("Internet"))

# Search by ID
expense_id = expense2.id
print(f"\nSearching for expense with ID: {expense_id}")
print(db.get_expense_by_id(expense_id))

# Remove an expense
print("\nRemoving 'Fuel' expense...")
db.remove_expense(expense4.id)

# Display updated expenses
print("\nUpdated Expense List:")
for exp in db.to_dict():
    print(exp)
