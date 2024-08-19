#  room assignment table populate
import sqlite3
def main():
    print('check sql instructions  room assignment table')
    conn = sqlite3.connect('E:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
    cur = conn.cursor()

 
    print('\n------------------ room assignment ------------------')
    idnum = input('enter id num: ')
    sidnum = '"' + idnum + '"'
    dbsel = "Select * from assignoffice"
    dbsel = dbsel + " where instructorid = " +sidnum
    print(dbsel)
    input('hit enter to continue')
    cur.execute(dbsel)
    results = cur.fetchall()
    print(len(results),'   length of db record')
    for line in results:
        print (line)


    idnum = input('enter id num: ')
    sidnum = '"' + idnum + '"'
    dbsel = "Select instructorid from assignoffice"
    dbsel = dbsel + " where instructorid = " +sidnum
    print(dbsel)
    input('hit enter to continue')
    cur.execute(dbsel)
    results = cur.fetchall()
    for line in results:
        print (line)    
    
    print('\n done')
    conn.commit()
    conn.close()

    return

if __name__ == '__main__':
    main()
