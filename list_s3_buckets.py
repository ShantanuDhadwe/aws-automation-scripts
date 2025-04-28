import boto3

def list_s3_buckets():
    """List all S3 buckets in your account."""
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")

def count_objects(bucket_name):
    """Count objects in the specified S3 bucket using pagination."""
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name)

    total = 0
    for page in page_iterator:
        total += page.get('KeyCount', 0)
    print(f"Total objects in '{bucket_name}': {total}")

if __name__ == "__main__":
    list_s3_buckets()                             # :contentReference[oaicite:12]{index=12}
    count_objects('your-bucket-name')             # :contentReference[oaicite:13]{index=13}
