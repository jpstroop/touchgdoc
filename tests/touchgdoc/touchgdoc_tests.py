from touchgdoc.touchgdoc import TouchGoogleDoc
from touchgdoc.touchgdoc import PERMISSIONS_CHOICES

def test_module_has_permissions_constant():
    assert PERMISSIONS_CHOICES == ('rw', 'co', 'ro')


class TouchGoogleDocTests():

    def test_1(self):
        assert True
