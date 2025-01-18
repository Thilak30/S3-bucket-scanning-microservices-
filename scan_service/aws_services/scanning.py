import boto3
import os
import re

def scan_s3_file(bucket_name, file_name):
    """
    Scans a file in S3 for sensitive data patterns directly in AWS.
    """
    # Use environment variables for AWS credentials
    aws_access_key_id = os.getenv('Your AWS Access key_id')
    aws_secret_access_key = os.getenv('Your AWS Access key')
    aws_region = os.getenv('Your Region')

    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )
    try:
        # Stream file content directly from S3
        obj = s3.get_object(Bucket=bucket_name, Key=file_name)
        content = obj['Body'].read().decode('utf-8')

        # Scan the content for sensitive data
        matches = scan_for_sensitive_data(content)
        return matches
    except Exception as e:
        return {"error": str(e)}

def scan_for_sensitive_data(content):
    """
    Defines sensitive data patterns and scans text content.
    """
    patterns = {
        "MasterCard": r'(?:5[12345][0-9]{14})',
        "VISA": r'(?:4[0-9]{12}(?:[0-9]{3})?)',
        "American Express": r'(?:3[47][0-9]{13})',
    }

    results = {}
    for label, pattern in patterns.items():
        found = re.findall(pattern, content)
        if found:
            results[label] = found
    return results
