from j2s3.settings import *

def test_can_substitute_variables():
    aws_access_key_id = 'test_access_key_id'
    aws_secret_key = 'test_secret_key'
    settings = Settings(aws_access_key_id, aws_secret_key)
    rendered = settings.tostring()
    assert '<username>%s</username>' % aws_access_key_id in rendered
    assert '<password>%s</password>' % aws_secret_key in rendered
