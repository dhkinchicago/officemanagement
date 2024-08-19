# OM099
#  print all tables to output
import sqlite3

def room(cur) -> None:
    print('\n------------------ room ------------------')
    dbsel = "SELECT * FROM room"
    cur.execute(dbsel)
    results = cur.fetchall()
    for line in results:
        print (line)
    print('-'*20)
    
def instructor(cur):        
    print('\n------------------ instructor ------------------')    
    dbsel = "SELECT * FROM instructor"
    cur.execute(dbsel)
    results = cur.fetchall()
    for line in results:
        print (line)
    print('-'*20)
    
def office(cur):
    print('\n------------------ room assignment ------------------') 
    dbsel = "SELECT * FROM assignoffice"
    cur.execute(dbsel)
    results = cur.fetchall()
    for line in results:
        print (line)
    print('-'*20)
    
def thekey(cur):
    print('\n------------------ key ------------------') 
    dbsel = "Select * from thekey"
    cur.execute(dbsel)
    results = cur.fetchall()
    for line in results:
        print (line)    
    print('-'*20)
    
def assignkey(cur):    
    print('\n------------------ key assign ------------------') 
    dbsel = "Select * from assignkey"
    cur.execute(dbsel)
    results = cur.fetchall()
    for line in results:
        print (line)
    print('-'*20)
     
def showmenu():
    desc=[' Room',' Instructor',' Office Assignment',' Key',
               ' Key Assignment ', ' ALL', ' QUIT']
    y=1
    for x in desc:
        if y==len(desc):
            print('\nQ   ',x)
        else:
            print(y,"   ",x)
        y=y+1

def menu(cur):
    sel ='0'
    showmenu()
    themenu={'1':room,'2':instructor,'3':office,'4':thekey,
                     '5':assignkey,'9': quit}
    while sel.upper() != 'Q':
        sel = input(' \nSelect 1,2,3,4,5,6,9 --> ')
        if  sel=='9':
            return
        if sel =='6':
            for x in range (1,6,1):
                themenu[str(x)](cur) 
        else:
            if sel in themenu:
                themenu[sel](cur)
            else:
                print('\nInvalid choice, try again\n\n')
        showmenu()
 
# --------------------------------------------------
#  main program
# ---------------------------------------------------
def om099():
    ans='y'
    print('contents of tables or selected table')
    conn = sqlite3.connect('E:/DATA6/CCC-wright/OfficeMGMT/officemgmt.db')
    cur = conn.cursor()
    
    while ans.upper()=='Y':
        menu(cur)
        ans = input('Run again y/n : ')
        
    print('\n done')
    conn.commit()
    conn.close()   
# --------------------------------------------------------------
if __name__ == '__main__':
    om099()
# -------------------------------------------------------------
