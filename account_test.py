import unittest #unnitest module import
import pyperclip
from user import User
from credentials import Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for user class
    behaviours
    '''
    def setUp(self):
        '''
        Setup method to run before each test cases
        '''
        self.new_user = User("Bright","Mukonesi","muko12")
    def test_init(self):
        '''
        test_init checks if the object is initialised properly
        '''
        self.assertEqual(self.new_user.first_name,"Bright")
        self.assertEqual(self.new_user.second_name,"Mukonesi")
        self.assertEqual(self.new_user.password,"muko12")
if __name__ == '__main__':
    unittest.main()
    
