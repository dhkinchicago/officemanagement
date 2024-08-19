#  instructor table populate
#  OM022
import sqlite3
def main():
    print('insert data into instructor table')
    conn = sqlite3.connect('E:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
    cur = conn.cursor()

    cur.execute('''INSERT INTO instructor (instructorid,firstname,lastname,status)
                    VALUES ('000001234',"first001","last001","A")''')
    cur.execute('''INSERT INTO instructor (instructorid,firstname,lastname,status)
                    VALUES ('000005678',"first002","last002","A")''')
    cur.execute('''INSERT INTO instructor (instructorid,firstname,lastname,status)
                    VALUES ('000009876',"first003","last003","F")''')
    cur.execute('''INSERT INTO instructor (instructorid,firstname,lastname,status)
                    VALUES ('195195195',"first004","last004","A" )''')
    cur.execute('''INSERT INTO instructor (instructorid,firstname,lastname,status)
                    VALUES ('000012345',"first005","last005","A" )''')
    cur.execute('''INSERT INTO instructor (instructorid,firstname,lastname,status)
                    VALUES ('000098765',"first006","last006","A" )''')
    cur.execute('''INSERT INTO instructor (instructorid,firstname,lastname,status)
                    VALUES ('000065471',"first007","last007","F" )''')
   

    
    print('insert done')
    conn.commit()
    conn.close()

    return

if __name__ == '__main__':
    main()
