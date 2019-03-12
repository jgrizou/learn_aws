import uuid

import boto3

s3_resource = boto3.resource('s3')

BUCKET_NAME = 'jgrizou-3deccfcc-1a67-4f95-83b3-cdc138f5e802'

FILENAME = '631fadfirstfile.txt'


first_bucket = s3_resource.Bucket(name=BUCKET_NAME)


first_bucket.download_file(
    Filename='tmp/{}'.format(FILENAME), Key=FILENAME)
