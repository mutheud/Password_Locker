class User:
    user_list = []

    def __init__(self,firstname,lastname,phone_number,email,password):

        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def save_account(self):
        User.user_list.append(self)

    def delete_account(self):
        User.user_list.remove(self)

    @classmethod
    def find_by_number(cls,phone_number):

        for user in cls.user_list:
            if user.phone_number == phone_number:
                return user
    @classmethod
    def account_exist(cls,phone_number):

        for user in cls.userlist:
            if user.phone_number == phone_number:
                return True

        return False

    @classmethod
    def display_all_account(cls):
        return cls.user_list
