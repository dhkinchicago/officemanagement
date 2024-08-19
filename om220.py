#  need to be tested
#  add key handling - look up and shows keys for the room
# 

# 
# ----------------------------------------------
#  OM220  ROOM Maintenance   (A,C,D)
#
#     version control
#     -------------------------
#  version .1 12/27/23
#
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
#     0 = textbox 0   room number to find
#     1 = textbox 1   roomnumber
#     2 = textbox 2   phone number
#     3 = textbox 3   key number
#     4 = textbox 4   staff count
#     5 = textbox 5   notes
#     6 = textbox 6   add/change/delete message
#     7 = not used
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
#   22 - 23  -- not used
#   24 = mainwin
# --------------------------------------------------------
#   error codes and messages
# -----------------------------------------------
e1dt= {1:"Required fields not filled in",
                2:"room number not filled in",
                3:"phone number not filled in",
                4:"key number filled in",
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
ldic={0:["Room # Search","black","yellow",'"Arial Bold"',16,100,100],
          1:["Room Number","black","yellow",'"Arial Bold"',16,10,150],
          2:["Phone Number","black","yellow",'"Arial Bold"',16,10,200],
          3:["Key Number","black","yellow",'"Arial Bold"',16,10,250],
          4:["Staff count","black","yellow",'"Arial Bold"',16,10,300],
          5:["Notes","black","yellow",'"Arial Bold"',16,40,350]
           }
#         
# ----------------------------------------------------------------------
# text box disctionary    use with wlist
#  key:width, font style, font size, x postion, y position
tdic = {0:[12,'"Arial bold"',16,250,100],      # Room # search
            1:[10,'"Arial bold"',16,150,150],      # room number
            2:[10,'"Arial bold"',16,150,200],      # Phone number
            3:[20,'"Arial bold"',16,150,250],      # Key Number
            4:[5,'"Arial bold"',16,150,300],        # staff count
            5:[12,'"Arial bold"',16,150,350],      #  Notes
            6:[40,'"Arial bold"',16,25,500]         #  action messages 
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
    pgmitems[5].delete(0,"end")
    pgmitems[6].delete(0,"end")
    pgmitems[10]=''
    pgmitems[11]=''
    btnshide()
    pgmitems[2].configure(bg="white")
    pgmitems[4].configure(bg="white")
    pgmitems[5].configure(bg="white")
    pgmitems[6].insert(0,"")
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
    pgmitems[24] = mainwin
    return  mainwin

# ---------------------------------------
#  screen title
# --------------------------------------
def labeltxtx():
    txt01 =Label(pgmitems[24], text="OM220",
                         fg="black",bg='yellow',font=("Arial Bold", 10))
    txt01.place(x=0, y=0) 
    txt02 = Label(pgmitems[24], text="Room Maintenance",
                  fg = "black", bg = 'yellow',  font=("Arial Bold", 20))
    txt02.place(x=100,y=0)
    return


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
    pgmitems[2].configure(bg="lightgreen")       # Phone
    pgmitems[3].configure(bg="lightgreen")       # key number
    pgmitems[4].configure(bg="lightgreen")       # staff count
    pgmitems[5].configure(bg="lightgreen")       # notes
    pgmitems[6].insert(0,"Required information in green")
    pgmitems[1]["state"] = "disabled"
    return

# -----------------------------------------
#   validate room number
# ---------------------------------------------
def auditroom(rmnum):
    msg = ''
    if rmnum=='' or rmnum.isspace():
        msg= 'enter a room number'
    return msg

# ----------------------------------------
#  find room
# ---------------------------------------
def roomfind():
    btnshide()
    clrit()
    rmnum=pgmitems[0].get()
    pgmitems[0].delete(0,"end")
    rmnum = rmnum.upper()
    pgmitems[1].insert(0,rmnum)
    pgmitems[1]["state"] = "disable"
    msg=auditroom(rmnum)
    if  msg !='':
        pgmitems[11] = msg
        pgmitems[10] = "Room NUMBER INVALID"
    else:
        try:
            srmnum = '"' + rmnum + '"'
            #print(sidnum)
            rsel = "Select * from room where roomid = "
            rsel=rsel + srmnum
            #print('rsel ',rsel)
            pgmitems[12].execute(rsel)
            results = pgmitems[12].fetchall()
            if len(results) == 0:
                btnadd()
            else:
                for theroom in results:
                        pgmitems[9] = theroom
                        if theroom[1] is not None:
                            pgmitems[2].insert(0,theroom[1])  #phone
                        if theroom[2] is not None:
                            pgmitems[4].insert(0,theroom[2])  # staff count
                        #if theinstr[4] is not None:
                            #pgmitems[5].insert(0,theroom[3])  # notes
         # -------------------------------------------------------
                        #  get keys for room from key table
                        #   can be more than 1
        # --------------------------------------------------------
                        btnsud()
                        pgmitems[3]["state"] = "disable"
                        pgmitems[4]["state"] = "disable"

        except:
            pgmitems[11] = " UNKNOWN ERROR with room number"
            pgmitems[10] = "ROOM NUMBER ERROR"
    if pgmitems[11] != "":
        showmsg()
    return

# ---------------------------------------
#   Add room number
#
# --------------------------------------
def roomadd():
    pgmitems[9] = ''      # clear rec
    pgmitems[20]=0     # reset error code
    pgmitems[6].delete(0,"end")
    roomid=pgmitems[1].get()         # room number
    fone=pgmitems[2].get()           #  phone number
    keynos=pgmitems[3].get()           #  key number(s)
    notes=pgmitems[5].get()           # notes
    if roomid == '' and fone == '':
        pgmitems[20] = 1
    else:
        if roomid == '':                  # room number
             pgmitems[20]=2
        if fone =='':              # phone number
             pgmitems[20]=3
    if pgmitems[20] ==0:
    #  add to database set staff count to 0
        try:
            staffcount='0'
            insrec="INSERT INTO room (roomid,phone,staffcount)"
            insrec=insrec + ' VALUES ('  +   '"' + roomid + '"' + ',' +  fone +  ',' +  staffcount
            insrec = insrec +')'
            print(insrec)
            cur=pgmitems[12]
            cur.execute(insrec)
            pgmitems[6].insert(0,roomid +' added to database')
            pgmitems[13].commit()
        #except Exception as e:
            #print(e)
            #pgmitems[20] = 10
        except:
            pgmitems[20] = 10

    if pgmitems[20]>0:
        pgmitems[5].delete(0,"end")
        pgmitems[6].insert(0,e1dt[pgmitems[20]])
    pgmitems[15].place_forget()  
    return

# ---------------------------------------
#   update room
#   pgmitems[9] has current (old) data
#    after update clear pgmitems[9]   & buttons
# --------------------------------------
def roomupd():
    # only update phone number,
    # key number change done with key maintenance
    updrec=''
    olddata = pgmitems[9]
    if olddata[1] != None:
        oldfone = olddata[1]        # fone
    else:
        oldfone=''

    newfone=pgmitems[2].get().strip()           #  fone
    #  any changes?    
    if oldfone==newfone:
       pgmitems[6].insert(0,olddata[0]+' NO Changes detected')
       pgmitems[20] =98
       btnshide()
    else:
        #  check required fields are not blank 
        if newfone==''  or newfone.isspace():
            pgmitems[6].insert(0,olddata[0]+' required fields cannot be blank')
            pgmitems[20] =98
            btnshide()
        else:
            try:
                uall=''
                updrec = 'UPDATE room '
                updrec = updrec + ' Set '
                uall =  'phone = '+ "'" + newfone +"'"
                updrec = updrec + uall
                updrec = updrec + ' WHERE roomid = ' + "'"  + str(pgmitems[1].get()) + "'"
                #print(updrec)
                cur=pgmitems[12]
                cur.execute(updrec)
                pgmitems[13].commit()
                idnum = pgmitems[1].get()
                clrit()
                pgmitems[6].insert(0,idnum +' Record UPDATED')
          #except Exception as e:
              #print(e)
              #pgmitems[20] = 10
            except:
               pgmitems[20] = 11

    if pgmitems[20]>0:
        pgmitems[5].delete(0,"end")
        pgmitems[6].insert(0,e1dt[pgmitems[20]])
    pgmitems[15].place_forget()  
    return

# ---------------------------------------
#   delete room
#   delete critieria 
#           cannot delete if still assigned to room
#           or has keys (to be added)
# --------------------------------------
def roomdel():
    roomid=pgmitems[1].get()
    try:
        # check if instructor is assigned an office
        usel = "Select * from assignoffice where roomnumber = " + '"' + roomid + '"'
        print(usel)
        pgmitems[12].execute(usel) 
        oresults = pgmitems[12].fetchall()
        if len(oresults)==0:
            pgmitems[11] = "ZZZ Delete from Database validate"
            pgmitems[10] = " Are you sure you want to DELETE ??"
            showmsg()
            if pgmitems[21] == True:
                delrec= "DELETE FROM room WHERE roomid = "+ '"' + roomid + '"'
                print(delrec)
                cur=pgmitems[12]
                cur.execute(delrec)
                clrit()
                pgmitems[6].insert(0,roomid+' *** DELETED *** from database')
                pgmitems[13].commit()  
            else:
                pgmitems[6].insert(0,'Deletion Canceled')
        else:
            pgmitems[6].insert(0,'Insturctor assign to an office, cannot delete')
    #except Exception as e:
            #print(e)
            #pgmitems[20] = 12
    except:
            pgmitems[20] =12
    if pgmitems[20]>0:
        pgmitems[5].delete(0,"end")
        pgmitems[6].insert(0,e1dt[pgmitems[20]])
    pgmitems[15].place_forget()  
    return

# ---------------------------------------
#  Create the buttons
# --------------------------------------
def btns():
    #  find button
    cmdfind = Button(pgmitems[24], text="FIND",
                    font=("Arial Bold", 20),  
                   command=lambda : roomfind())
    cmdfind.place(x=425,y=75)
    pgmitems[14] = cmdfind
    #   Add button
    cmdadd = Button(pgmitems[24], text="Add",
                    font=("Arial Bold", 16),  
                   command=lambda : roomadd())
    cmdadd.place(x=400,y=175)
    pgmitems[15] = cmdadd
    #  update button
    cmdupd = Button(pgmitems[24], text="Update",
                    font=("Arial Bold", 16),  
                   command=lambda : roomupd())
    cmdupd.place(x=400,y=250)
    pgmitems[16] = cmdupd
    #  delete button
    cmddel = Button(pgmitems[24], text="Delete",
                    font=("Arial Bold", 16),  
                   command=lambda : roomdel())
    cmddel.place(x=400,y=300)
    pgmitems[17] = cmddel
    #   clear button
    cmdclr = Button(pgmitems[24], text="Clear",
                    font=("Arial Bold", 16),  
                   command=lambda : clrit())
    cmdclr.place(x=400,y=400)
    pgmitems[18] = cmdclr
    #  quit button
    cmdquit = Button(pgmitems[24], text="QUIT", 
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
def buildwindow():
    # build labels
    e=len(ldic)
    for w in range(0,e,1):
        wlist = ldic[w]
        txtboxlbl = Label(pgmitems[24], text=wlist[0],
        fg = wlist[1], bg = wlist[2], font=(wlist[3], wlist[4]))
        txtboxlbl.place(x=wlist[5],y=wlist[6])
    # build textboxes
    e=len(tdic)
    for w in range(0,e,1):
        wlist=tdic[w]
        pgmitems[w] = Entry(pgmitems[24],width=wlist[0],
                                font=(wlist[1], wlist[2]))
        pgmitems[w].place(x=wlist[3],y=wlist[4])
    pgmitems[0].focus_set()      
        # end of loop
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
def om220():
    mainwin = createwindow()
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
    om220()
# -------------------------------------------------------------
# ---------------------------------------
#  end of program
# --------------------------------------

