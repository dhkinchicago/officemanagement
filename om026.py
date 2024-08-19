#  key  table populate
#   OM026
import sqlite3
def main():
    print('insert data into key table')
    conn = sqlite3.connect('E:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
    cur = conn.cursor()

    cur.execute('''INSERT INTO thekey (keyid, roomnum)
                    VALUES ('299',"L357" )''')
    cur.execute('''INSERT INTO thekey (keyid, roomnum)
                    VALUES ('340',"L374" )''')
    cur.execute('''INSERT INTO thekey (keyid, roomnum)
                    VALUES ('BH34',"L374" )''')
    cur.execute('''INSERT INTO thekey (keyid, roomnum)
                    VALUES ('502',"L369" )''')
    
    print('insert done')
    conn.commit()
    conn.close()

    return

if __name__ == '__main__':
    main()
