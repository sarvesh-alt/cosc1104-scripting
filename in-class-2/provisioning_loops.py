# provisioning_loops.py
# Author: Sarvesh More and Julekha Khatoon
# Date: 2024-09-27
# Description: We are extending the main idea of our simulation from the previous part, still doing a mock resource allocation app. However, this time it will incorporate both loops and lists.
# Instead of checking whether one resource allocation request is valid, it will do as many as the user wants.


# Constants

TOTAL_CPU_CORES = 32  # Total number of CPU cores available
TOTAL_MEMORY_GB = 128  # Total amount of memory available in gigabytes (GB)

# Lists to track resources
allocated_resources = []  # List to store allocated resources
pending_requests = []      # List to store pending requests

# Variables to track used resources
used_cpu_cores = 0
used_memory_gb = 0

# Main loop for handling user requests
while True:
    # User input for resource requests
    username = input("Enter username: ")
    required_cpu_cores = int(input("Enter the number of required CPU cores (positive integer): "))
    required_memory_gb = float(input("Enter the amount of required memory in GB (positive number): "))

    # Input validation
    if required_cpu_cores < 0 or required_memory_gb < 0:
        print("Error: Resource requests cannot be negative.")
        continue

    # Check resource availability
    if (used_cpu_cores + required_cpu_cores <= TOTAL_CPU_CORES) and \
       (used_memory_gb + required_memory_gb <= TOTAL_MEMORY_GB):
        # Allocate resources
        allocated_resources.append([username, required_cpu_cores, required_memory_gb])
        used_cpu_cores += required_cpu_cores
        used_memory_gb += required_memory_gb
        print("Resources provisioned successfully.")
    else:
        # Add to pending requests
        pending_requests.append([username, required_cpu_cores, required_memory_gb])
        print("Resource request exceeds capacity. Provisioning failed.")

    # Ask if the user wants to make another request
    another_request = input("Do you want to make another request? (yes/no): ").strip().lower()
    if another_request != 'yes':
        break

# Display allocated resources
print("\nAllocated Resources:")
print("Username\tCPU Cores\tMemory (GB)")
for resource in allocated_resources:
    print(f"{resource[0]}\t\t{resource[1]}\t\t{resource[2]}")

# Display pending requests
print("\nPending Requests:")
print("Username\tCPU Cores\tMemory (GB)")
for request in pending_requests:
    print(f"{request[0]}\t\t{request[1]}\t\t{request[2]}")
