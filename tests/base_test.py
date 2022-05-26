import unittest
import script


class BaseConfig(object):
    """Common configurations"""
    TESTING = False


class BaseTest(unittest.TestCase):
    """Base test class"""

    def create_app(self):
        BaseConfig.TESTING = True
        return script()

    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client()
        self.user_data = {}

    def tearDown(self):
        pass
