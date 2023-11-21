import os
from tabulate import tabulate
from conection import *
from contact import *

con = connect()
create_table(con)

def start():
    os.system('cls')
    print('SELECT AN OPTION:\n')
    print('\t1.- Add contact')
    print('\t2.- Show all contacts')
    print('\t3.- Search contact')
    print('\t4.- Modify contact')
    print('\t5.- Delete contact')
    print('\t6.- Exit aplication\n')
    opc = input('Choose an option: \n')

    if opc == '1':
        new_contact()
    elif opc == '2':
        show_contacts()
    elif opc == '3':
        search_contact()

def show_contacts():
    data = show_data()
    headers = ['ID', 'NAMES', 'LASTNAMES', 'ENTERPRISE', 'PHONE NUMBER', 'EMAIL', 'ADDRESS', 'REGISTER_DATE']
    table = tabulate(data, headers, tablefmt='fancy_grid')
    print(table)

def new_contact():
    name = input('Enter name: ')
    last_name = input('Enter lastname: ')
    enterpise = input('Enter name enterpise: ')
    phone = input('Enter phone number: ')
    email = input('Enter email: ')
    address = input('Enter address: ')

    res = register(name,last_name,enterpise,phone,email,address)    
    print(res)
    
def search_contact():
    id_contact = input("Enter id of contact: ")
    data = search(id_contact)
    headers = ['ID', 'NAMES', 'LASTNAMES', 'ENTERPRISE', 'PHONE NUMBER', 'EMAIL', 'ADDRESS', 'REGISTER_DATE']
    table = tabulate(data, headers, tablefmt='fancy_grid')
    print(table)


start()