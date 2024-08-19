#  room table populate
#  OM020
import sqlite3
def main():
    print('insert data into room table')
    conn = sqlite3.connect('E:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
    cur = conn.cursor()

    cur.execute('''INSERT INTO room (roomid)
                    VALUES ("L335" )''')
    cur.execute('''INSERT INTO room (roomid, phone)
                    VALUES ("L352", 8331)''')
    cur.execute('''INSERT INTO room (roomid, phone,staffcount)
                    VALUES ("L357", 8532, 2)''')
    cur.execute('''INSERT INTO room (roomid)
                    VALUES ("L359" )''')
    cur.execute('''INSERT INTO room (roomid)
                    VALUES ("L360" )''')
    cur.execute('''INSERT INTO room (roomid)
                    VALUES ("L361" )''')
    cur.execute('''INSERT INTO room (roomid)
                    VALUES ("L368" )''')
    cur.execute('''INSERT INTO room (roomid, phone)
                    VALUES ("L369",8333 )''')
    cur.execute('''INSERT INTO room (roomid, phone,staffcount)
                    VALUES ("L370",8335 , 0)''')
    cur.execute('''INSERT INTO room (roomid, phone,staffcount)
                    VALUES ("L371", 8313, 0)''')
    cur.execute('''INSERT INTO room (roomid)
                    VALUES ("L374")''')

    
    print('insert done')
    conn.commit()
    conn.close()

    return

if __name__ == '__main__':
    main()
