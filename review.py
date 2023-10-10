foo = []

from .models import Expense
from collections import namedtuple

MyExpense = namedtuple('F', ['type_', 'amount'])

# test data
foo.append(MyExpense('food', 4))
foo.append(MyExpense('food', 3))
foo.append(MyExpense('var', 3))
foo.append(MyExpense('dog', 1))


def summarizeExpenses(min_amount, input):
    expenses = {}
    for expense in input:
        if expense.amount >= min_amount:
            if not expense.type in expenses:
                expenses[expense.type_] = 0
            expenses[expense.type_] = expenses[expense.type_] + expense.amount
    
    for (expense, amount) in sorted(expenses.items(), key=lambda e: e[1], reverse=False):
        print expense.type_, amount
summarizeExpenses(2, foo)