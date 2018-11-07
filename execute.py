#!/usr/bin/env python3.6
from user import User
from password import Credentials


def create_credentials(accountname,firstname,lastname,phone_number,email,password):
    new_credentials = Credentials(accountname,firstname,lastname,phone_number,email,password)
    return new_credentials

def save_credentials(password):
    password.save_credentials()

def delete_credentials(password):
    password.delete_credentials()

def find_credentials(password):
    return Credentials.find_by_email(email)

def credential_exist(phone_number):

    return Credentials.credential_exist(phone_number)

def display_credentials():
    
    return Credentials.display_credentials()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()



    print(f"Hello {user_name}. what would you like to do?")

    print('\n')

    while True:
                    print("Use these short codes : cc - create new credential, dc - display credentias, fc -find a credentia, ex -exit the credentials list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("Account name ....")
                            accountname = input()

                            print ("First name ....")
                            firstname = input()

                            print("Last name ...")
                            lastname = input()

                            print("Phone number ...")
                            phone_number = input()

                            print("Email address ...")
                            email = input()

                            print("password...")
                            password = input()

                            save_credentials(create_credentials(accountname,firstname,lastname,phone_number,email,password))
                            print ('\n')
                            print(f"New Contact {firstname} {lastname} created")
                            print ('\n')
                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for password in display_credentials():
                                            print(f"{firstname} {password.lastname} .....{password.phone_number}")
                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_phone_number = input()
                            if credential_exist(search_phone_number):
                                    search_credentials = find_credentials(search_password)
                                    print(f"{search_credentials.first_name} {search_credentials.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_credentials.phone_number}")
                                    print(f"Email address.......{search_credentials.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()

