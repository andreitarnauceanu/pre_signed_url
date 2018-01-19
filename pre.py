import boto3

import json
import requests

GOOGLE_URL_SHORTEN_API = 'AIzaSyBrnkM64WKqmKa_FmRbR6WIZeAu-hXE-6I' # IP Address restrictions

def shorten(url):
   req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + GOOGLE_URL_SHORTEN_API
   payload = {'longUrl': url}
   headers = {'content-type': 'application/json'}
   r = requests.post(req_url, data=json.dumps(payload), headers=headers)
   resp = json.loads(r.text)
   return resp['id']

def pre_signed_url(key, bucket):
	s3Client = boto3.client('s3')
	return s3Client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': key}, ExpiresIn = 300)


s3 = boto3.resource('s3')
bucket_name = 'microservice-backet-linuxacademyuser'
my_bucket = s3.Bucket(bucket_name)

for file in my_bucket.objects.all():
  if 'CROP' in file.key:
    print " %s | %s" % (file.key, shorten(pre_signed_url(file.key, bucket_name)))
print '-'*30
for file in my_bucket.objects.all():
  if 'uploads' in file.key:
    print " %s | %s" % (file.key, shorten(pre_signed_url(file.key, bucket_name)))
