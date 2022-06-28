import boto3
import uuid 

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_my_bucket(bucket_prefix, s3_connection):
		# generate session object using users credentials. get session object.
    session = boto3.session.Session()
		# get the region name from that session object
    # current_region = session.region_name
    current_region = "ap-south-1"
		# get the bucket name from the previous function
    bucket_name = create_bucket_name(bucket_prefix)
		# save response from AWS! 
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response
    # function doesn't specify a client or resource interface - code works with either

def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    path = rF'P:\CSpCloud\H_Workspace\Boto3\{random_file_name}'
    with open(path, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name

def copy_to_bucket(s3_connection, from_bucket, to_bucket, filename):
  # make a new dictionary
  copy_source = {
    'Bucket':from_bucket,
    'Key':filename
  }
  # create new object (in the new bucket, with same filename)
  s3_connection.Object(to_bucket, filename).copy(copy_source)

def enable_bucket_versioning(s3_connection, bucket_name):
		# create a bucket versioning object with the bucket_name
    bkt_versioning = s3_connection.BucketVersioning(bucket_name)
    bkt_versioning.enable()
		# return status
    print(bkt_versioning.status)

def delete_all_objects(s3_connection, bucket_name):
    res = []
    bucket=s3_connection.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    print(res)
    bucket.delete_objects(Delete={'Objects': res})
  