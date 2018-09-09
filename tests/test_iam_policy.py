from j2s3.iam_policy import *

def test_can_get_iam_policy():
    bucket_name = 'test_bucket_name'
    policy = get_iam_policy(bucket_name)
    assert '"arn:aws:s3:::%s/snapshot/*"' % bucket_name in policy
    assert '"arn:aws:s3:::%s/release/*"' % bucket_name in policy
