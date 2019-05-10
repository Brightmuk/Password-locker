import unittest

from credential import Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for user class
    behaviours
    '''
    def setUp(self):
        '''
        Setup method to run before each test cases
        '''
        self.new_credential = Credential("twitter","muko12")
    def test_init(self):
        '''
        test_init checks if the object is initialised properly
        '''
        self.assertEqual(self.new_credential.account_name,"twitter")
        self.assertEqual(self.new_credential.password,"muko12")

    def test_save_credential(self):
        '''
        test_save_credential tests if a new credential has been added to credentials
        list of a user
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def test_display_user_credentials(self):
        '''
        test to display the credentials of a user
        '''
        self.assertEqual(Credential.display_user_credentials(),Credential.credential_list)
if __name__ == '__main__':
    unittest.main()
