'''
Author: Sarvesh More 
Date: 2024-11-12
Description:This tool helps in managing time efficiently, as users can focus on higher-priority tasks first and avoid forgetting important ones. 
'''

import datetime

def get_task_input():
    """Function to get task details from the user."""
    task_name = input("Enter the task name: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
    if due_date:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
    else:
        due_date = None
    return task_name, priority, due_date

def display_tasks(tasks):
    """Function to display tasks sorted by priority."""
    if tasks:
        tasks.sort(key=lambda x: (x[1], x[2]))  # Sort by priority and due date
        for task in tasks:
            print(f"Task: {task[0]}, Priority: {task[1]}, Due: {task[2] if task[2] else 'N/A'}")
    else:
        print("No tasks available.")

def mark_task_complete(tasks):
    """Function to mark a task as complete."""
    task_name = input("Enter the task name to mark as complete: ")
    task_found = False
    for task in tasks:
        if task_name == task[0]:
            tasks.remove(task)
            print(f"Task '{task_name}' completed and removed.")
            task_found = True
            return tasks, task_found
    return tasks, task_found

def main():
    """Main function to run the task scheduler."""
    tasks = []
    user_input = ""

    while user_input != "4":
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")
        
        user_input = input("Choose an option: ")
        
        if user_input == "1":
            task_name, priority, due_date = get_task_input()
            tasks.append((task_name, priority, due_date))
        elif user_input == "2":
            display_tasks(tasks)
        elif user_input == "3":
            tasks, task_found = mark_task_complete(tasks)
            if not task_found:
                print(f"Task '{task_name}' not found.")
        elif user_input != "4":
            print("Invalid option. Please try again.")
        
    print("Goodbye!")

if __name__ == "__main__":
    main()




