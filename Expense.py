import uuid
from datetime import datetime

class Expense:
    """Represents an individual financial expense."""

    def __init__(self, title: str, amount: float, currency: str = "USD"):
        """
        Initializes an Expense instance with a unique ID, title, amount, currency
        created_at, and updated_at timestamps.
        """
        self.id = str(uuid.uuid4())  
        self.title = self.validate_title(title)  
        self.amount = self.validate_amount(amount)  
        self.currency = currency  
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, title: str = None, amount: float = None):
        """
        Updates the title and/or amount of the expense.
        Updates the `updated_at` timestamp upon modification.
        """
        if title:
            self.title = self.validate_title(title) 
        if amount:
            self.amount = self.validate_amount(amount)  
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary representation of the expense and currency."""
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "currency": self.currency,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def validate_title(title):
        """Validates that the title is a non-empty string."""
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        return title.strip()

    @staticmethod
    def validate_amount(amount):
        """Validates that the amount is a positive float."""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a positive number.")
        return float(amount)
