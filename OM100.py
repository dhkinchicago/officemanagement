
# ----------------------------------------------
#  OM100  Room Inquiry
#
#     version control
#     -------------------------
#  version  1 11/04/2023
#
#   change to match other programs
#    screen build, add key lookup
#
# -----------------------------------------------
from tkinter import *
import sqlite3
import os
from os.path import isfile
from tkinter import messagebox
import tkinter.font as font
# -----------------------------
# global variables
pgmitems =['']*25
#     0 = textbox 0 room number to search for
#     1 = textbox 1   room number
#     2 = textbox 2   phone
#     3 = textbox 3   # in room
#     4 = textbox 4    key #
#     5 = textbox 5   notes
#     6 = textbox 6  messages
#     7  -- not used
#     8 = find button
#     9 = listbox  ( instructor list )
#   10 = textbox  error message  (call showmsg)
#   11 = textbox title           (call showmsg)
#   12 = DB cursor
#   13 = conn (connection)
#   14-23 = not used
#   24 = mainwin pointer
# --------------------------------------------------------
# ---------------------------------------------------------------------
# ----------------------------------------------------------------------
#  Dictionaries for labels and text box
# ---------------------------------------------------------------------
#  Label dictionary   usw with wlist
#   title = NONE or KEY  -- special processing
#   key:title,fg color,bg color, font style, font size,x position, y postion
ldic={0:["OM100","black","yellow",'"Arial Bold"',8,0,0],
          1:["Room Inquiry","black","yellow",'"Arial Bold"',30,150,0],
          2:["Enter Room #: ","black","yellow",'"Arial Bold"',16,75,100],
          3:["Room: ","black","yellow",'"Arial Bold"',16,1,150],
          4:["Phone: ","black","yellow",'"Arial Bold"',16,1,200],
          5:["# in room: ","black","yellow",'"Arial Bold"',16,1,250],
          6:["Key # ","black","yellow",'"Arial Bold"',16,1,300],
          7:["Notes:  ","black","yellow",'"Arial Bold"',16,1,375],
          8:["Key # ","black","yellow",'"Arial Bold"',16,1,300]  
           }
#         
# ----------------------------------------------------------------------
# text box disctionary    use with wlist
#  key:width, font style, font size, x postion, y position
tdic = {0:[12,'"Arial bold"',16,250,100],      # room # search
            1:[10,'"Arial bold"',16,100,150],      # room number
            2:[10,'"Arial bold"',16,100,200],      # phone
            3:[5,'"Arial bold"',16,100,250],      # number in room
            4:[15,'"Arial bold"',16,100,300],      # key numbers
            5:[40,'"Arial bold"',16,100,375],        # notes
            6:[40,'"Arial bold"',16,50,450]    #  messages
            }
#
# -------------------------------------------------------------------------------------------
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
            pgmitems[13] = conn
        except:
             pgmitems[12] =''
             pgmitems[13] =''
    return

# ------------------------------------------
#  message box
# -------------------------------------------
def showmsg():
    messagebox.showerror(pgmitems[11], pgmitems[10])
    clrit(pgmitems)
    return

# -----------------------------------------
#   validate room number
# ---------------------------------------------
def auditroom(roomnum):
    msg = ''
    if len(roomnum)==0 or roomnum.isspace():
        msg= 'Room number cannot be blank'
    return msg

# ------------------------------
#  normal text boxes for display
# ---------------------------------
def txtopen():
    pgmitems[1]["state"] = "normal"
    pgmitems[2]["state"] = "normal"
    pgmitems[3]["state"] = "normal"
    pgmitems[4]["state"] = "normal"
    pgmitems[5]["state"] = "normal"
    pgmitems[9]["state"] = "normal"
    return

# -------------------------------
# disable text boxes
# ------------------------------
def txtdisable():
    pgmitems[1]["state"] = "disabled"
    pgmitems[2]["state"] = "disabled"
    pgmitems[3]["state"] = "disabled"
    pgmitems[4]["state"] = "disabled"
    pgmitems[5]["state"] = "disabled"
    pgmitems[9]["state"] = "disabled"    
    return

# ---------------------------------------
# find and display room
# --------------------------------------------
def findroom():
    roomnum=pgmitems[0].get()
    roomnum=roomnum.upper()
    pgmitems[0].delete(0,"end")     # clear room number
    pgmitems[6].delete(0,"end")     # clear message box
    clrit()
    txtopen()
    pgmitems[1].insert(0,roomnum)
    msg=auditroom(roomnum)         # audit room number
    if  len(msg) > 0:
        pgmitems[6].insert(0,msg)
    else:
        try:
            roomnum=roomnum.upper()
            rsel = "Select * from room where roomid = "  + "'" + roomnum + "'"
            #print('rsel ',rsel)
            pgmitems[12].execute(rsel)
            results = pgmitems[12].fetchall()
            if len(results) == 0:
                msgx= roomnum + ' ' + 'Room NOT found '
                pgmitems[6].insert(0,msgx)
            else:
                for theroom in results:
                    if theroom[1] is not None:
                        pgmitems[2].insert(0,theroom[1])  #phone
                    if theroom[2] is not None:
                        pgmitems[3].insert(0,theroom[2])  # staff count
                    else:
                        pgmitems[3].insert(0,0)  # staff count
                    # ----------------------------------------------
                    # look up key(s) for room
                    # -----------------------------------
                                       
                    if theroom[3] is not None:
                        pgmitems[5].insert(0,theroom[3])  # notes
                if theroom[2] is not None:
                    usel = "Select * from assignoffice where roomnumber = "
                    usel = usel + '"' + roomnum+ '"'
                    pgmitems[12].execute(usel)
                    oresults = pgmitems[12].fetchall()
                    for office in oresults:
                        inst = office[2]
                        isel = 'select * from instructor where instructorid ='
                        isel = isel + '"' + inst + '"'
                        pgmitems[12].execute(isel)
                        iresults = pgmitems[12].fetchall()
                        x=1
                        for instr in iresults:
                            thename = instr[1] + ' ' + instr[2]
                            pgmitems[9].insert(x,thename)
                            x=x+1
                     # disable all textboxs and listbox except room
        #except Exception as e:
                    #print(str(e))
        except:
            pgmitems[11] = " UNKNOWN ERROR with Room number"
            pgmitems[10] = "ROOM NUMBER ERROR"
    if pgmitems[11] != "":
        print('11 ',pgmitems[11])
        showmsg()
    txtdisable()
    return

# ---------------------------------------
# clear text boxes
# code == null - clear all boxes
# --------------------------------------------
def clrit():
    txtopen()
    pgmitems[1].delete(0,"end")
    pgmitems[2].delete(0,"end")
    pgmitems[3].delete(0,"end")
    pgmitems[4].delete(0,"end")
    pgmitems[5].delete(0,"end")
    pgmitems[9].delete(0,"end")
    pgmitems[10]=''
    pgmitems[11]=''
    txtdisable()
    return

# ---------------------------------------
#  create window
# --------------------------------------
def createwindow():
    mainwin = Tk()
    pgmitems[24] = mainwin
    mainwin.title("Office Management")
    mainwin.geometry('600x600+200+200')
    mainwin["bg"] = 'yellow' 
    return  mainwin



# -------------------------------------------
# call maintenance program
# ----------------------------------------------
def callmaint():
    os.system('om200.py')
    
# ---------------------------------------
#  Create the buttons
# --------------------------------------
def btns():
    cmdfind = Button(pgmitems[24], text="FIND",
                    font=("Arial Bold", 20),  
                   command=lambda : findroom())
    cmdfind.place(x=400,y=100)
    pgmitems[8] = cmdfind

    maintlbl = Label(pgmitems[24], text="Maintenance: ",
                    fg = "Black", bg = 'yellow', font=("Arial Bold", 12))
    maintlbl.place(x=100,y=500)
    
    cmdmaint = Button(pgmitems[24], text="GO", 
                   fg="red",
                   font=("Arial Bold", 15),                                      
                   command=lambda : callmaint())
    cmdmaint.place(x=210,y=500)

    
    cmdquit = Button(pgmitems[24], text="QUIT", 
                   fg="red",
                   font=("Arial Bold", 20),                                      
                   command=lambda : CloseWindow())
    cmdquit.place(x=400,y=500)
    return

# ---------------------------------------------------------------------
#  place labels and textboxes on window
# ------------------------------------------------------------------------
def buildwindow():
    
    # put labels on window
    e=len(ldic)
    for w in range(0,e,1):
        wlist = ldic[w]
        txtboxlbl = Label(pgmitems[24], text=wlist[0],
                    fg = wlist[1], bg = wlist[2], font=(wlist[3], wlist[4]))
        txtboxlbl.place(x=wlist[5],y=wlist[6])
    # put text boxes on window
    e=len(tdic)
    for w in range(0,e,1):
        wlist=tdic[w]
        pgmitems[w] = Entry(pgmitems[24],width=wlist[0],
                                font=(wlist[1], wlist[2]))
        pgmitems[w].place(x=wlist[3],y=wlist[4])
    pgmitems[0].focus_set()      
        # end of loop
    # create instructor list box
    lstboxlbl = Label(pgmitems[24], text="Instructors ",
                    fg = "Black", bg = 'yellow', font=("Arial Bold", 12))
    lstboxlbl.place(x=300,y=180)
    pgmitems[9]= Listbox(pgmitems[24],
                 font=("Arial Bold", 16),                      
                 height = 6, width = 20, 
                  bg = "white", fg = "black")
    pgmitems[9].place(x=300,y=200)
    
    return

# ----------------------------------------------------
#   red x clicked
# ------------------------------------------------------
def redx():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        CloseWindow()

# -----------------------------------------
#  Close the window and database
# -----------------------------------------
def CloseWindow():
    if pgmitems[13] != '':                    #   database open ??
        pgmitems[13].commit()           #   yes commit and close databse
        pgmitems[13].close()
    pgmitems[24].destroy()               # destroy window
# ---------------------------------------
#  main line code
# --------------------------------------
def om100():
    mainwin = createwindow()
    mainwin.protocol("WM_DELETE_WINDOW", redx)  
    buildwindow()
    btns()
    txtdisable()
    obtaindatabase()
    if pgmitems[12]== '':
        pgmitems[8].place_forget()
        #pgmitems[8]["state"] = "disabled"
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
    om100()
# -------------------------------------------------------------
# ---------------------------------------
#  end of program
# --------------------------------------

