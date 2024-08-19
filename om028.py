#  key assign table populate
# om028
import sqlite3
def main():
    print('insert data into key assign table')
    conn = sqlite3.connect('E:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
    cur = conn.cursor()

    cur.execute('''INSERT INTO assignkey (assignid, roomnumber, roomkey)
                    VALUES (1,"L374",'340' )''')
    cur.execute('''INSERT INTO assignkey (assignid, roomnumber, roomkey)
                    VALUES (2,"L357",'299' )''')
    cur.execute('''INSERT INTO assignkey (assignid, roomnumber, roomkey)
                    VALUES (3,"L374",'BH34' )''')


    
    print('insert done')
    conn.commit()
    conn.close()

    return

if __name__ == '__main__':
    main()
