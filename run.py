from user import User

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

            print("Enter your password...")
            password1=input()

            print("Please confirm your password...")
            password=input()

            save_users(create_user(f_name,s_name,password))
            print('\n')
            print(f"Congratulations {f_name} {s_name}, you now have an account")
            print('\n')
        else:
            print("Ok well.")
            break
if __name__ == '__main__':

    intro()
