import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.new_credentials = Credentials("Dee","Mutheu","0798505109","dee@gmail.com","mutheu")
    
    def test_init(self):
        self.assertEqual(self.new_credentials.firstname,"Dee")
        self.assertEqual(self.new_credentials.lastname,"Mutheu")
        self.assertEqual(self.new_credentials.phone_number,"0798505109")
        self.assertEqual(self.new_credentials.email,"dee@gmail.com")
        self.assertEqual(self.new_credentials.password,"mutheu")
    
if __name__ == '__main__':
    unittest.main()
    