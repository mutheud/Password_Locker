import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.new_credentials = Credentials("twitter","Dee","Mutheu","0798505109","dee@gmail.com","mutheu")
    
    def test_init(self):
        self.assertEqual(self.new_credentials.accountname,"twitter")
        self.assertEqual(self.new_credentials.firstname,"Dee")
        self.assertEqual(self.new_credentials.lastname,"Mutheu")
        self.assertEqual(self.new_credentials.phone_number,"0798505109")
        self.assertEqual(self.new_credentials.email,"dee@gmail.com")
        self.assertEqual(self.new_credentials.password,"mutheu")

    def test_save_credentials(self):
         self.assertEqual(len(Credentials.credentials_list),2)
       
    def teardown(self):
        Credentials.credentials_list= []

    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        paul_credentials = Credentials("facebook","Paul","Mulyungi","0789210912","paul@gmail.com","paul")
        paul_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),4)


    def test_delete_credentials(self):
        
        self.assertEqual(len(Credentials.credentials_list),0)



    def test_find_by_email(self):

        self.new_credentials.save_credentials()
        paul_credentials = Credentials("facebook","Paul","Mulyungi","0789210912","paul@gmail.com","paul")
        paul_credentials.save_credentials()

        found_password = Credentials.find_by_email("paul@gmail.com")

        self.assertEqual(found_password.email,paul_credentials.email)



    def test_display_credentials(self):
      
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


    
if __name__ == '__main__':
    unittest.main()
    