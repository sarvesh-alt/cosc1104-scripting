'''
Author: Sarvesh More 
Date: 2024-11-11
Description:Managing personal finances is an essential task for individuals, but it can often be overwhelming, especially 
when expenses are not tracked systematically.
A simple budget planner will allow users to track their monthly income and categorize their expenses. 
'''


import matplotlib.pyplot as plt
import json
import os

def get_income():
    """Function to get the monthly income from the user."""
    income = float(input("Enter your monthly income: $"))
    return income

def get_expenses():
    """Function to get expenses from the user."""
    expenses = []
    category = ""
    while category.lower() != 'done':
        category = input("Enter expense category (or 'done' to finish): ")
        if category.lower() != 'done':
            amount = float(input(f"Enter expense amount for {category}: $"))
            expenses.append((category, amount))
    return expenses

def calculate_budget(income, expenses):
    """Function to calculate total expenses and remaining budget."""
    total_expenses = sum(expense[1] for expense in expenses)
    remaining_budget = income - total_expenses
    return total_expenses, remaining_budget

def save_data(income, expenses):
    """Function to save data to a JSON file for later use."""
    data = {
        "income": income,
        "expenses": expenses
    }
    with open("budget_data.json", "w") as file:
        json.dump(data, file)

def load_data():
    """Function to load previously saved data from a JSON file."""
    if os.path.exists("budget_data.json"):
        with open("budget_data.json", "r") as file:
            data = json.load(file)
            return data["income"], data["expenses"]
    else:
        return 0, []

def visualize_budget(income, total_expenses):
    """Function to generate a bar chart comparing income and expenses."""
    categories = ['Income', 'Expenses']
    values = [income, total_expenses]
    
    plt.bar(categories, values, color=['green', 'red'])
    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    plt.title('Income vs Expenses')
    plt.show()

def main():
    """Main function to run the budget planner."""
    print("Welcome to the Simple Budget Planner!")
    
    income, expenses = load_data()
    
    if income == 0:
        income = get_income()
    
    expenses = get_expenses()
    
    total_expenses, remaining_budget = calculate_budget(income, expenses)
    
    print(f"\nTotal Expenses: ${total_expenses}")
    print(f"Remaining Budget: ${remaining_budget}")
    
    save_data(income, expenses)
    
    visualize_budget(income, total_expenses)

if __name__ == "__main__":
    main()
