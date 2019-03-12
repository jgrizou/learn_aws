import uuid

import boto3

s3_resource = boto3.resource('s3')

BUCKET2 = 'jgrizou-7dc328b4-d41f-4045-9b82-3571ed2c6ca3'

second_bucket = s3_resource.Bucket(name=BUCKET2)


for object in second_bucket.objects.all():
    print(object.key)
