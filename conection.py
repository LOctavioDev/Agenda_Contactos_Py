import sqlite3

def connect():
    try:
        conection = sqlite3.connect('contactos.db')
        print('successful conection')
        return conection
    except sqlite3.Error as err:
        print(f'Something went wrong {err}')
        
def create_table(conection):
    cursor = conection.cursor()
    sql_statement = ''' CREATE TABLE IF NOT EXISTS tbb_contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            company_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            register_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    ) '''
    cursor.execute(sql_statement) 
    conection.commit()   