# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: Contacts Searcher
# Version: 1.0: Base version by author

import csv


class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Phone:
    def __init__(self):
        self.contacts = []

    def load_contacts_from_csv(self, file_name):
        with open(file_name, newline='') as contacts_file:
            reader = csv.DictReader(contacts_file, delimiter=',')
            self.contacts = [PhoneContact(contact['Name'], contact['Phone']) for contact in reader]

    def search_contacts(self, phrase):
        for contact in self.contacts:
            if phrase.lower() in contact.name.lower() or phrase.lower() in contact.phone:
                print('Search Results Found. Contact: ', contact.name, ' (', contact.phone, ')', sep='')


if __name__ == "__main__":
    _phone = Phone()
    _phone.load_contacts_from_csv("contacts.csv")
    input_phrase = input("Search contacts: ")
    _phone.search_contacts(input_phrase)
