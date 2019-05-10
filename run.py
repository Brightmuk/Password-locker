from user import User
from credential import Credential

def create_credential(account_name,password):
    '''
    function to create a new credential
    '''
    new_credential = Credential(account_name,password)
    return new_credential
def save_credential(credential):
    '''
    function to save a credential
    '''
    credential.save_credential()
def display_credentials():
    '''
    function that dispalys all credentials
    '''
    return Credential.display_credentials()

def create_user(f_name,s_name,password):
    '''
    function to create a new user
    '''
    new_user = User(f_name,s_name,password)
    return new_user
def save_users(user):
    '''
    function to save a user
    '''
    user.save_user()
def display_users():
    '''
    function that dispalys all signed up users
    '''
    return User.display_users()
def intro():
    print("Hey there! Welcome to Password Locker")
    print('\n')
    print("Please sign up for an accout to enjoy services")

    while True:
        print("Use these short codes : su - sign up, lg - login")
        short_code = input().lower()
        if short_code == 'su':
            print("New User")
            print("-"*9)

            print("Enter you first name...")
            f_name = input()

            print("Enter your second name...")
            s_name=input()

            print("Please confirm your password...")
            password=input()



            save_users(create_user(f_name,s_name,password))
            print('\n')
            print(f"Congratulations {f_name} {s_name}, you now have an account")
            print('\n')
        elif short_code == 'lg':
            print("Enter the name of your registered account")
            account_name = input()
            print("Enter your password")
            authentification = input()
            while True:
                print("cc-To create new credential, ex-exit account, vc-To view all your credentials")
                short_code=input().lower()
                if short_code == 'cc':

                    print("Enter account name")
                    account_name = input()
                    print("Enter its password")
                    password = input()
                    print(f"{account_name} has been saved")

                    save_credential(create_credential(account_name,password))
                elif short_code == 'vc':
                    if display_credentials:
                        print("Here is a list of all your accounts and passwords")
                        for credential in display_credentials():
                            print(f"{credential.account_name} {credential.password}")
                            
                elif short_code == 'ex':
                    print("You have exited your account")
                    break
                else:
                    print("Please use the codes provided")

        else:
            print("Ok well.")
            break
if __name__ == '__main__':

    intro()
