import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp (self):
        self.new_contact = User("Dee","Mutheu","0712345678","dee@gmail.com","mutheu")

    def test_init(self):
        self.assertEqual(self.new_contact.firstname,"Dee")
        self.assertEqual(self.new_contact.lastname,"Mutheu")
        self.assertEqual(self.new_contact.email,"dee@gmail.com")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.password,"mutheu")

    def test_save_contact(self):
        self.assertEqual(len(User.user_list),0)
        
        
if __name__ == '__main__':
    unittest.main()
    