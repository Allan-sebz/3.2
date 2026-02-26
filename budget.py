import sys

class Expense:
    """
    Data Class to represent a single financial transaction.
    Encapsulates the details of an expense.
    """
    def __init__(self, category, description, amount):
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        """Returns a formatted string for the transaction log."""
        return f"[{self.category}] {self.description} - {self.amount:.2f}"


