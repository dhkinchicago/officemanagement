# Create database
#  om001
import sqlite3
def main():
    print('Create database')
    #conn = sqlite3.connect('e:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
    #conn = sqlite3.connect('e:/dbtemp/static.db')
    cur = conn.cursor()
    conn.commit()
    print('database created')
    conn.close()
    return
if __name__ == '__main__':
    main()
