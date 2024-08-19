#  office managment - create tables
#  OM010
import sqlite3
def main():
    print('create room table')
    conn = sqlite3.connect('E:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE room (roomid TEXT PRIMARY KEY NOT NULL,
                    phone INTEGER,
                    staffcount INTEGER,
                    notes TEXT)''')

    print('room table created')
    print('\ncreate instructor table')
    conn.commit()
    
    cur.execute('''CREATE TABLE instructor (instructorid TEXT PRIMARY KEY NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    middlename TEXT,
                    status TEXT,
                    keys BOOLEAN,
                    notes TEXT)''')

    print('instructor table created')
    conn.commit()
    
    print('\ncreate room assignment table')
    cur.execute('''CREATE TABLE assignoffice (aonum INTEGER PRIMARY KEY NOT NULL,
                    roomnumber TEXT,
                    instructorid TEXT,
                    notes TEXT)''')

    print('room assignment table created')
    conn.commit()

    print('\ncreate key table')
    cur.execute('''Create TABLE thekey (keyid TEXT PRIMARY KEY NOT NULL,
                    roomnum TEXT,
                    numkey INTEGER,
                    notes TEXT)''')

    print('key table created')
    conn.commit()
    

    print('\ncreate key assign table')
    cur.execute('''Create TABLE assignkey (assignid INTEGER PRIMARY KEY NOT NULL,
                    roomnumber TEXT,
                    roomkey TEXT,
                    notes TEXT)''')

    print('key assign table created')
    conn.commit()

 
    conn.close()

    return
if __name__ == '__main__':
    main()

