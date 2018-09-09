import os

from j2s3.pom import *
from j2s3.xml_service import *
from j2s3.file_service import *

filename = os.path.join(os.path.dirname(__file__), '../resources/pom.xml')

def test_parse_xml_string():
    root = parse_xml_string(get_file_content(filename))
    deps = root.findall('.//' + Pom.tag_prefix + 'dependency')
    assert len(deps) == 7
