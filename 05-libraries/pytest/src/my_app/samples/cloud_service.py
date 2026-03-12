# cloud_service.py
import os
import boto3

def upload_system_log(filename):
    # This comes from the OS environment
    bucket = os.getenv("LOG_BUCKET") 
    if not bucket:
        raise ValueError("Bucket not configured")
        
    # This is an external API call
    s3 = boto3.client("s3")
    s3.upload_file(filename, bucket, "logs/latest.log")
    return True