import uuid

import boto3

s3_resource = boto3.resource('s3')

BUCKET1 = 'jgrizou-3deccfcc-1a67-4f95-83b3-cdc138f5e802'

FILEKEY = '631fadfirstfile.txt'

s3_resource.Object(BUCKET1, FILEKEY).delete()


## delete all bucket

# first_bucket = s3_resource.Bucket(name=BUCKET1)
# first_bucket.delete()
