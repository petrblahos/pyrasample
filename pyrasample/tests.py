import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import named_view_in_root
        request = testing.DummyRequest()
        info = named_view_in_root(request)
        self.assertEqual(info, {})
