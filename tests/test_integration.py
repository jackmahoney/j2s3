import os
from j2s3.main import publish

def test_integration():
    dir = os.path.join(os.path.dirname(__file__), '../resources/petstore')
    username = os.environ['AWS_ACCESS_KEY_ID']
    password = os.environ['AWS_SECRET_ACCESS_KEY']
    bucket_name = os.environ['BUCKET_NAME']
    publish(dir, username, password, bucket_name)