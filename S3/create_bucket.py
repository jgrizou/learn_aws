import uuid

import boto3

s3_resource = boto3.resource('s3')

def create_bucket_name():
    # The generated bucket name must be between 3 and 63 chars long
    return 'jgrizou-{}'.format(str(uuid.uuid4()))

def create_bucket(s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name()
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response
