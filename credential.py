class Credential:
    '''
    class that generates new instaces of credentials information
    '''
    credential_list = [] #credential list
    def save_credential(self):
        '''
        save_credential method saves object in credential list
        '''
        Credential.credential_list.append(self)
    def __init__(self,account_name,password):
        self.account_name = account_name
        self.password = password
    @classmethod
    def display_user_credentials(cls):
        '''
        method that returns credentials of a user
        '''
        return cls.credential_list
