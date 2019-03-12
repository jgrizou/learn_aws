import uuid

import boto3

s3_resource = boto3.resource('s3')

BUCKET1 = 'jgrizou-3deccfcc-1a67-4f95-83b3-cdc138f5e802'

BUCKET2 = 'jgrizou-7dc328b4-d41f-4045-9b82-3571ed2c6ca3'

FILEKEY = '631fadfirstfile.txt'


def copy_to_bucket(bucket_from_name, bucket_to_name, file_key):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_key
    }
    s3_resource.Object(bucket_to_name, file_key).copy(copy_source)

copy_to_bucket(BUCKET1, BUCKET2, FILEKEY)
