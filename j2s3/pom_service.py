from .xml_service import parse_xml_string
from lxml import etree

class Pom:
    # xmlns namespace
    tag_prefix = '{http://maven.apache.org/POM/4.0.0}'

    def __init__(self, xmlstring, bucket_name):
        self.bucket_name = bucket_name
        self.root = parse_xml_string(xmlstring)
        # set properties repo url to bucketname
        properties = self.get_or_create(self.root, 'properties')
        artifactrepo_url = self.get_or_create(properties, 'artifactrepo.url')
        artifactrepo_url.text = bucket_name

    def get(self, tag):
        return self.root.find('.//' + self.tag_prefix + tag)

    def create(self, root, tag):
        return etree.SubElement(root, tag)

    def get_or_create(self, root, tag):
        elem = self.get(tag)
        return elem if elem else self.create(root, tag)

    def tostring(self):
        return etree.tostring(self.root)


