from Expense import Expense  

class ExpenseDB:
    """Manages a collection of Expense objects."""

    def __init__(self):
        """Initializes an empty list of expenses."""
        self.expenses = []

    def add_expense(self, expense: Expense):
        """Adds an expense to the database."""
        if not isinstance(expense, Expense):
            raise TypeError("Only Expense objects can be added.")
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        """Removes an expense by its unique ID."""
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        """Retrieves an expense by ID."""
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None  

    def get_expense_by_title(self, title: str):
        """Retrieves all expenses with a given title."""
        return [expense for expense in self.expenses if expense.title.lower() == title.lower()]

    def to_dict(self):
        """Returns a list of dictionaries representing expenses."""
        return [expense.to_dict() for expense in self.expenses]


