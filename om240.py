# ----------------------------------------------
#  OM240  key Maintenance
#
#     version control
#     -------------------------
#  version .1 12/27/23
#
# ------------------------------
from tkinter import *
import sqlite3
from os.path import isfile
from tkinter import messagebox
import tkinter.font  as font
# -----------------------------
# global variables
pgmitems =['']*25
#     0 = textbox 0   key number to find
#     1 = textbox 1   key number
#     2 = textbox 2   room number
#     3 = textbox 3   number of keys
#     4 = textbox 4   notes
#     5 = not used
#     6 = not used
#     7 = textbox 6   add/change/delete message
#     8 -- not used
#     9 -- found record (used for update) ---
#   10 = textbox  error message  (call showmsg)
#   11 = textbox title                    (call showmsg)
#   12 = DB cursor
#   13  = conn   
#   14 =  find button
#   15 =  Add button
#   16 =  update button
#   17 =  delete button
#   18 =  clear button
#   19 =  quit button
#   20 =  error code
#   21 =  mesage box code
#   22 - 25  -- not used
# --------------------------------------------------------
#   error codes and messages
# -----------------------------------------------
e1dt= {1:"Required fields not filled in",
                2:"key number not filled in",
                3:"room number not filled in",
                4:"room number not in database",
                10:"database error - insert failed",
                11:" Database error - update failed",
                12:"database error - delete failed",
                98:"no changes detected",               # not an error used by update routine
                99:"unknown error"}
# ---------------------------------------------------------------------
wlist=[]        # work list  for window elements
# ---------------------------------------------------------------------
# ----------------------------------------------------------------------
#  Dictionaries for labels and text box
# ---------------------------------------------------------------------
#  Label dictionary   usw with wlist
#   title = NONE or KEY  -- special processing
#   key:title,fg color,bg color, font style, font size,x position, y postion
ldic={0:["Key # Search","black","yellow",'"Arial Bold"',16,100,100],
          1:["Key Number","black","yellow",'"Arial Bold"',16,10,150],
          2:["Room Number","black","yellow",'"Arial Bold"',16,10,200],
          3:["# of keys","black","yellow",'"Arial Bold"',16,10,250],
          4:["Notes","black","yellow",'"Arial Bold"',16,10,300]
           }
#         
# ----------------------------------------------------------------------
# text box disctionary    use with wlist
#  key:width, font style, font size, x postion, y position
tdic = {0:[12,'"Arial bold"',16,250,100],      # key # search
            1:[10,'"Arial bold"',16,150,150],      # key number
            2:[10,'"Arial bold"',16,150,200],      # room number
            3:[5,'"Arial bold"',16,150,250],      # number of keys
            4:[20,'"Arial bold"',16,150,300],        # notes
            5:["NONE",1],                                   # skip    
            6:["NONE",1],                                   #  skip
            7:[40,'"Arial bold"',16,25,500]         #  action messages 
            }
#
# ---------------------------------------------------------------------
#  to do: database connection
#     local:
#       get path and database from profile
#       path (ex:  c:\data\officemgmt )  folder
#       database -- semester (ex: spring2024)
#
#    network:
#       logon and password
#       get rest of info from profile 
#
#    profile:
#       either a flat file or datbase file
#       flat file:
#           local or network
# -------------------------------------------------------
#  --- >note: datbase and path hard coded <----
def obtaindatabase():
    # get path and databse from profile
    
    #dbdata = "not a database"
    dbpath='E:/DATA6/CCC-wright/OfficeMGMT/'
    dbname='officemgmt.db'
    dbdata = dbpath + dbname
    #dbdata='C:/temp/officemgmt.db'
    
    #print(dbdata)
    tc = dbdata.find(":") 
    if not isfile(dbdata) or tc == 0:
        msg= 'Data Base: '+ dbdata
        pgmitems[10] = 'Data Base: '+ dbdata
        pgmitems[11] = "DATABASE NOT FOUND"
        showmsg()
    else:
        try:
            conn = sqlite3.connect(dbdata)
            cur = conn.cursor()
            pgmitems[12]=cur
            pgmitems[13]=conn
        except:
             pgmitems[12] =''
             pgmitems[13] =''
    return

# ------------------------------------------
#  message box
#    note first three characters is switch
#       which indicate which message box to display
#       pgmitems[21]  message box responce
# -------------------------------------------
def showmsg():
    if pgmitems[11][:3] == 'ZZZ':
        pgmitems[21]=messagebox.askyesno(pgmitems[11][3:], pgmitems[10])
    else:
        messagebox.showerror(pgmitems[11], pgmitems[10])
        clrit()
    return

# ---------------------------------------
# clear text boxes
# code == null - clear all boxes
# --------------------------------------------
def clrit():
    pgmitems[1]["state"] = "normal" 
    pgmitems[1].delete(0,"end")
    pgmitems[2].delete(0,"end")
    pgmitems[3].delete(0,"end")
    pgmitems[4].delete(0,"end")
    pgmitems[7].delete(0,"end")
    pgmitems[10]=''
    pgmitems[11]=''
    btnshide()
    pgmitems[2].configure(bg="white")
    pgmitems[4].configure(bg="white")
    pgmitems[7].insert(0,"")
    pgmitems[20] = 0
    pgmitems[21] =''
    return

# ---------------------------------------
#  create window
# --------------------------------------
def createwindow():
    mainwin = Tk()
    mainwin.title("Office Management")
    mainwin.geometry('700x600+300+300')
    mainwin["bg"] = 'yellow'
    return  mainwin

# ---------------------------------------
#  screen title
# --------------------------------------
def labeltxtx(mainwin):
    txt01 =Label(mainwin, text="OM400",
                         fg="black",bg='yellow',font=("Arial Bold", 8))
    txt01.place(x=0, y=0) 
    txt02 = Label(mainwin, text="Key Maintenance",
                  fg = "black", bg = 'yellow',  font=("Arial Bold", 20))
    txt02.place(x=100,y=0)
    return

# -----------------------------------------
#  Close the window and database
# -----------------------------------------
def CloseWindow(mainwin):
    if pgmitems[13] != '':
        pgmitems[13].commit()
        pgmitems[13].close()
    mainwin.destroy()

# -----------------------------------------
#  hide all buttons
# ----------------------------------------
def btnshide():
    pgmitems[15].place_forget()     # add
    pgmitems[16].place_forget()     # update
    pgmitems[17].place_forget()     # delete
    if pgmitems[20] == 98:               # if update (no update found, leave claer button)
        pgmitems[20] = 0
    else:
        pgmitems[18].place_forget()     # clear
    return

# ---------------------------------------------
#  acivate update & delete button
# ------------------------------------------------
def btnsud():
    pgmitems[16].place(x=400,y=250)   # update button
    pgmitems[17].place(x=400,y=300)   # delete button
    pgmitems[18].place(x=400,y=400)   # clear button
    return

# ----------------------------------------------
#  ACTIVATE ADD BUTTON
# -------------------------------------------
def btnadd():
    pgmitems[15].place(x=400,y=175)   # add button
    pgmitems[18].place(x=400,y=400)   # clear button
    pgmitems[2].configure(bg="lightgreen")       # room number
    #pgmitems[3].configure(bg="lightgreen")       # number of keys
    #pgmitems[4].configure(bg="lightgreen")       # notes  
    pgmitems[7].insert(0,"Required information in green")
    pgmitems[1]["state"] = "disabled"
    return

# -----------------------------------------
#   validate key number
# ---------------------------------------------
def auditkey(kynum):
    msg = ''
    if kynum=='' or kynum.isspace():
        msg= 'enter a room number'
    return msg

# ----------------------------------------
#  find key
# ---------------------------------------
def keyfind():
    btnshide()
    clrit()
    kynum=pgmitems[0].get()
    pgmitems[0].delete(0,"end")
    kynum = kynum.upper()
    pgmitems[1].insert(0,kynum)
    pgmitems[1]["state"] = "disable"
    msg=auditkey(kynum)
    if  msg !='':
        pgmitems[11] = msg
        pgmitems[10] = "Key NUMBER INVALID"
    else:
        try:
            #print(sidnum)
            rsel = "Select * from thekey where keyid = "
            rsel=rsel + '"' + kynum + '"'
            #print('rsel ',rsel)
            pgmitems[12].execute(rsel)
            results = pgmitems[12].fetchall()
            if len(results) == 0:
                btnadd()
            else:
                for theky in results:
                        pgmitems[9] = theky
                        if theky[1] is not None:
                            pgmitems[2].insert(0,theky[1])  #room num
                        if theky[2] is not None:
                            pgmitems[3].insert(0,theky[2])  # num of keys
                        if theky[3] is not None:
                            pgmitems[4].insert(0,theky[3])  # notes
                        btnsud()
        except:
            pgmitems[11] = " UNKNOWN ERROR with key number"
            pgmitems[10] = "ROOM NUMBER ERROR"
    if pgmitems[11] != "":
        showmsg()
    return

# ---------------------------------------
#   Add key number
#    >>>> room number must be on the database
#             to be written
#
# --------------------------------------
def keyadd():
    pgmitems[9] = ''      # clear rec
    pgmitems[20]=0     # reset error code
    pgmitems[7].delete(0,"end")
    keyid=pgmitems[1].get()         # key number
    roomid = pgmitems[2].get()     # get room number       
    numofkey =pgmitems[3].get()     # get number of keys
    if roomid ==  '' or roomid.isspace():
        pgmitems[20] = 3
    #    look up room number
    #    if room number not of database  set error code 4
    #    pgmitems[20] = 4        room number not on database
 
    if pgmitems[20] ==0:
        #  check number of keys if error default 1
        try:
            if numofkey == '' or numofkey.isspace():
                numofkey = '1'
            else:
                if not numofkey.isnumeric():
                    numofkey ='1'
        except:
            numofkey = '1'
            
        insrec="INSERT INTO thekey (keyid,roomnum,numkey)"
        insrec=insrec + ' VALUES ('  +   '"' + keyid + '"' + ',' +  '"' + roomid +  '"' +  ',' +  numofkey
        insrec = insrec +')'
        #print(insrec)
        try:
            cur=pgmitems[12]
            cur.execute(insrec)
            pgmitems[7].insert(0,keyid +' added to database')
            pgmitems[13].commit()
            
        #except Exception as e:
            #print(e)
            #pgmitems[20] = 10
        except:
            pgmitems[20] = 10

    if pgmitems[20]>0:
        pgmitems[7].insert(0,e1dt[pgmitems[20]])
    pgmitems[15].place_forget()  
    return

# ---------------------------------------
#   update room
#   pgmitems[9] has current (old) data
#
#   convert to key room num, number of keys and notes
# --------------------------------------
def keyupd():
#  can be changed:  room number, num of keys and notes
#  room number can not be change if assign to instructor
#   or assigned to room
    updrec=''
    olddata = pgmitems[9]
  
    if olddata[1] != None:
        oldroomnum = olddata[1]          # room number
    else:
        oldroomnum=''
    if olddata[2] != None:
        oldnumofkeys = olddata[2]        # number of keys
    else:
        oldnumofkeys=''
    newnumofkeys = pgmitems[2].get().strip()       #  room number
    newroomnum=pgmitems[3].get().strip()           #  number of keys   
    #  any changes?    
    if oldroomnum ==newroomnum and oldnumofkeys==newnumofkeys:
       pgmitems[7].insert(0,olddata[0]+' NO Changes detected')
       pgmitems[20] =98
       btnshide()
    else:
       #  check required fields are not blank (room number & number of keys)
            try:
                uall=''
                u2=''
                u3=''   
                updrec = 'UPDATE thekey'
                updrec = updrec + ' Set '
                if oldnumofkeys != newnumofkeys:    # number of keys
                    u3 = ' roomnum = '+ "'" + newnumofkeys + "'"
                if oldroomnum != newroomnum:     # room number
                    u2 = ' numkey = ' + "'" + newroomnum + "'"
                if len(u2) != 0:
                    if len(uall) ==0:
                        uall = u2
                    else:
                        uall =uall + ',' + u2
                if len(u3) != 0:
                    if len(uall) ==0:
                        uall = u3
                    else:
                        uall =uall + ',' + u3
                updrec = updrec + uall
                updrec = updrec + ' WHERE keyid = ' + "'"  + str(pgmitems[1].get()) + "'"
                print('updrec= ',updrec)
                cur=pgmitems[12]
                cur.execute(updrec)
                pgmitems[13].commit()
                idnum = pgmitems[1].get()
                clrit()
                pgmitems[7].insert(0,idnum +' Record UPDATED')
            except:
                pgmitems[20] =11

    if pgmitems[20]>0:
        pgmitems[7].insert(0,e1dt[pgmitems[20]])
    pgmitems[15].place_forget()  
    return

# ---------------------------------------
#   delete key
#   delete critieria 
#           cannot delete if still assigned to room
#
#   convert to key
# --------------------------------------
def keydel():
#  delete key from database
#  conditions:
#             cannot be assigned to room (room assign table)
#             cannot be assigned to instructor
    sroomnum=pgmitems[1].get()
    try:
        # check if instructor is assigned an office
        usel = "Select * from assignoffice where roomnumber = " +sroomnum
        #print(usel)
        pgmitems[12].execute(usel) 
        oresults = pgmitems[12].fetchall()
        if len(oresults)==0:
            pgmitems[11] = "ZZZ Delete from Database validate"
            pgmitems[10] = " Are you sure you want to DELETE ??"
            showmsg()
            if pgmitems[21] == True:
                delrec= "DELETE FROM room WHERE instructorid = "+ sroomnum
                #print(delrec)
                cur=pgmitems[12]
                cur.execute(delrec)
                clrit()
                pgmitems[7].insert(0,idnum+' *** DELETED *** from database')
                pgmitems[13].commit()  
            else:
                pgmitems[7].insert(0,'Deletion Canceled')
        else:
            pgmitems[7].insert(0,'Insturctor assign to an office, cannot delete')
            
    except:
            pgmitems[20] =12
    if pgmitems[20]>0:
        pgmitems[7].insert(0,e1dt[pgmitems[20]])
    pgmitems[15].place_forget()  
    return

# ---------------------------------------
#  Create the buttons
# --------------------------------------
def btns(mainwin):
    #  find button
    cmdfind = Button(mainwin, text="FIND",
                    font=("Arial Bold", 20),  
                   command=lambda : keyfind())
    cmdfind.place(x=425,y=75)
    pgmitems[14] = cmdfind
    #   Add button
    cmdadd = Button(mainwin, text="Add",
                    font=("Arial Bold", 16),  
                   command=lambda : keyadd())
    cmdadd.place(x=400,y=175)
    pgmitems[15] = cmdadd
    #  update button
    cmdupd = Button(mainwin, text="Update",
                    font=("Arial Bold", 16),  
                   command=lambda : keyupd())
    cmdupd.place(x=400,y=250)
    pgmitems[16] = cmdupd
    #  delete button
    cmddel = Button(mainwin, text="Delete",
                    font=("Arial Bold", 16),  
                   command=lambda : keydel())
    cmddel.place(x=400,y=300)
    pgmitems[17] = cmddel
    #   clear button
    cmdclr = Button(mainwin, text="Clear",
                    font=("Arial Bold", 16),  
                   command=lambda : clrit())
    cmdclr.place(x=400,y=400)
    pgmitems[18] = cmdclr
    #  quit button
    cmdquit = Button(mainwin, text="QUIT", 
                   fg="red",
                   font=("Arial Bold", 20),                                      
                   command=lambda : CloseWindow(mainwin))
    cmdquit.place(x=525,y=500)
    pgmitems[19] = cmdquit
    btnshide()
    return

# ---------------------------------------------------------------------
#  place labels and textboxes on window
# ------------------------------------------------------------------------
def buildwindow(mainwin):
    e=len(ldic)
    for w in range(0,e,1):
        wlist = ldic[w]
        if wlist[0] != "NONE":
            txtboxlbl = Label(mainwin, text=wlist[0],
                    fg = wlist[1], bg = wlist[2], font=(wlist[3], wlist[4]))
            txtboxlbl.place(x=wlist[5],y=wlist[6])
    e=len(tdic)
    for w in range(0,e,1):
        wlist=tdic[w]

        if wlist[0] != "NONE":
            pgmitems[w] = Entry(mainwin,width=wlist[0],
                                font=(wlist[1], wlist[2]))
            pgmitems[w].place(x=wlist[3],y=wlist[4])
        pgmitems[0].focus_set()
        # end of loop
    return
 

# ---------------------------------------
#  main line code
# --------------------------------------
def om400():
    (mainwin) = createwindow()
    labeltxtx(mainwin)
    buildwindow(mainwin)
    btns(mainwin)
    obtaindatabase()
    if pgmitems[12]== '':    # have database?
        pgmitems[14].place_forget()      # find button
        pgmitems[10] = "SELECT Quit button to Exit"
        pgmitems[11] = " DATABASE ERROR"
        showmsg()
    #else:
        #print('database is open')
    mainloop()
# ---------------------------------------
#  start point of program
# --------------------------------------
# --------------------------------------------------------------
if __name__ == '__main__':
    om400()
# -------------------------------------------------------------
# ---------------------------------------
#  end of program
# --------------------------------------

