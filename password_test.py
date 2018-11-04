import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.new_credentials = Credentials("James","Muriuki","0712345678","james@ms.com","mutheu")