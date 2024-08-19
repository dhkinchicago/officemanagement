#  instructor table update
import sqlite3
def main():
    print('update data into instructor table')
    conn = sqlite3.connect('E:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
    cur = conn.cursor()
    idn = '195195195'
    mn = 'testmiddle'
    usql='Select * from instructor WHERE instructorid ='
    usql = usql + idn
    cur.execute(usql)
    results = cur.fetchall()
    print('---before')
    print (results)
    
    usql='UPDATE instructor '
    usql = usql + 'SET middlename = ' + "'" + mn + "'"
    usql = usql + ' WHERE instructorid = ' + idn
    print(usql)
    usql = 'UPDATE instructor  Set middlename = '
    a = 'MM123'
    usql = usql + "'" + a + "'" + ' WHERE instructorid = 195195195'
    print(usql)
    cur.execute(usql)
    conn.commit()
    usql='Select * from instructor WHERE instructorid ='
    usql = usql + idn
    cur.execute(usql)
    results = cur.fetchall()
    print('---after')
    print (results)
    
    conn.commit()
    conn.close()

    return

if __name__ == '__main__':
    main()
