import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title


        if amount is not None:
            self.amount = amount

        self.updated_at = datetime.now(timezone.utc)

    # A dictionary representation to cleary show the expense
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class ExpenseDB:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, expense_title):
        similar_expenses = []
        for expense in self.expenses:
            if expense.title == expense_title:
                similar_expenses.append(expense)
        return similar_expenses
    def to_dict(self):
        return {
            'expenses': [expense.to_dict() for expense in self.expenses]
        }


