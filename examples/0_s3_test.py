"""
Just testing the AWS boto client against S3 to validate credentials
"""

import boto3

# Let's use Amazon S3
s3 = boto3.resource("s3")


# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
