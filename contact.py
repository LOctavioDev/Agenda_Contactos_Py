from conection import *

def register(name, lastname, enterprise, phone, email, adress):
    try:
        con = connect()
        cursor = con.cursor()
        sql_statement = ''' INSERT INTO tbb_contacto(
                name, last_name, company_name, phone, email, direction) 
                VALUES( ?,?,?,?,?,?) '''
        data = (name, lastname, enterprise, phone, email, adress)
        cursor.execute(sql_statement, data)
        con.commit()
        con.close()
        return 'Register completed'
    except sqlite3.Error as err:
        print(f'Something went wrong {err}')

def show_data():
    data = []
    try:
        con = connect()
        cursor = con.cursor()
        sql_statement = ''' SELECT * FROM tbb_contacto '''
        cursor.execute(sql_statement)
        data = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print(f'Something went wrong {err}')