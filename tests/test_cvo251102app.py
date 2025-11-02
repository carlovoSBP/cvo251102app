from unittest import TestCase

from cvo251102app import hello


class TestSmoke(TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_integration(self):
        self.assertEqual("Hello you from cvo251102app!", hello())
