import unittest

from aufgaben_package.rechen_operation import *

class TestRechenOperationMethods(unittest.TestCase):

    def test_erhoehe_um_zwei(self):
        assert erhoehe_um_zwei(2) == 4

    def test_multipliziere_mit_drei(self):
        assert multipliziere_mit_drei(2) == 6

    def test_subtrahiere_zehn(self):
        assert subtrahiere_zehn(13) == 3

    def test_teile_durch_vier(self):
        assert teile_durch_vier(8) == 2
        with self.assertRaises(ValueError):
            teile_durch_vier(9)

