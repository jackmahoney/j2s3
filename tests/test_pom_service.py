import os

from j2s3.pom_service import *
from j2s3.file_service import *

filename = os.path.join(os.path.dirname(__file__), '../resources/pom.xml')

def test_parse_xml_string():
    bucket_name = "test_bucket_name"
    xmlstring = get_file_content(filename)
    pom = Pom(xmlstring, bucket_name)
