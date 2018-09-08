from j2s3.file_service import *
import os
import tempfile

filename = os.path.join(os.path.dirname(__file__), '../resources/testfile.txt')

def test_can_get_file_content():
    res = get_file_content(filename)
    assert res == 'test_content'

def test_can_write_file_content():
    with tempfile.NamedTemporaryFile() as tmp:
        path = tmp.name
        test_content = "test_content"
        assert get_file_content(path) == ""
        write_file_content(path, test_content)
        assert get_file_content(path) == test_content
