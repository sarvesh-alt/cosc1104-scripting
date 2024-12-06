'''
Author: Sarvesh More 
Date: 2024-12-04
Description:Managing cloud resources efficiently is crucial for organizations to avoid unnecessary costs,
maintain security, and reduce clutter. However, unused resources like unattached EBS volumes,
idle EC2 instances, unused S3 buckets, and stale IAM users often go unnoticed. 
The problem is to create a Python script that identifies and removes these unused resources on
AWS to automate the cleanup process.
'''

import boto3
from InquirerPy import inquirer
import logging

# Constants
LOG_FILE = "cleanup.log"
AWS_REGION = "us-east-1"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize AWS session
session = boto3.Session(region_name=AWS_REGION)
ec2_client = session.client('ec2')
s3_client = session.client('s3')


def list_unused_resources():
    """Identify unused AWS resources."""
    print("\nScanning for unused resources...\n")

    # Find unattached EBS volumes
    volumes = ec2_client.describe_volumes(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )
    unused_volumes = [v['VolumeId'] for v in volumes['Volumes']]

    # Find idle S3 buckets (placeholder logic)
    buckets = s3_client.list_buckets()
    unused_buckets = [bucket['Name'] for bucket in buckets['Buckets']]

    return unused_volumes, unused_buckets


def interactive_cleanup(unused_volumes, unused_buckets):
    """Present resources to user for cleanup."""
    choices = []
    if unused_volumes:
        choices += [f"Volume: {v}" for v in unused_volumes]
    if unused_buckets:
        choices += [f"Bucket: {b}" for b in unused_buckets]

    if not choices:
        print("No unused resources found!")
        return []

    to_delete = inquirer.checkbox(
        message="Select resources to delete:",
        choices=choices
    ).execute()

    return to_delete


def delete_resources(to_delete):
    """Delete selected AWS resources based on user input."""
    for resource in to_delete:
        try:
            if resource.startswith("Volume:"):
                volume_id = resource.split(": ")[1]
                ec2_client.delete_volume(VolumeId=volume_id)
                logging.info(f"Deleted Volume: {volume_id}")
            elif resource.startswith("Bucket:"):
                bucket_name = resource.split(": ")[1]
                s3_client.delete_bucket(Bucket=bucket_name)
                logging.info(f"Deleted Bucket: {bucket_name}")
        except Exception as e:
            logging.error(f"Error deleting {resource}: {e}")


def main():
    """Main function to orchestrate the cleanup."""
    print("AWS Resource Cleanup Script")
    print("===========================\n")

    unused_volumes, unused_buckets = list_unused_resources()
    to_delete = interactive_cleanup(unused_volumes, unused_buckets)

    if to_delete:
        delete_resources(to_delete)
        print("\nCleanup completed. Check 'cleanup.log' for details.")
    else:
        print("\nNo resources were selected for deletion.")


if __name__ == "__main__":
    main()
