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


class BudgetTracker:
    """
    The 'Engine' of the application. 
    Manages the budget logic, category definitions, and expense collection.
    """
    # --- Constants to replace 'Magic Numbers' ---
    EXIT_CODE = 0
    MIN_BUDGET = 0.01
    
    # Predefined categories stored within the class context
    CATEGORIES = {
        1: "Sacks",
        2: "Lunch",
        3: "Breakfast",
        4: "Supper",
        5: "Utilities"
    }

    def __init__(self, budget):
        self.budget = budget
        self.expenses = []

