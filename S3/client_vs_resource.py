import boto3

# client is low level API
s3_client = boto3.client('s3')

# ressouce is high-level API
s3_resource = boto3.resource('s3')

# client can be found in resource
#s3_resource.meta.client.

#give your users access to an object within your bucket
# s3_client.generate_presigned_url()
# s3_resource.meta.client.generate_presigned_url()
