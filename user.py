class User: 
    user_list = []

    def __init__ (self,firstname,lastname,phone_number,email,password):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def save_contact(self):

        User.user_list.append(self)

        
    