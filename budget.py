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

    def get_total_spent(self):
        """Calculates total spending dynamically from the list of objects."""
        return sum(exp.amount for exp in self.expenses)

    def get_remaining_balance(self):
        """Calculates the difference between budget and spending."""
        return self.budget - self.get_total_spent()

    def add_expense(self, category_index, description, amount):
        """Creates an Expense object and adds it to the internal list."""
        category_name = self.CATEGORIES.get(category_index, "Unknown")
        new_expense = Expense(category_name, description, amount)
        self.expenses.append(new_expense)
        return new_expense


def main():
    """
    The 'User Interface' layer.
    Handles all print() and input() calls, delegating logic to the BudgetTracker.
    """
    print("=" * 40)
    print("    Personal Financial Assistant (OOP)")
    print("=" * 40)

    # --- Initialize Budget ---
    while True:
        try:
            user_budget = float(input("\nEnter your budget for this period: "))
            if user_budget < BudgetTracker.MIN_BUDGET:
