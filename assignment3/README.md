Environment and AWS Credentials Setup
This guide explains how to set up your environment and AWS credentials to ensure your Python scripts interact seamlessly with AWS services.

1. Prerequisites
Before proceeding, ensure you have the following installed on your system:

Python 3.7+
Pip (Python package manager)
AWS CLI (Download and Installation Guide)
Boto3 library (Install using pip install boto3)


2. Setting Up AWS Credentials
AWS credentials allow your script to authenticate and access AWS services.

Option 1: Using AWS CLI
Open a terminal or command prompt.
Run the following command to configure your credentials:

aws configure

Enter your AWS Access Key ID, Secret Access Key, default region, and output format (e.g., json).

Example:

AWS Access Key ID [None]: YOUR_ACCESS_KEY
AWS Secret Access Key [None]: YOUR_SECRET_KEY
Default region name [None]: us-east-1
Default output format [None]: json
This will automatically create a credentials file at:

Linux/Mac: ~/.aws/credentials
Windows: C:\Users\YourUsername\.aws\credentials  (I used this)


Option 2: Manually Creating the Credentials File
Locate the credentials directory:
Linux/Mac: ~/.aws/
Windows: C:\Users\YourUsername\.aws\

Create a file named credentials (if it doesn’t already exist).

Add the following content:

[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY

Optionally, create a config file in the same directory to specify the default region:

[default]
region = us-east-1
output = json


3. Setting Up the Environment
Create and activate a virtual environment (optional:

python -m venv env
source env/bin/activate  # On Linux/Mac
.\env\Scripts\activate   # On Windows



4. Testing the Setup
Test if AWS credentials are correctly set up by listing S3 buckets:

bash

aws s3 ls
Or use a Python script to verify the credentials:


# Test connection to AWS S3
s3 = boto3.client('s3')
response = s3.list_buckets()
print("Available Buckets:", [bucket['Name'] for bucket in response['Buckets']])


NOW you can execute the script of the Assignment 3 in the other folder PArt 3 as you are connected with AWS
