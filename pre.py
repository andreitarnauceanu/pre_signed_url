import boto3
import json
import requests
from utils import shorten, pre_signed_url

original_files = []
croped_files = []
s3 = boto3.resource('s3')
bucket_name = 'microservice-backet-linuxacademyuser'
my_bucket = s3.Bucket(bucket_name)
for file in my_bucket.objects.all():
  if 'CROP' in file.key:
    shorturl = shorten(pre_signed_url(file.key, bucket_name))
    original_files.append(dict(key=file.key, url=shorturl))
print '-'*30
for file in my_bucket.objects.all():
  if 'uploads' in file.key:
    shorturl = shorten(pre_signed_url(file.key, bucket_name))
    croped_files.append(dict(key=file.key, url=shorturl))
	
print original_files
print croped_files

