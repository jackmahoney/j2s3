import os

from j2s3.pom import *
from j2s3.file_service import *

filename = os.path.join(os.path.dirname(__file__), '../resources/pom.xml')

def test_parse_xml_string():
    bucket_name = 'test_bucket_name'
    xmlstring = get_file_content(filename)
    pom = Pom(xmlstring, bucket_name)
    rendered = pom.tostring()
    assert '<artifactrepo.url>%s</artifactrepo.url>' % bucket_name in rendered
    assert '<url>s3://${artifactrepo.url}/snapshot</url>' in rendered
    assert '<url>s3://${artifactrepo.url}/release</url>' in rendered
    assert '<groupId>org.kuali.maven.wagons</groupId>' in rendered
    assert '<artifactId>maven-s3-wagon</artifactId>' in rendered
    assert '<version>1.2.1</version>' in rendered
