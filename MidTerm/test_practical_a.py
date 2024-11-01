'''
Author : Sarvesh More
Date : 15-October-2024
Description : Midterm Exercises for SCripting
'''

#Constants
TOTAL_NUMBER_OF_DEPARTMENTS = 3
MAXIMUM_TOTAL_USERS = 32
request_more = 'yes'

while(request_more == "yes"):
    
#input from user
             
    first_department = int(input("Enter the number of users in the first department: "))            #the Number of users in the first department
    second_department = int(input("Enter the number of users in the second department: "))          #The number of users in the second department
   
    # Calculate the total number of users in the first two departments to make it easier
    total_users_first_two = first_department + second_department
    
    #The program should not end until the user has confirmed to exit
    
    # Check if the number of users in the first two departments exceeds the maximum total users
    if total_users_first_two > MAXIMUM_TOTAL_USERS:
        print(f"Error: You have exceeded the maximum allowable users {MAXIMUM_TOTAL_USERS}.")
    
    # Check if the number of users in the first two departments equals the maximum total users
    elif total_users_first_two == MAXIMUM_TOTAL_USERS:
        print(f"There are no additional users allowed.")
    # If the total is less than the maximum, calculate the remaining users for the third department
    else:
        remaining_users = MAXIMUM_TOTAL_USERS - total_users_first_two
        print(f"There are {remaining_users} users still available")
    #Ask if the user wants to make another request
request_more = input("Do you want to make another request? (yes/no): ").strip().lower()


# Display allocated resources
print("\nAllocated Users:")
print("Department 1\Department 2\Department 3")

print(f"{first_department[0]:<16}{second_department[1]:<12}{remaining_users[2]}")

    
    
while request_more == "yes":
    
    # Input from user
    try:
        first_department = int(input("Enter the number of users in the first department: "))   # Number of users in the first department
        second_department = int(input("Enter the number of users in the second department: ")) # Number of users in the second department
        
        # Calculate the total number of users in the first two departments
        total_users_first_two = first_department + second_department

        # Check if the number of users in the first two departments exceeds the maximum total users
        if total_users_first_two > MAXIMUM_TOTAL_USERS:
            print(f"Error: You have exceeded the maximum allowable users ({MAXIMUM_TOTAL_USERS}).")

        # Check if the number of users in the first two departments equals the maximum total users
        elif total_users_first_two == MAXIMUM_TOTAL_USERS:
            print("There are no additional users allowed.")

        # If the total is less than the maximum, calculate the remaining users for the third department
        else:
            remaining_users = MAXIMUM_TOTAL_USERS - total_users_first_two
            print(f"There are {remaining_users} users still available for the third department.")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer for the number of users.")
        continue  # Continue to the next iteration if there is an invalid input

    # Ask if the user wants to make another request
    request_more = input("Do you want to make another request? (yes/no): ").strip().lower()

# Display allocated resources
print("\nAllocated Users:")
print("Department 1    Department 2    Department 3")

# Display the number of users in each department
print(f"{first_department:<16}{second_department:<16}{remaining_users}")