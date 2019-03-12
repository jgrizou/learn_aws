import uuid

import boto3

s3_resource = boto3.resource('s3')

BUCKET_NAME = 'jgrizou-3deccfcc-1a67-4f95-83b3-cdc138f5e802'

def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name


first_file_name = create_temp_file(300, 'firstfile.txt', 'f')


first_bucket = s3_resource.Bucket(name=BUCKET_NAME)


first_bucket.upload_file(
    Filename=first_file_name, Key=first_file_name)
