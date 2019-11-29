# Java 2 Aws S3

<img src="logo.png" height="100"/>
<br/>
Python library for publishing maven projects to an S3 maven repository. Requires maven installed in your path. 

## Why?
When building a Java API one often wants to publish API Clients after each build. This can be a cumbersome process. With J2S3 you can publish to an s3 repository for internal use without the hassle of setting up mavencentral on bintray access.

## Preliminaries
- Set up an s3 bucket in s3 to use as a repository
- Create an IAM user with s3 access
- Get the access key id and secret for this user

## Usage
- Use the [j2s3 docker image](https://hub.docker.com/r/jackmahoney/j2s3/) with j2s3-cli, maven, and java installed
- OR the [j2s3 cli](https://pypi.org/project/j2s3-cli/)
- OR invoke j2s3 in python directly


### Example invocation

```bash
pip3 install j2s3
```

```python
from j2s3.main import publish

# project_directory: a dir containing Java code and a pom.xml file
publish(project_directory, aws_access_key_id, aws_secret_access_key, s3_bucket_name)
```

## Contributing
Pull requests and bug reports welcome on the github repository.
