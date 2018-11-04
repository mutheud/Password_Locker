class Credentials:

    credentials_list =[]

    def __init__(self,firstname,lastname,phone_number,email,password):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email
        self.password = password

        # print(firstname)
    def save_credentials(self):

        Credentials.credentials_list.append(self)

    # def delete_credentials(self):

    #     Credentials.credentials_list.remove(self)

    # @classmethod
    # def find_by_email(cls,email):
    #     for password in cls.credentials_list:
    #         if password.email == email:
    #             return password

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list
        
    