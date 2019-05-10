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
        self.new_credential = Credential("Bright","Mukonesi","muko12")
    def test_init(self):
        '''
        test_init checks if the object is initialised properly
        '''
        self.assertEqual(self.new_credential.first_name,"Bright")
        self.assertEqual(self.new_credential.second_name,"Mukonesi")
        self.assertEqual(self.new_credential.password,"muko12")
if __name__ == '__main__':
    unittest.main()
