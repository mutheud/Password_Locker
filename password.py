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

    
    
    