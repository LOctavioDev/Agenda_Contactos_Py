import os
from conection import *

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
    input('Choose an option: ')

start()