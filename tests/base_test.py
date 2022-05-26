import unittest
import script


class BaseConfig(object):
    """Common configurations"""
    TESTING = True
    DEBUG = True


class BaseTest(unittest.TestCase):
    """Base test class"""

    def create_app(self):
        BaseConfig.TESTING = True
        return script.app

    def setUp(self):
        self.app = script.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass
