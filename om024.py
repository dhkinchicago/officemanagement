#  room assignment table populate
# OM024
import sqlite3
def main():
    print('insert data into room assignment table')
    conn = sqlite3.connect('E:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
    cur = conn.cursor()

    cur.execute('''INSERT INTO assignoffice (aonum, roomnumber, instructorid)
                    VALUES (1,"L374",'000001234' )''')
    cur.execute('''INSERT INTO assignoffice (aonum, roomnumber, instructorid)
                    VALUES (2,"L352", '000065471')''')
    cur.execute('''INSERT INTO assignoffice (aonum, roomnumber, instructorid)
                    VALUES (3,"L357", '000009876')''')
    cur.execute('''INSERT INTO assignoffice (aonum, roomnumber, instructorid)
                    VALUES (4,"L357",'000012345' )''')
    cur.execute('''INSERT INTO assignoffice (aonum, roomnumber, instructorid)
                    VALUES (5,"L360",'195195195' )''')
    cur.execute('''INSERT INTO assignoffice (aonum, roomnumber, instructorid)
                    VALUES (6,"L361",'000005678' )''')


    
    print('insert done')
    conn.commit()
    conn.close()

    return

if __name__ == '__main__':
    main()
