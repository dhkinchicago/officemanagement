# om095
# print selected table to output

import sqlite3

pgmitems=['']*10
#  0  - connect    conn
#  1 -  cursor   cur
#  2 -  error code

# -----------------------------------
#   connect to database
# -----------------------------------
def getdb():
    try:
        pgmitems[0] = sqlite3.connect('E:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
        pgmitems[1] = pgmitems[0].cursor()
        print('connect to database good\n')
        pgmitems[2] = 0
    except:
        print('error connectiong to database')
        pgmitems[2] = 1
    return

# --------------------------------
#  print room table
# -------------------------------
def roomtable():
    print('\n------------------ room ------------------')
    dbsel = "SELECT * FROM room"
    pgmitems[1].execute(dbsel)
    results = pgmitems[1].fetchall()
    for line in results:
        print (line)
    return

# -------------------------------------
# print instructor table
# --------------------------------------
def instructor():
    print('\n------------------ instructor ------------------')    
    dbsel = "SELECT * FROM instructor"
    pgmitems[1].execute(dbsel)
    results = pgmitems[1].fetchall()
    for line in results:
        print (line)
    return

# ------------------------------------------
#  print room / instructor table
# ------------------------------------------
def roomassign():
    print('\n------------------ room assignment ------------------') 
    dbsel = "SELECT * FROM assignoffice"
    pgmitems[1].execute(dbsel)
    results = pgmitems[1].fetchall()
    for line in results:
        print (line)
    return

# -------------------------------------------------
# print key table
# -----------------------------------------------
def keytable():
    print('\n------------------ key ------------------') 
    dbsel = "Select * from thekey"
    pgmitems[1].execute(dbsel)
    results = pgmitems[1].fetchall()
    for line in results:
        print (line)    
    return

# ----------------------------------------------------------
# print key / romm assignment table
# --------------------------------------------------
def keyassign():
    print('\n------------------ key assign ------------------') 
    dbsel = "Select * from assignkey"
    pgmitems[1].execute(dbsel)
    results = pgmitems[1].fetchall()
    for line in results:
        print (line)
    return

# -------------------------------------------------------
#    show menu choices
# -------------------------------------------------------
def showmenu():
    desc=['Room','Instructor','Room Assignment','Key','Key Assignment','QUIT']
    y=1
    for x in desc:
        if y==len(desc):
            print('\nQ   ',x)
        else:
            print(y,"   ",x)
        y=y+1
    return

# ---------------------------------------------------------
# close database
# ---------------------------------------------------------
def closedb():
    pgmitems[0].commit()
    pgmitems[0].close()
    print('\ndatabase closed')
    return

# ----------------------------------------------------------
# menu processing
# ---------------------------------------------------------
def menu() -> None:
    """
    display the menu loop
    :return:
    """
    sel ='0'
    showmenu()
    themenu={'1':roomtable,'2':instructor,'3':roomassign,'4':keytable,'5':keyassign,'Q':closedb}
    while sel.upper() != 'Q':
        sel = input(' \nSelect 1,2,3,4,5 or Q --> ')
        if sel.upper() in themenu:
            themenu[sel.upper()]()
        else:
            print('\nInvalid choice, try again\n\n')
            showmenu()
    return

#----------------------------------------------------
# start of program
# --------------------------------------------------
def om095() -> None:
    getdb()
    if pgmitems[2] == 0:
        menu()
    else:
        print(' program terminated due to errors')
    print('\n done')

# ---------------------------------------------------------------------
if __name__ == '__main__':
    om095()
# --------------------------------------------------------------------
