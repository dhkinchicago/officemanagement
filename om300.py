# change to room assignment
#    instructor to room
#
#    ****** need to work on this
#     do not test
# ----------------------------------------------
#  OM300  room assignment  (A,D)
#     assign instructor to room
#    unassign instructor from room
#    NO changes can be made
#     changes done from maintenance screens
#
#     version control
#     -------------------------
#  version .1 12/27/23
#   ---- redo label and textbox creation
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
#     0 -- not used
#     1 -- not used     
#     2 -- not used
#     3 = listbox 1     room listbox
#     4 = listbox 2     employee listbox
#     5 = listbox 3     connected list room/employee
#     6 = textbox 1   notes
#     7 = not used
#     8 -- not used
#     9 -- radiobutton select code
#   10 = textbox  error message  (call showmsg) 
#   11 = textbox title                    (call showmsg)
#   12 = DB cursor
#   13 = conn   
#   14 -- not used
#   15 = connect button
#   16 = disconnect button
#   17 = quit button
#   18 = print button
#   19 - not used
#   20 =  error code
#   21 =  mesage box code
#   22 - 23  -- not used
#   24 = mainwin
# --------------------------------------------------------
#   error codes and messages
# -----------------------------------------------
e1dt= {1:"unknown error",
                10:"database error - insert failed",
                12:"database error - delete failed",
                99:"unknown error"}
# ---------------------------------------------------------------------
wlist=[]        # work list  for window elements
# ---------------------------------------------------------------------

# ----------------------------------------------------------------------
#  Dictionaries for labels and text box
# ---------------------------------------------------------------------
#  Label dictionary   use with wlist
#   title = NONE or KEY  -- special processing
#   key:title,fg color,bg color, font style, font size,x position, y postion
#    list box titles and notes textbox title
labdic={0:["Room ","black","yellow",'"Arial Bold"',16,100,150],
             1:["Instructor","black","yellow",'"Arial Bold"',16,300,150],
             2:["Notes","black","yellow",'"Arial Bold"',16,25,400],
            }
#         
# ----------------------------------------------------------------------
# text box dictionary    use with wlist
#   key: pgmitems, width, font style, font size, x postion, y position,
txdic = {0:[6,40,'"Arial bold"',16,75,400],      # notes
             1:[10, 40,'"Arial bold"',16,50,650],      # error message
            }
#

# ----------------------------------------------------------------------
# radio button dictionary    use with wlist
#  key:, pgmitems, width, font style, font size, x postion, y position, pgmitems
rddic = {0:[0,12,'"Arial bold"',16,250,100],      # full time
             1:[1,10,'"Arial bold"',16,150,150],      # Adjunct
             2:[2,10,'"Arial bold"',16,150,200],      # staff
            }

# ----------------------------------------------------------------------
#  listboxs dictionary    use with wlist
#  key: pgmitems, width, font style, font size, x postion, y position
lbxdic = {0:[3,12,'"Arial bold"',16,250,100,3],      # room
               1:[4,10,'"Arial bold"',16,150,150,4],      # instructor
               2:[5, 10,'"Arial bold"',16,150,200,5],      # connected (room, Instructor)
              }

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
# clear text boxes and listboxes
# code == null - clear all boxes
# --------------------------------------------
def clrit():
    pass
    return

# ---------------------------------------
#  create window
# --------------------------------------
def createwindow():
    mainwin = Tk()
    mainwin.title("Office Management")
    mainwin.geometry('800x800+400+100')
    mainwin["bg"] = 'yellow'
    pgmitems[24] = mainwin
    var = StringVar()   # used for radio button selection
    pgmitems[9] = var
    return  mainwin

# ---------------------------------------
#  screen title
# --------------------------------------
def labeltxtx():
    txt01 =Label(pgmitems[24], text="OM300",
                         fg="black",bg='yellow',font=("Arial Bold", 8))
    txt01.place(x=0, y=0) 
    txt02 = Label(pgmitems[24], text="Room - Instructor Assignment",
                  fg = "black", bg = 'yellow',  font=("Arial Bold", 20))
    txt02.place(x=100,y=0)
    return



# ---------------------------------------
#   Add assignment - connect room & instructor
#   selected room and Instructor (highlighted)
#   connect button selected
#   some editing is done (adjunct room number check)
#   room-instructor addd to database and bottom listbox
#   instructor removed from list
#  room number removed from list when full
#  refresh window listboxes
#
# --------------------------------------
def connectri():
    pass

# ---------------------------------------
#  disconnect assignment  room -instructor
#   delete critieria 
#           selcted room instructor from bottom listbox
#           remove from bottom list
#           add back to room and instructor listbox
#           adjust room count
#           delete from room-instructor database table
#           refresh window
#   ------------------  add later, cross check with key processing
#           or has keys (to be added)
# --------------------------------------
def disconnectri():
    pass
# ---------------------------------------
#  Create the buttons
#    buttons on the window
# --------------------------------------
def btns():

    #  connect button
    cmddel = Button(pgmitems[24], text="Connect",
                    font=("Arial Bold", 16),  
                   command=lambda : connectri())
    cmddel.place(x=600,y=200)
    pgmitems[15] = cmddel

 
    #  disconnect button
    cmddel = Button(pgmitems[24], text="Disconnect",
                    font=("Arial Bold", 16),  
                   command=lambda : disconnectri())
    cmddel.place(x=600,y=500)
    pgmitems[16] = cmddel

    #  quit button
    cmdquit = Button(pgmitems[24], text="QUIT", 
                   fg="red",
                   font=("Arial Bold", 20),                                      
                   command=lambda : CloseWindow())
    cmdquit.place(x=600,y=700)
    pgmitems[17] = cmdquit

    #  print button
    cmdquit = Button(pgmitems[24], text="print", 
                   fg="red",
                   font=("Arial Bold", 16),                                      
                   command=lambda : printlist())
    cmdquit.place(x=250,y=700)
    pgmitems[18] = cmdquit

    
    
    return
# ---------------------------------------------------------------------------
#  radio button processing
#  change color of selection
#  populate room, instructor and connection listbox
#  upon change in radio button,
#     clear listboxes and repopulate
# -----------------------------------------------------------------------------
def rbselection():
    print('Selected: ',pgmitems[9].get())
    pass
# ---------------------------------------------------------------------
#  place labels and textboxes on window
#  build window: labels, textboxes, listboxes
# ------------------------------------------------------------------------
def buildwindow():
# put labels (3) on window
    e=len(labdic)
    for w in range(0,e,1):
        wlist = labdic[w]
        txtboxlbl = Label(pgmitems[24], text=wlist[0],
                    fg = wlist[1], bg = wlist[2], font=(wlist[3], wlist[4]))
        txtboxlbl.place(x=wlist[5],y=wlist[6])
        
# put text boxes (2) on window
    e=len(txdic)
    for w in range(0,e,1):
        wlist=txdic[w]              # object for screen
        z=wlist[0]                      # pgmitems position
        pgmitems[z] = Entry(pgmitems[24],width=wlist[1],
                                font=(wlist[2], wlist[3]))
        pgmitems[z].place(x=wlist[4],y=wlist[5])
        
# put radio buttons (3) on window  (using loop)
    # var = StringVar()   # used for radio button selection
    r1 = Radiobutton(pgmitems[24], text='Full Time',
                     variable=pgmitems[9], value='A', command=rbselection)
    r1.place(x=150,y=70)
    r2 = Radiobutton(pgmitems[24], text='Adjunct',
                     variable=pgmitems[9], value='B', command=rbselection)
    r2.place(x=250,y=70)
    r3 = Radiobutton(pgmitems[24], text='Staff',
                     variable=pgmitems[9], value='C', command=rbselection)
    r3.place(x=350,y=70)
    
#    e=len(rddic)                 #  radio button loop  <----------
#   for w in range(0,e,1):
#        wlist=rddic[w]              # object for screen
#       z=wlist[0]                      # pgmitems position
#        pgmitems[z] = Entry(pgmitems[24],width=wlist[1],
#                                font=(wlist[2], wlist[3]))
#        pgmitems[z].place(x=wlist[4],y=wlist[5])
     
    # put listboxs (3) on window   Using loop)

#    create 3 listboxes
    lbroom = Listbox(pgmitems[24], width=20, height=10)
    lbroom.place(x=100,y=200)
    
    lbinstr = Listbox(pgmitems[24], width=40, height=10)
    lbinstr.place(x=300,y=200)
    
    lbconnect = Listbox(pgmitems[24], width=80, height=10)
    lbconnect.place(x=100,y=450)
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
def om300():
    (mainwin) = createwindow()
    
    mainwin.protocol("WM_DELETE_WINDOW", redx) 
    labeltxtx()
    buildwindow()
    btns()
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
    om300()
# -------------------------------------------------------------
# ---------------------------------------
#  end of program
# --------------------------------------

