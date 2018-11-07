import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp (self):
        self.new_account = User("Dee","Mutheu","0712345678","dee@gmail.com","mutheu")

    def test_init(self):
        self.assertEqual(self.new_account.firstname,"Dee")
        self.assertEqual(self.new_account.lastname,"Mutheu")
        self.assertEqual(self.new_account.email,"dee@gmail.com")
        self.assertEqual(self.new_account.phone_number,"0712345678")
        self.assertEqual(self.new_account.password,"mutheu")

    def test_save_account(self):
        self.assertEqual(len(User.user_list),4)

    def teardown(self):
        User.user_list = []    

    def test_save_multiple_account(self):
        
        self.new_account.save_account()
        test_account = User("paul","luusa","0712447975","paul@gmail.com","paul")
        test_account.save_account()
        self.assertEqual(len(User.user_list),6)
        
    def test_delete_account(self):
        self.assertEqual(len(User.user_list),2)

    def test_find_by_number(self):
         
        self.new_account.save_account()
        test_account = User("paul","luusa","0712447975","paul@gmail.com","paul")
        test_account.save_account()
        found_account = User.find_by_number("0712447975")
        
        self.assertEqual(found_account.phone_number,test_account.phone_number)

    def test_account_exist(self):
         
        self.new_account.save_account()
        test_account = User("paul","luusa","0712447975","paul@gmail.com","paul")
        test_account.save_account()
        account_exist = User.find_by_number("0712447975")
        
        self.assertTrue(account_exist)

    def test_display_all_account(self):
        self.assertEqual(User.display_all_account(),User.user_list)

if __name__ == '__main__':
    unittest.main()
    