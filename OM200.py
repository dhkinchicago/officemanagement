# ----------------------------------------------
#  OM200  Instructor Maintenance (A,C,D)
#
#     version control
#     -------------------------
#  version .2 11/07/23
#  version .3 12/27/23
#
# add in note to update
#
#  to do  add in key processing
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
#     0 = textbox 0   Id number to find
#     1 = textbox 1   id number
#     2 = textbox 2   first name
#     3 = textbox 3   middle name
#     4 = textbox 4   last name
#     5 = textbox 5   status (F,A,O)
#     6 = textbox 6   notes
#     7 = textbox 7  add/change/delete message
#     8 -- radio button for key (y/n)
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
                2:"first name not filled in",
                3:"last name not filled in",
                4:"status not filled in",
                5:"valid status: (F,A,O) only",
                10:"database error - insert failed",
                11:"database error - update failed",
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
ldic={0:["ID # Search","black","yellow",'"Arial Bold"',16,100,100],
          1:["ID Number","black","yellow",'"Arial Bold"',16,25,150],
          2:["First Name","black","yellow",'"Arial Bold"',16,10,200],
          3:["Middle Name","black","yellow",'"Arial Bold"',16,10,250],
          4:["Last Name","black","yellow",'"Arial Bold"',16,10,300],
          5:["Status","black","yellow",'"Arial Bold"',16,40,350],
          6:["Notes","black","yellow",'"Arial Bold"',16,50,400],
          7:["NONE",'z']     # no label for textbox
           }
#         
# ----------------------------------------------------------------------
# text box disctionary    use with wlist
#  key:width, font style, font size, x postion, y position
tdic = {0:[12,'"Arial bold"',16,250,100],      # ID # search
            1:[10,'"Arial bold"',16,150,150],      # ID number
            2:[10,'"Arial bold"',16,150,200],      # First name
            3:[10,'"Arial bold"',16,150,250],      # Middle name
            4:[10,'"Arial bold"',16,150,300],      # Last name
            5:[5,'"Arial bold"',16,150,350],        # status
            6:[12,'"Arial bold"',16,150,400],      #  Notes
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
    pgmitems[5].delete(0,"end")
    pgmitems[6].delete(0,"end")
    pgmitems[7].delete(0,"end")
    pgmitems[10]=''
    pgmitems[11]=''
    btnshide()
    pgmitems[2].configure(bg="white")
    pgmitems[4].configure(bg="white")
    pgmitems[5].configure(bg="white")
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
    pgmitems[24] = mainwin
    return  mainwin

# ---------------------------------------
#  screen title
# --------------------------------------
def labeltxtx():
    txt01 =Label(pgmitems[24], text="OM200",
                         fg="black",bg='yellow',font=("Arial Bold", 8))
    txt01.place(x=0, y=0) 
    txt02 = Label(pgmitems[24], text="Instructor Maintenance",
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
    if pgmitems[20] == 98:               # if update (no update found, leave clear button)
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
    pgmitems[2].configure(bg="lightgreen")       # first name
    pgmitems[4].configure(bg="lightgreen")       # last name
    pgmitems[5].configure(bg="lightgreen")       # status
    pgmitems[7].insert(0,"Required information in green")
    pgmitems[1]["state"] = "disabled"
    return
# -----------------------------------------------------------------
# highlight blanks fields
# -----------------------------------------------------------------
def setred(fn, ln, st):
    if len(fn)==0 or fn.isspace():
        pgmitems[2].configure(bg="red")       # first name
    if len(ln)==0 or ln.isspace():
        pgmitems[4].configure(bg="red")        # last name
    if len(st)==0 or st.isspace():
        pgmitems[5].configure(bg="red")       # status
    return
# -----------------------------------------
#   validate id number
# ---------------------------------------------
def auditinstr(idnum):
    msg = ''
    if idnum=='' or idnum.isspace():
        msg= 'enter a instructor id number'
    else:
        if len(idnum) != 9:
            msg = 'Invalid id number number'
        else:
            if idnum.isnumeric():
                msg = ''
            else:
                msg = 'id number not numeric'
    return msg

# ----------------------------------------
#  find instructor
# ---------------------------------------
def instrfind():
    btnshide()
    clrit()
    idnum=pgmitems[0].get()
    pgmitems[0].delete(0,"end") 
    pgmitems[1].insert(0,idnum)
    pgmitems[1]["state"] = "disable"
    msg=auditinstr(idnum)
    if  msg !='':
        pgmitems[11] = msg
        pgmitems[10] = "ID NUMBER INVALID"
    else:
        try:
            sidnum = '"' + str(idnum) + '"'
            #print(sidnum)
            rsel = "Select * from instructor where instructorid = "
            rsel=rsel + sidnum
            #print('rsel ',rsel)
            pgmitems[12].execute(rsel)
            results = pgmitems[12].fetchall()
            if len(results) == 0:
                btnadd()
            else:
                for theinstr in results:
                        pgmitems[9] = theinstr
                        #print('theroom ',theroom)
                        if theinstr[1] is not None:
                            pgmitems[2].insert(0,theinstr[1])  #first name
                        if theinstr[3] is not None:
                            pgmitems[3].insert(0,theinstr[3])  # last name
                        if theinstr[2] is not None:
                            pgmitems[4].insert(0,theinstr[2])  # middle name
                        if theinstr[4] is not None:
                            pgmitems[5].insert(0,theinstr[4])  # status
                        else:
                            pgmitems[4].insert(0,'U')
                        if theinstr[6] is not None:
                            pgmitems[6].insert(0,theinstr[6])  # notes
                        btnsud()
        except:
            pgmitems[11] = " UNKNOWN ERROR with instructor number"
            pgmitems[10] = "INSTRUCTOR NUMBER ERROR"
    if pgmitems[11] != "":
        showmsg()
    return

# ---------------------------------------
#   Add instructor
#
#    add key processing
#          has key(s)  (y/n)
#        using assign thru room get key number from room
# --------------------------------------
def instradd():
    pgmitems[9] = ''      # clear rec
    pgmitems[20]=0     # reset error code
    pgmitems[7].delete(0,"end")
    idn=pgmitems[1].get()         # id number
    fn=pgmitems[2].get()           #  first name
    mn = pgmitems[3].get()       # middle name
    ln=pgmitems[4].get()           #  last name
    st=pgmitems[5].get()           # status
    if fn == '' and ln == '' and st == '':
        pgmitems[20] = 1
    else:
        if fn == '':                  # first name
             pgmitems[20]=2
        if ln =='':              # last name
             pgmitems[20]=3
        if st =='':              # status
             pgmitems[20] =4
    if pgmitems[20] ==0:
        st=st.upper()
        pgmitems[5].delete(0,"end")
        pgmitems[5].insert(0,st) 
        if st=='F' or st=='A' or st =='O':
            try:
                insrec="INSERT INTO instructor (instructorid,firstname,lastname,status"
                if mn !='':
                    insrec=insrec + ',middlename'
                insrec=insrec + ')'
                sidn = '"' + str(idn) + '"'
                insrec=insrec + 'VALUES (' + sidn + ',"' + fn + '","' + ln + '","' + st
                if mn != '':
                    insrec = insrec +'","' + mn
                insrec = insrec +'")'
                print (insrec)
                cur=pgmitems[12]
                cur.execute(insrec)
                pgmitems[7].insert(0,idn+' added to database')
                pgmitems[13].commit() 
            except:
                pgmitems[20] =10
        else:
            pgmitems[20]=5
    if pgmitems[20]>0:
        pgmitems[7].delete(0,"end")
        pgmitems[7].insert(0,e1dt[pgmitems[20]])
    pgmitems[15].place_forget()  
    return

# ---------------------------------------
#   update instructor
#   pgmitems[9] has current (old) data
#    after update clear pgmitems[9]   & buttons
#
#    add key processing
#          has key(s)  (y/n)
#        using assign thru room get key number from room
# --------------------------------------
def instrupd():
    # steps
    # 1. determine if there is any changes
    #      yes proceed   no, issue msg and clear window
    # 2. build update line
    # 3. update database
    # 4. issue msg and clear window
    #  to be added later: (has) key change from y/n
    
# prepare current data base record
    updrec=''
    olddata = pgmitems[9]
    if olddata[1] != None:
        oldfn = olddata[1]        # first name
    else:
        oldfn=''
    if olddata[2] != None:
        oldln = olddata[2]          # last name
    else:
        oldln=''
    if olddata[3] != None:
        oldmn = olddata[3]        # middle name
    else:
        oldmn=''
    if olddata[4] != None:
        oldst = olddata[4]         # status
    else:
        oldst=''
 
    newfn=pgmitems[2].get().strip()           #  first name
    newmn = pgmitems[3].get().strip()       # middle name
    newln=pgmitems[4].get().strip()           #  last name
    newst=pgmitems[5].get().strip()             # status
    #  any changes?    
    if oldfn==newfn and oldln ==newln and oldmn==newmn and oldst ==newst:
       pgmitems[7].insert(0,olddata[0]+' NO Changes detected')
       pgmitems[20] =98
       btnshide()
    else:
        #  check required fields are not blank (first, last & status)
        if newfn=='' or newln=='' or newst=='' or newfn.isspace() or newln.isspace() or newst.isspace():
            pgmitems[7].insert(0,olddata[0]+' required fields cannot be blank')
            pgmitems[20] =98
            btnshide()
            #  add:  highlight fields in red if required fields are blank
            setred(newfn,newln,newst)
        else:
            try:
                uall=''
                u1=''
                u2=''
                u3=''
                u4=''
                updrec = 'UPDATE instructor '
                updrec = updrec + ' Set '
                if oldfn !=newfn:
                    u1 =  'firstname = '+ "'" + newfn +"'"
                if oldmn != newmn:    # allow middle name to be changed to blank
                    u2 = 'middlename = '+ "'" + newmn + "'"
                if oldln != newln:
                    u3 = ' lastname = ' + "'" + newln + "'"
                if oldst != newst:
                    u4 = 'status = ' + "'" + newst + "'"
                if len(u1) != 0:
                    uall =u1
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
                if len(u4) != 0:
                    if len(uall) ==0:
                        uall = u4
                    else:
                        uall =uall + ',' + u4
                updrec = updrec + uall
                updrec = updrec + ' WHERE instructorid = ' + "'"  + str(pgmitems[1].get()) + "'"
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
        pgmitems[7].delete(0,"end")
        pgmitems[7].insert(0,e1dt[pgmitems[20]])
    return

# ---------------------------------------
#   delete instructor
#   delete critieria 
#           cannot delete if still assigned to room
#           or has keys (to be added)
# --------------------------------------
def instrdel():
    idnum=pgmitems[1].get()
    try:
        sidnum = '"' + str(idnum) + '"'
        # check if instructor is assigned an office
        # check if instructor has keys
        usel = "Select * from assignoffice where instructorid = " +sidnum
        #print(usel)
        pgmitems[12].execute(usel) 
        oresults = pgmitems[12].fetchall()
        if len(oresults)==0:
            pgmitems[11] = "ZZZ Delete from Database validate"
            pgmitems[10] = " Are you sure you want to DELETE ??"
            showmsg()
            if pgmitems[21] == True:
                delrec= "DELETE FROM instructor WHERE instructorid = "+ sidnum
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
       pgmitems[7].delete(0,"end")
       pgmitems[7].insert(0,e1dt[pgmitems[20]])           
    return

# ---------------------------------------
#  Create the buttons
# --------------------------------------
def btns():
    #  find button
    cmdfind = Button(pgmitems[24], text="FIND",
                font=("Arial Bold", 20),  
                   command=lambda : instrfind())
    cmdfind.place(x=425,y=75)
    pgmitems[14] = cmdfind
    #   Add button
    cmdadd = Button(pgmitems[24], text="Add",
                    font=("Arial Bold", 16),  
                   command=lambda : instradd())
    cmdadd.place(x=400,y=175)
    pgmitems[15] = cmdadd
    #  update button
    cmdupd = Button(pgmitems[24], text="Update",
                    font=("Arial Bold", 16),  
                   command=lambda : instrupd())
    cmdupd.place(x=400,y=250)
    pgmitems[16] = cmdupd
    #  delete button
    cmddel = Button(pgmitems[24], text="Delete",
                    font=("Arial Bold", 16),  
                   command=lambda : instrdel())
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
                   command=lambda : CloseWindow())
    cmdquit.place(x=525,y=500)
    pgmitems[19] = cmdquit
    btnshide()
    return

# ---------------------------------------------------------------------
#  place labels and textboxes on window
# ------------------------------------------------------------------------
def buildwindow():
    e=len(ldic)
    for w in range(0,e,1):
        wlist = ldic[w]
        if wlist[0] != "NONE":
            txtboxlbl = Label(pgmitems[24], text=wlist[0],
                    fg = wlist[1], bg = wlist[2], font=(wlist[3], wlist[4]))
            txtboxlbl.place(x=wlist[5],y=wlist[6])
        wlist=tdic[w]
        pgmitems[w] = Entry(pgmitems[24],width=wlist[0],
                                font=(wlist[1], wlist[2]))
        pgmitems[w].place(x=wlist[3],y=wlist[4])
        pgmitems[0].focus_set()
        # end of loop
    return
 # -----------------------------------------
#  Close the window and database
# -----------------------------------------
def CloseWindow():
    if pgmitems[13] != '':
        pgmitems[13].commit()
        pgmitems[13].close()
    pgmitems[24].destroy()
# ----------------------------------------------------
#   red x clicked
# ------------------------------------------------------
def redx():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        CloseWindow()
# ---------------------------------------
#  main line code
# --------------------------------------
def om200():
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
    om200()
# -------------------------------------------------------------
# ---------------------------------------
#  end of program
# --------------------------------------

