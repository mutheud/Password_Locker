#!/usr/bin/env python3.6
from password import Credentials

def create_credentials(firstname,lastname,phone_number,email,password):
    new_credentials = Credentials(firstname,lastname,phone_number,email,password)
    return new_credentials

def save_credentials(password):
    password.save_credentials()

def delete_credentials(password):
    password.delete_credentials()

def find_by_email(password):
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

if __name__ == '__main__':
    main()

