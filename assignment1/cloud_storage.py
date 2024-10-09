'''
Author:Sarvesh More
Date: 2024-09-27
Problem:
This program is based around the creation of a simulated cloud storage tracking system.
You will need to define at least these three functions:
•	A function to create a user account. Its parameters will be a username, and the amount of storage space this used has available.
    When the user account is created, the username will be added to a list of usernames and the storage space will be added to a list 
    for each user’s available space.
    This should include some validation to ensure the username is unique (and not blank!) and the storage space is a positive number.
•	A function representing the upload of a file. Its parameters will be a username, a filename, and a filesize. 
    If the user exists and has enough space to upload the file, update the used space.
•	A function to delete a user account.

'''
usernames = []
available_spaces = []
used_spaces = []


def create_user_account():
    """Create a new user account."""
    username = input("Enter a username: ").strip()
    '''Assuming username can have numbers and or characters so no validation on it except blank '''
    if not username:
        print("Error: Username cannot be blank.")
        return
    
    if username in usernames:
        print("Error: Username already exists.")
        return
    
    try:
        storage_space = float(input("Enter available storage space (MB): "))
        if storage_space <= 0:
            print("Error: Storage space must be a positive number.")
            return
    except ValueError:
        print("Error: Please enter a valid number for storage space.")
        return
    
    usernames.append(username)
    available_spaces.append(storage_space)
    used_spaces.append(0.0)
    
    print(f"User '{username}' created successfully with {storage_space} MB of storage.")


def upload_file():
    """Upload a file to an existing user account."""
    username = input("Enter username: ").strip()
    
    if username not in usernames:
        print("Error: User does not exist.")
        return
    
    index = usernames.index(username)
    
    ''' No validation again on filename since we have might need to import external library like re to not let user 
        user use hyphen or dot'''
    filename = input("Enter filename: ").strip()
    
    try:
        filesize = float(input("Enter file size (MB): "))
        if filesize <= 0:
            print("Error: File size must be a positive number.")
            return
    except ValueError:
        print("Error: Please enter a valid number for file size.")
        return
    
    available_space = available_spaces[index]
    used_space = used_spaces[index]
    
    if filesize > (available_space - used_space):
        print("Error: Not enough storage space available to upload the file.")
    else:
        used_spaces[index] += filesize
        print(f"File '{filename}' uploaded successfully for user '{username}'.")


def delete_user_account():
    """Delete an existing user account."""
    username = input("Enter username to delete: ").strip()
    
    if username not in usernames:
        print("Error: User does not exist.")
        return
    
    index = usernames.index(username)
    usernames.pop(index)
    available_spaces.pop(index)
    used_spaces.pop(index)
    
    print(f"User '{username}' deleted successfully.")


def display_all_accounts():
    """Display all user accounts with their available storage space."""
    if not usernames:
        print("No users exist.")
    else:
        print("\nCurrent user accounts and their storage:")
        for i in range(len(usernames)):
            available_space = available_spaces[i]
            used_space = used_spaces[i]
            remaining_space = available_space - used_space
            print(f"Username: {usernames[i]}, Available Space: {remaining_space:.2f} MB")
        print()


def show_menu():
    """Display the main menu and handle user selections."""
    while True:
        print("\nCloud Storage Tracking System")
        print("1. Create User Account")
        print("2. Delete User Account")
        print("3. Upload File")
        print("4. Display All Accounts")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            create_user_account()
        elif choice == "2":
            delete_user_account()
        elif choice == "3":
            upload_file()
        elif choice == "4":
            display_all_accounts()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please select a valid option.")


# Start the program
if __name__ == "__main__":
    show_menu()
