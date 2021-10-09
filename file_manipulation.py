sqlite3_help = str('''#  **********************************************Hr sqlite3 data base module********************************************
from time import strftime #  import time unit classes from time library
currentyear = strftime("%Y")
current_year = int(currentyear)  #  convert year string data type into an integer

from tkinter import *  # import all classes from tkinter GUI library
def HRDBwindow():    #  HR module main GUI window name== win
    win = Tk()
    win.title('AA human resource database') #  HR window title
    win.geometry('535x720+0+0')
    win.maxsize(535, 500)
    win.configure(bg="cyan", bd=10)

    def hr_module():
        import sqlite3 #  import sqlite the database application that we will be using
        conn = sqlite3.connect('hr.db')  #  Create cursor object that wiil be used to 
                                         #  manipulate the data in the database
                                         #  named hr db
        conn.execute(''CREATE TABLE IF NOT EXISTS tblCOMPANY
                            (ID INT PRIMARY KEY NOT NULL,
                            NAME TEXT NOT NULL,
                            AGE INT NOT NULL,
                            ADDRESS CHAR(50) NOT NULL,
                            SALARY REAL NOT NULL,
                            QUALIFICATION TEXT NOT NULL,
                            DEPARTMENT TEXT NOT NULL,
                            YEAR_RECRUITMENT INT NOT NULL,
                            CELL_NUMBER INT NOT NULL,
                            BRANCH TEXT NOT NULL);'') #  Data defination language statement
        #  to create table named 'tblCompany' for storing employee data
        
    hr_module()  #  Call hr_module function

    
    def hrnew():  # gui to create an iterface form for adding a new employee
        import tkinter
        tk = Tk()  #  set name of the gui to 'tk'
        tk.minsize(500, 330)
        tk.maxsize(505, 330)
        tk.title('New employee')  #  set title of tk to 'New employee'
        tk.configure(bg='white', bd=5)
        label = Label(tk, text='ID', width=20, bg='gray', fg='yellow', relief='flat', font=('times new roman', 12)).grid(row=1, column=1)
        label = Label(tk, text='Name', width=20, bg='gray', fg='yellow', relief='flat', font=('times new roman', 12)).grid(row=2, column=1)
        label = Label(tk, text='Age', width=20, bg='gray', fg='yellow', relief='flat', font=('times new roman', 12)).grid(row=3, column=1)
        label = Label(tk, text='Address', width=20, bg='gray', fg='yellow', relief='flat', font=('times new roman', 12)).grid(row=4, column=1)
        label = Label(tk, text='Salary', width=20, bg='gray', fg='yellow', relief='flat', font=('times new roman', 12)).grid(row=5, column=1)
        label = Label(tk, text='Qualification', width=20, bg='gray', fg='yellow', relief='flat', font=('times new roman', 12)).grid(row=6, column=1)
        label = Label(tk, text='Department', width=20, bg='gray', fg='yellow', relief='flat', font=('times new roman', 12)).grid(row=7, column=1)
        label = Label(tk, text='Year recruited', width=20, bg='gray', fg='yellow', relief='flat', font=('times new roman', 12)).grid(row=8, column=1)
        label = Label(tk, text='Cell Number', width=20, bg='gray', fg='yellow', relief='flat', font=('times new roman', 12)).grid(row=9, column=1)
        label = Label(tk, text='Branch', width=20, bg='gray', fg='yellow', relief='flat', font=('times new roman', 12)).grid(row=10, column=1)        
            
        I_D = Entry(tk, width=20, bg='lime', fg='brown', relief='sunken', font=('times new roman', 12))
        I_D.grid(row=1, column=2)
        n_ame = Entry(tk, width=20, bg='lime', fg='brown', relief='sunken', font=('times new roman', 12))
        n_ame.grid(row=2, column=2)
        a_ge = Entry(tk, width=20, bg='lime', fg='brown', relief='sunken', font=('times new roman', 12))
        a_ge.grid(row=3, column=2)
        a_ddress = Entry(tk, width=20, bg='lime', fg='brown', relief='sunken', font=('times new roman', 12))
        a_ddress.grid(row=4, column=2)
        s_alary = Entry(tk, width=20, bg='lime', fg='brown', relief='sunken', font=('times new roman', 12))
        s_alary.grid(row=5, column=2)
        q_ualification = Entry(tk, width=20, bg='lime', fg='brown', relief='sunken', font=('times new roman', 12))
        q_ualification.grid(row=6, column=2)
        d_epartment = StringVar(tk)
        dept_list = ["Accounting", "HR", "Technical", "Production", "Marketing",
                     "Management", "Security", "Public relations"]  # list for available departments
        dept_option = OptionMenu(tk, d_epartment, *dept_list)
        dept_option.configure(width=20, bg='blue', fg='black', font=('times new roman', 10))
        dept_option.grid(row=7, column=2)
        y_ear_recruited = Entry(tk, width=20, bg='lime', fg='brown', relief='sunken', font=('times new roman', 12))
        y_ear_recruited.grid(row=8, column=2)
        c_ell_number = Entry(tk, width=20, bg='lime', fg='brown', relief='sunken', font=('times new roman', 12))
        c_ell_number.grid(row=9, column=2)
        b_ranch= Entry(tk, width=20, bg='lime', fg='brown', relief='sunken', font=('times new roman', 12))
        b_ranch.grid(row=10, column=2)

        
        def submit():  #  function to validate information entered and insert it into db if valid
            dumb = str('check')
            dummy = type(dumb)  #  function to set dummy as representative of string variable       
            if int(I_D.get()) in range(0, 100):
                ID = int(I_D.get())  #condition to check if ID value entered is an integer within 0 and 100
            else:
                tkinter.messagebox.showerror('Invalid ID data', 'out of range or wrong data type')
                
            #####    condition to check if name is a string and not a space
            if  (n_ame.get().isspace() == False) and (type(n_ame.get()) == dummy):
                name = str(n_ame.get())
            else:
                tkinter.messagebox.showerror('Invalid Name data', 'out of range or wrong data type')
                
            ####   condition to check if address is a string and not a space
            if  (a_ddress.get().isspace() == False) and (type(a_ddress.get()) == dummy):
                address = str(a_ddress.get())
            else:
                tkinter.messagebox.showerror('Invalid Address data', 'out of range or wrong data type')
                
            ####   condition to check if qualification is not a string and not a space
            if  (q_ualification.get().isspace() == False) and (type(q_ualification.get()) == dummy):
                qualification = str(q_ualification.get())
            else:
                tkinter.messagebox.showerror('Invalid Qualification data', 'out of range or wrong data type')
                
            ####  allocation of the option selected from department list to the variable department
            department = d_epartment.get()
            
            ####   condition to check if address is a string and not a space
            if  (b_ranch.get().isspace() == False) and (b_ranch.get().isalnum() == True):
                branch = str(b_ranch.get())
            else:
                tkinter.messagebox.showerror('Invalid branch data', 'out of range or wrong data type')
                
            ####  condition to check if age is a digit in the legal working age 18 to 65
            if (a_ge.get().isdigit() == True) and (int(a_ge.get()) in range(17, 66)):
                age = int(a_ge.get())
            else:
                tkinter.messagebox.showerror('Invalid Age data', 'out of range or wrong data type')
                
            ####  codition to check if salary is a digit within the legal standard 100 to 6000
            if (s_alary.get().isdigit() == True) and (int(s_alary.get()) in range(99, 6001)):
                salary = float(s_alary.get())
            else:
                tkinter.messagebox.showerror('Invalid salary data', 'out of range or wrong data type')
                
            ####  condition to check if year recruited is within range of 47 years backwards
            if (y_ear_recruited.get().isdigit() == True) and (int(y_ear_recruited.get()) in range(current_year-47, current_year)):
                year_recruited =  int(y_ear_recruited.get())
            else:
                tkinter.messagebox.showerror('Invalid year of recruitment data', 'out of range or wrond data type')

            ####  condition to ckeck if cell number  is an integer in range lenth 5 to 14
            if (c_ell_number.get().isdigit() == True) and (int(c_ell_number.get()) in range(9999, 1000000000)):
                    cell_number = int(c_ell_number.get())
            else:
                tkinter.messagebox.showerror('Invalid cell number data', 'out of range or wrong data type')            

            ### Code to insert entered values into  database if it is valid    
            import sqlite3
            conn = sqlite3.connect('hr.db')
            insert = 'INSERT INTO tblCOMPANY(ID,NAME,AGE,ADDRESS,SALARY,QUALIFICATION,DEPARTMENT,YEAR_RECRUITMENT,CELL_NUMBER,BRANCH) VALUES(?,?,?,?,?,?,?,?,?,?)'
            conn.execute(insert,[(ID),(name),(age),(address),(salary),(qualification),(department),(year_recruited),(cell_number),(branch)])
            conn.commit()
            Success_msg = ('You have successfully added a new employee', ID)
            tkinter.messagebox.showinfo('Employee successfully added', Success_msg) 
            conn.close()
        submit_button = Button(tk, text='Submit', width=10, height=2, bg='plum', fg='white', relief='groove'
                                       , font=('times new roman', 12), command=submit).grid(row=10, column=3)
        ### function to clear all entries for new entry
        def reset_all():
            I_D.delete(0, END)
            n_ame.delete(0, END)
            a_ge.delete(0, END)
            a_ddress.delete(0, END)
            s_alary.delete(0, END)
            q_ualification.delete(0, END)
            c_ell_number.delete(0, END)
            y_ear_recruited.delete(0, END)
            b_ranch.delete(0, END)
        reset_button = Button(tk, text='Reset', width=10, height=2, bg='yellow', fg='white', relief='groove'
                            , font=('times new roman', 12), command=reset_all).grid(row=9, column=3)

        ### function to exit hr new window
        def e_xit_tk():
            import tkinter.messagebox
            #  dialogue to check exit confirmation
            reply = tkinter.messagebox.askquestion('SYSTEM EXIT', 'Do you truly want to exit?')
                                                       
            if reply == 'yes':
                tk.destroy()
        exit_button = Button(tk, text='Exit', width=5, height=5, bg='red', fg='white', relief='groove'
                            , font=('times new roman', 12), command=e_xit_tk).place(x=443, y=207)
        
        
        tk.mainloop()  #  commitment to prevent window from just poping up and disappearing

    ### module to view db information in a console window           
    def view_tab():
        import sqlite3
        conn = sqlite3.connect('hr.db')
        cursor = conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY,QUALIFICATION, DEPARTMENT,YEAR_RECRUITMENT,CELL_NUMBER,BRANCH FROM tblCOMPANY")
        for row in cursor:  #  loop to display each and every entity one by one in seperate lines
            print("ID = :", row[0])
            print("NAME =               :", row[1])
            print("AGE =                :", row[2])
            print("ADDRESS =            :", row[3])
            print("SALARY =             :", row[4])
            print("QUALIFICATION =      :", row[5])
            print("DEPARTMENT =         :", row[6])
            print("YEAR RECRUITED  =    :", row[7])
            print("CELL NUMBER =        :", row[8])
            print("BRANCH =             :", row[9], "\n")

    ###  function to display all info in the tblCOMPANY tabel on a gui screen

    def gui_display_db_data():
        import sqlite3
        conn = sqlite3.connect('hr.db')
        cursor = conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY,QUALIFICATION, DEPARTMENT,YEAR_RECRUITMENT,CELL_NUMBER,BRANCH FROM tblCOMPANY")
        ### query to to select all fields
        def data():
            ### loop to display all data in in a line by line format
            for row in cursor:
               ID_prefix = ('Worker ID', row[0]) 
               Label(frame,text=ID_prefix, font=('courier new', 12), width=30, fg='steel blue', bg='grey').pack()
               string = ('|',row[1],'|',           '|',row[2],'|',          '|',row[3],'|',         '|',row[4],'|',
                                   '|',row[5],'|',          '|',row[6],'|',         '|',row[7],'|',         '|','+263', row[8],'|',         '|',row[9],'|',)
               Label(frame,text=string, font=('courier new', 12), width=130, fg='yellow', bg='grey').pack()
               
                  
        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"),width=1280,height=600)
        import tkinter
        gui=Tk()  #  name of gui for displaying db information named 'gui'
        gui.geometry("1280x720+0+0")
        gui.title('All items in employee table')
        gui.configure(bg='plum', bd=5)
        

        myframe=Frame(gui,relief=GROOVE,width=1260,height=600,bd=2)
        myframe.place(x=15,y=15)

        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myfunction)
        data()
        gui.mainloop()

    ### function to delete an employee from tblCOMPANY    
    def delete_entity():
        import tkinter
        deltk = Tk()
        deltk.minsize(500, 200)
        deltk.maxsize(500, 325)
        deltk.title('Delete Individual')
        deltk.configure(bg='white', bd=5)
        label = Label(deltk, text='Please enter ID of target record', width=20, bg='gray', fg='yellow',
                      relief='flat', font=('times new roman', 12)).place(x=10, y=20)      
        redundant = Entry(deltk, width=20, bg='lime', fg='brown', relief='sunken', font=('times new roman', 12))
        redundant.place(x=200, y=20)
        ### code to confirm if user truly wants to delete an employee
        def del_confirm():
            import sqlite3
            conn = sqlite3.connect('hr.db')
            del_line = 'DELETE from tblCOMPANY where ID=(?)'
            import tkinter.messagebox
            reply = tkinter.messagebox.askquestion('Delete item', 'Are you sure you want to delete this pearmanantly?')
            if reply == 'yes':
                cursor = conn.execute(del_line, [(redundant.get())])
        delete_button = Button(deltk, text='Delete', fg='white', bg='red', width=8, height=2, bd=2,
                                     relief='flat', font=('times new roman', 16), command=del_confirm).place(x=300, y=20)
        deltk.mainloop()
    ### code to display data read, write, append, delete if user enterscorrect login credentials 
    def display():
        hr_new_button = Button(win, text='New employee', width=10, height=5, bg='grey', fg='yellow',
                                   font=('times new roman', 16), relief='ridge', bd=5, command=hrnew).place(x=0, y=120)
        view_all_button = Button(win, text='View all', width=10, height=5, bg='blue', fg='orange',
                                   font=('times new roman', 16), relief='ridge', bd=5, command=view_tab).place(x=150, y=120)
        del_ind_button = Button(win, text='Delete item', width=10, height=5, bg='pink', fg='purple',
                                   font=('times new roman', 16), relief='ridge', bd=5, command=delete_entity).place(x=0, y=300)     
        view_all_button_gui = Button(win, text='View all gui', width=10, height=5, bg='orange', fg='lime',
                               font=('times new roman', 16), relief='ridge', bd=5, command=gui_display_db_data).place(x=150, y=300)

    ### function to exit database    
    def e_xit():
        import tkinter.messagebox
        reply = tkinter.messagebox.askquestion('DATABASE SYSTEM EXIT', 'Do you truly want to exit?')
        #  condition to check if user truly wants to exit                                         
        if reply == 'yes':
            win.destroy()
        
    ### function to check if check user login credentials before batabase password
    sysdbcode = str("royal2019")  ### correct database access password
    sysdbuser = str('patrick_madzamba')  ### correct database access username
    def security():
        passcode = str(Passcode.get())
        username = str(Db_user_name.get())
        ###  condition to check if login credentials match the correct ones
        if (passcode == str(sysdbcode)) and (username == sysdbuser):
            display()
            Passcode.delete(0, END)
            coverlabel = Label(win, text="*", bg='aqua', relief='flat', fg="white",
                               font=('algerian', 18, 'bold'), height=4).grid(row=1, column=1)
            coverlabel = Label(win, text="***********************welcome***********************",
                               bg='aqua', relief='ridge', fg="white", font=('freesansbold', 18, 'bold'), height=3)
            coverlabel.place(x=0, y=0)
        else:
            ### message output if user enters incorrect password or username
           import tkinter.messagebox
           tkinter.messagebox.showerror('Wrong login details', 'WRONG PASSWORD AND/OR USERNAME PLEASE RETRY')
           Passcode.delete(0, END)
           Db_user_name.delete(0, END)
    ### buuton to submit login in credentials for system validation
    submit_passcode_button = Button(win, text='»›Enter«‹', relief='sunken', width=8, height=2, font=('times new roman', 16),
                                    bg='lime', fg='blue', command=security).place(x=400, y=10)
    exit_button = Button(win, text='Exit', fg='white', bg='red', width=8, height=2, bd=2,
                                     relief='flat', font=('times new roman', 16), command=e_xit).place(x=400, y=120)
    
    usernamelabel= Label(win, text='Username', fg='blue', bg='brown',
                                    relief='groove', width=20, font=('freesansbold', 12))   
    passwordlabel= Label(win, text='Password', fg='blue', bg='brown',
                                    relief='groove', width=20, font=('freesansbold', 12))
    Db_user_name = Entry(win, width=15, fg='plum', bg='grey', relief='sunken', font=('courier new', 12), show='ɸ')
    Passcode = Entry(win, width=15, fg='plum', bg='grey', relief='sunken', font=('courier new', 12), show='*')
    
    usernamelabel.place(x=10, y=5)
    passwordlabel.place(x=10, y=35)
    Db_user_name.place(x=240, y=10)
    Passcode.place(x=240, y=35)

    win.mainloop()
        


#  *****End HR database module*******# ''')

brute_force_help = str('''import random
pincode = input('Enter password    :')
y = int(0)
x = str()
while x != str(pincode):
    probability = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
                   'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    c1 = random.choice(probability)
    c2 = random.choice(probability)
    c3 = random.choice(probability)
    c4 = random.choice(probability)
    xx = (c1,c2,c3,c4)
    x = (''.join(xx))
    y = y+1
    xli = []
    xli.append(x)
    print("".join(x))
print_out =  ('test successful at attempt #',y)   
print('test successful at attempt #',y)
print('******************operation brute force accomplished******************')
from tkinter import messagebox
tkinter.messagebox.showinfo('result', print_out)''')

sahara_browser_help = str('''# ###################################################################################
# ------------------------------ABOUT THE PROGRAM - ------------------------------  #
#    Program name : Sahara Browser     1.0                                          #
#    Program description : browser prototype with a video downloading               #
#                                              function and dreadnaught             #
#    mzinyoni7@gmail.com, mzinyoni7@outlook.com, +263 771 588 144, 784528370        #
#    Author : MIKE ZINYONI                                                          #
#    Date : 1 April 2019                                                            #
#                                                                                   #                                                                         #
#    BRICKS COOPERATION ™                                                           #
# ###################################################################################
import subprocess
from time import strftime
x = strftime("%Y")
if x > str(2019):
    import tkinter.messagebox
    reply = tkinter.messagebox.askquestion('EXPIRED PRODUCT', 'SYSTEM ACCESS DENIED, YOUR AUTO ACCOUNTING LICENCE HAS EXPIRED, RENEW LICENCE ?')
    if reply == 'yes':
        tkinter.messagebox.showinfo('RENEW AA LICENCE', 'visit www.mykapps.com to download the latest edition of auto accounting')
    print('trial time is over renew licence')
    quit()
    exit()

import webbrowser
from tkinter import *

root = Tk()
root.configure(bg='white', bd=5)
root.geometry('1200x600+0+0')
root.title('Sahara')
label = Label(root, text='BRICKS COOPERATION ™ ', fg='white',
              bg='black', font=('courier', 8, 'bold', 'underline')).place(x=1200, y=700)


#scrollbar = Scrollbar(root)
#scrollbar.place(x= 1200, y = 2)

def SVB():
    new = 1
    def download1():
        urld = 'https://en.savefrom.net/#url='+ str(yburl1.get())
        webbrowser.open(urld, new=new)

    new = 1
    def download2():
        urld2 = 'https://en.savefrom.net/#url='+ str(yburl2.get())
        webbrowser.open(urld2, new=new)

    new = 1
    def download3():
        urld3 = 'https://en.savefrom.net/#url='+ str(yburl3.get())
        webbrowser.open(urld3, new=new)

    new = 1
    def download4():
        urld4 = 'https://en.savefrom.net/#url='+ str(yburl4.get())
        webbrowser.open(urld4, new=new)

    new = 1
    def download5():
        urld5 = 'https://en.savefrom.net/#url='+ str(yburl5.get())
        webbrowser.open(urld5, new=new)        
        
    
    pp = Tk()
    pp.geometry("450x150")
    pp.title("Sahara Video-Buddy")
    pp.minsize(450, 300)
    pp.maxsize(1000, 730)
    pp.config(bg='white', bd=5)

    def dum():
        print('')
    google = PhotoImage(file="SVD.png")  # how to add an image or icon
    photo = Label(pp, text="►SAHARA▼DOWN¶OADER◄", relief='groove',
                  bg='aqua', fg='pink', font=('times new roman', 24, 'bold')).place(x=220, y=150)
    label = Label(pp, text='BRICKS COORPORATION ™ ', fg='white', bg='black', font=('courier', 8, 'bold', 'underline')).place(x=750, y=700)
    #photo = Button(pp, text=".", image=google, command=dum).place(x=200, y=150)

    

    new = 1
    url = 'https://mail.google.com/mail/'
    def openmail():
        webbrowser.open(url, new=new)


    def suggestions(): 
        import tkinter.messagebox
        reply = tkinter.messagebox.askquestion('FEEDBACK', 'Do you wish to send any suggestions for product '
                                                                            'enhancement. Your continued support is deeply appreciated '
                                                                             ' Please click yes, yours lovingly the author Mike Zinyoni')
        if reply == 'yes':
            openmail()



    def aaa():
        import tkinter.messagebox
        reply = tkinter.messagebox.askquestion('About Sahara video downloader', 'Developed by Mike Zinyoni. MORE INFO?')
        if reply == 'yes':
            tkinter.messagebox.showinfo('Sahara video downloader origins', 'The application was developed in 2019 January by a '
                                                               'Zimbabwean scholar Mike Zinyoni as part . By the time '
                                                                'sir Mikiel developed this desktop application'
                                                                ' he was 17. Sir Mikiel is a natural born intellect'
                                                                ' son of a farmer and a "mother". He is one of '
                                                                'Jehovahs Witnesses. He is also a big time wrestling'
                                                                ' and MMA fan, patriotic citizen, future billionaire '
                                                                'and celeb. He devotes his work to the following '
                                                                'Mitchell Madzamba, C Madzamba, Tavonga Rakata,R '
                                                                'Mukwedeya, K.Chimanga, Chitonga, Matsika and to that'
                                                                ' one unknown African kid who is a tech nerd but '
                                                                'dosent known how to power up a computer, most '
                                                                'importantly to the independant nation of Zimbabwe'
                                                                '                                                                                    '
                                                                'Through out the course of time mike has acquired '
                                                                 'the following titles: MOST WONDERFUL ₱ROGRAMMER Ώ'
                                                                 ' SCOPION KING ᴥ (LORD OF SCOPE), Ṩṃằṙṱ Ẳȿș, '
                                                                 ' Bļäđë man, Ħãŕåříěň šŏłƌıëɍ, warren wolf'
                                                                '                                                                                    '                                                                '                                                                                    '
                                                                '© BRICKS COORPORATION ™ 2019  ® all rights reserved'                                    
                                                                ' ........All in all To GOD BE THE GLORY......... ')

    def blue():
        pp.config(bg='blue', bd=5)
    def grey():
        pp.config(bg='grey', bd=5)
    def plum():
        pp.config(bg='plum', bd=5)
    def aqua():
        pp.config(bg='aqua', bd=5)
    def light():
        pp.config(bg='green', bd=5)
    def yellow():
        pp.config(bg='yellow', bd=5)
    def purple():
        pp.config(bg='purple', bd=5)
    def pink():
        pp.config(bg='pink', bd=5)
    def white():
        pp.config(bg='white', bd=5)
    def silver():
        pp.config(bg='silver', bd=5)
    def gold():
        pp.config(bg='gold', bd=5)
    def black():
        pp.config(bg='black', bd=5)

    def eXit():
        exit
        quit

    
    menu = Menu(pp)
    pp.config(menu=menu)

    submenu = Menu(menu)
    menu.add_cascade(label="FILE", menu=submenu)
    submenu.add_command(label="Print window", command=black)
    submenu.add_separator()
    submenu.add_command(label="EXIT", command=eXit)

    editmenu = Menu(menu)
    menu.add_cascade(label="CONFIGURE", menu=editmenu)
    editmenu.add_command(label="Blue bg", command=blue)
    editmenu.add_command(label="Grey bg", command=grey)
    editmenu.add_command(label="Plum bg", command=plum)
    editmenu.add_separator()
    editmenu.add_command(label="Aqua bg", command=aqua)
    editmenu.add_command(label="Green bg", command=light)
    editmenu.add_command(label="Yellow bg", command=yellow)
    editmenu.add_separator()
    editmenu.add_command(label="Purple bg", command=purple)
    editmenu.add_command(label="Black bg", command=black)
    editmenu.add_command(label="Pink bg", command=pink)
    editmenu.add_separator()
    editmenu.add_command(label="Gold bg", command=gold)
    editmenu.add_command(label="White bg", command=white)
    editmenu.add_command(label="Silver bg", command=silver)


    feedbackmenu = Menu(menu)
    menu.add_cascade(label="FEEDBACK", menu=feedbackmenu)
    feedbackmenu.add_command(label="Suggestions ««««««", command=suggestions)
    feedbackmenu.add_separator()
    feedbackmenu.add_command(label="Rate us ♥♥♥♥♥", command=suggestions)
    feedbackmenu.add_separator()


    helpmenu = Menu(menu)
    menu.add_cascade(label="ABOUT", menu=helpmenu)
    helpmenu.add_command(label="About Sahara video downloader", command=aaa)
    helpmenu.add_separator()


    dummy = Label(pp, text='.', bg='white', height=15, width=5).grid(row=0, column=0)
    
    label = Label(pp, text='Paste video url 1', font=('Castellar', 14, 'italic'), bg='orange', fg='lime').grid(row=2, column=1)
    yburl1 = StringVar()
    e = Entry(pp, textvariable=yburl1, bg='white', fg='black', bd=5, width=30, font=('courier', 20, 'italic')).grid(row=2, column=2)
    gsearch_button = Button(pp, text="download", width=4, height=2, bg="red", relief='groove', fg='white', command=download1).grid(row=2, column=3)
    
    label = Label(pp, text='Paste video url 2', font=('Castellar', 14, 'italic'), bg='plum', fg='aqua').grid(row=3, column=1)
    yburl2 = StringVar()
    e = Entry(pp, textvariable=yburl2, bg='white', fg='black', bd=5, width=30, font=('courier', 20, 'italic')).grid(row=3, column=2)
    gsearch_button = Button(pp, text="download", width=4, height=2, bg="yellow", relief='groove', fg='white', command=download2).grid(row=3, column=3)
    
    label = Label(pp, text='Paste video url 3', font=('Castellar', 14, 'italic'), bg='blue', fg='orange').grid(row=4, column=1)
    yburl3 = StringVar()
    e = Entry(pp, textvariable=yburl3, bg='white', fg='black', bd=5, width=30, font=('courier', 20, 'italic')).grid(row=4, column=2)
    gsearch_button = Button(pp, text="download", width=4, height=2, bg="green", relief='groove', fg='white', command=download3).grid(row=4, column=3)

    label = Label(pp, text='Paste video url 4', font=('Castellar', 14, 'italic'), bg='cyan', fg='black').grid(row=5, column=1)
    yburl4 = StringVar()
    e = Entry(pp, textvariable=yburl4, bg='white', fg='black', bd=5, width=30, font=('courier', 20, 'italic')).grid(row=5, column=2)
    gsearch_button = Button(pp, text="download", width=4, height=2, bg="black", relief='groove', fg='white', command=download4).grid(row=5, column=3)
    
    label = Label(pp, text='Paste video url 5', font=('Castellar', 14, 'italic'), bg='pink', fg='white').grid(row=6, column=1)
    yburl5 = StringVar()
    e = Entry(pp, textvariable=yburl5, bg='white', fg='black', bd=5, width=30, font=('courier', 20, 'italic')).grid(row=6, column=2)
    gsearch_button = Button(pp, text="download", width=4, height=2, bg="blue", relief='groove', fg='white', command=download5).grid(row=6, column=3)
        

    

    pp.mainloop()




new = 1
def dino():
    urldino = 'https://chrome://dino'
    webbrowser.open(urldino, new=new)

new = 1
urldocs = 'https://docs.google.com/document/'
def opendocs():
    webbrowser.open(urldocs, new=new)
        
new = 1
def google_search():
    url1 = 'https://www.google.com/search?q='+ str(gsearch.get())
    webbrowser.open(url1, new=new)


new = 1
url = 'https://mail.google.com/mail/'
def openmail():
    webbrowser.open(url, new=new)


new = 1
urlyoutube = 'https://www.youtube.com/'
def openyoutube():
    webbrowser.open(urlyoutube, new=new)


new = 1
urluptodown = 'https://uptodown.com/windows'
def openmail():
    webbrowser.open(urluptodown, new=new)




def suggestions(): 
    import tkinter.messagebox
    reply = tkinter.messagebox.askquestion('FEEDBACK', 'Do you wish to send any suggestions for product '
                                                                            'enhancement. Your continued support is deeply appreciated '
                                                                             ' Please click yes, yours lovingly the author Mike Zinyoni')
    if reply == 'yes':
        openmail()



def aaa():
    import tkinter.messagebox
    reply = tkinter.messagebox.askquestion('About Sahara', 'Developed by Mike Zinyoni. MORE INFO?')
    if reply == 'yes':
        tkinter.messagebox.showinfo('Sahara Browser origins', 'The application was developed in 2019 January by a '
                                                               'Zimbabwean scholar Mike Zinyoni as part . By the time '
                                                                'sir Mikiel developed this desktop application'
                                                                ' he was 17. Sir Mikiel is a natural born intellect'
                                                                ' son of a farmer and a "mother". He is one of '
                                                                'Jehovahs Witnesses. He is also a big time wrestling'
                                                                ' and MMA fan, patriotic citizen, future billionaire '
                                                                'and celeb. He devotes his work to the following '
                                                                'Mitchell Madzamba, C Madzamba, Tavonga Rakata,R '
                                                                'Mukwedeya, K.Chimanga, Chitonga, Matsika and to that'
                                                                ' one unknown African kid who is a tech nerd but '
                                                                'dosent known how to power up a computer, most '
                                                                'importantly to the independant nation of Zimbabwe'
                                                                '                                                                                    '
                                                                'Through out the course of time mike has acquired '
                                                                 'the following titles: MOST WONDERFUL ₱ROGRAMMER Ώ'
                                                                 ' SCOPION KING ᴥ (LORD OF SCOPE), Ṩṃằṙṱ Ẳȿș, '
                                                                 ' Bļäđë man, Ħãŕåříěň šŏłƌıëɍ, warren wolf'
                                                                '                                                                                    '                                                                '                                                                                    '
                                                                '© BRICKS COORPORATION ™ 2019  ® all rights reserved'                                    
                                                                ' ........All in all To GOD BE THE GLORY......... ')

def blue():
    root.config(bg='blue', bd=5)
def grey():
    root.config(bg='grey', bd=5)
def plum():
    root.config(bg='plum', bd=5)
def aqua():
    root.config(bg='aqua', bd=5)
def light():
    root.config(bg='green', bd=5)
def yellow():
    root.config(bg='yellow', bd=5)
def purple():
    root.config(bg='purple', bd=5)
def pink():
    root.config(bg='pink', bd=5)
def white():
    root.config(bg='white', bd=5)
def silver():
    root.config(bg='silver', bd=5)
def gold():
    root.config(bg='gold', bd=5)
def black():
    root.config(bg='black', bd=5)

def eXit():
    exit
    quit

    
menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="FILE", menu=submenu)
submenu.add_command(label="Print window", command=black)
submenu.add_separator()
submenu.add_command(label="EXIT", command=eXit)

editmenu = Menu(menu)
menu.add_cascade(label="CONFIGURE", menu=editmenu)
editmenu.add_command(label="Blue bg", command=blue)
editmenu.add_command(label="Grey bg", command=grey)
editmenu.add_command(label="Plum bg", command=plum)
editmenu.add_separator()
editmenu.add_command(label="Aqua bg", command=aqua)
editmenu.add_command(label="Green bg", command=light)
editmenu.add_command(label="Yellow bg", command=yellow)
editmenu.add_separator()
editmenu.add_command(label="Purple bg", command=purple)
editmenu.add_command(label="Black bg", command=black)
editmenu.add_command(label="Pink bg", command=pink)
editmenu.add_separator()
editmenu.add_command(label="Gold bg", command=gold)
editmenu.add_command(label="White bg", command=white)
editmenu.add_command(label="Silver bg", command=silver)


feedbackmenu = Menu(menu)
menu.add_cascade(label="FEEDBACK", menu=feedbackmenu)
feedbackmenu.add_command(label="Suggestions ««««««", command=suggestions)
feedbackmenu.add_separator()
feedbackmenu.add_command(label="Rate us ♥♥♥♥♥", command=suggestions)
feedbackmenu.add_separator()


helpmenu = Menu(menu)
menu.add_cascade(label="ABOUT", menu=helpmenu)
helpmenu.add_command(label="About Sahara", command=aaa)
helpmenu.add_separator()















dummy_grid = Label(root, text='.', width=15, height=7, bg="black", bd=5, fg='plum').grid(row=0, column=1)
dummy_grid = Label(root, text='.', width=15, height=7, bg="white", bd=5, fg='plum').grid(row=1, column=1)
dummy_grid = Label(root, text='.', width=15, height=7, bg="cyan", bd=5, fg='plum').grid(row=2, column=1)
dummy_grid = Label(root, text='.', width=15, height=7, bg="plum", bd=5, fg='plum').grid(row=3, column=1)
dummy_grid = Label(root, text='.', width=15, height=1, bg="orange", bd=5, fg='plum').grid(row=5, column=1)
dummy_grid = Label(root, text='.', width=15, height=7, bg="lime", bd=5, fg='plum').grid(row=6, column=1)




def mk():
    print('hello world')




gsearch_label = Label(root, text='Search google', font=('Castellar', 16, 'italic'), bg='orange', fg='black').place(x=125, y=405)
gsearch = StringVar()
g = Entry(root, textvariable=gsearch, bg='white', fg='black', bd=5, width=35, font=('times new roman', 20)).place(x=325, y=400)
google = PhotoImage(file="google.png")
gsearch_button = Button(root, image=google, text="search", width=40, height=40, bg="plum", relief='groove', fg='white', command=google_search).place(x=818, y=400)

google_sahara = PhotoImage(file="ggg.png")  # how to add an image or icon
photo = Label(root, image=google_sahara, relief='sunken').place(x=350, y=300)



ig = PhotoImage(file='ig.png')
instagram = Button(root, text="INSTAGRAM", image=ig, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=4, column=2)
facebook = PhotoImage(file='facebook.png')
FACEBOOK = Button(root, text="FACEBOOK  ", image=facebook, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=4, column=3)
twitter = PhotoImage(file='twitter.png')
TWITTER = Button(root, text="TWITTER     ", image=twitter, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=4, column=4)
snapchat = PhotoImage(file='snapchat.png')
SNAPCHART= Button(root, text="SNAPCHAT  ", image=snapchat, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=4, column=5)


gmail = PhotoImage(file='gmail.png')
GMAIL = Button(root, text="GMAIL", image=gmail, width=100, height=100, bg="steel blue", fg='plum', command=openmail).grid(row=6, column=2)  # done
gdrive = PhotoImage(file='gdrive.png')
GDRIVE= Button(root, text="GOOGLE DRIVE ", image=gdrive, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=6, column=3)
photo = PhotoImage(file='photo.png')
GPHOTOS = Button(root, text="GOOGLE PHOTOS", image=photo, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=6, column=4)
doc = PhotoImage(file='doc.png')
GDOCUMENTS = Button(root, text="GOOGLE DOCUMENTS", image=doc, width=100, height=100, bg="steel blue", fg='plum', command=opendocs).grid(row=4, column=10) #  done

outlook = PhotoImage(file='outlook.png')
OUTLOOK = Button(root, text="OUTLOOK", image=outlook, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=4, column=8)
skype = PhotoImage(file='skype.png')
SKYPE = Button(root, text="SKYPE", image=skype, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=6, column=8)
msstore = PhotoImage(file='ms store.png')
MICROSOFT = Button(root, text="MICROSOFT STORE", image=msstore, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=4, column=6)
dropbox = PhotoImage(file='dropbox.png')
DROPBOX = Button(root, text="DROPBOX", image=dropbox, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=6, column=6)


youtube = PhotoImage(file='youtube.png')
YOUTUBE = Button(root, text="YOUTUBE", image=youtube, width=100, height=100, bg="steel blue", fg='plum', command=openyoutube).grid(row=4, column=9) #done
uptodown = PhotoImage(file='uptodown.png')
UPTODOWN = Button(root, text="UPTODOWN", image=uptodown, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=6, column=9) # done
jw = PhotoImage(file='jw.png')
JW = Button(root, text="JW", image=jw, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=4, column=7)
xbox = PhotoImage(file='xbox.png')
XBOX = Button(root, text="X BOX", image=xbox, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=6, column=7)


amazon = PhotoImage(file='amazon.png')
AMAZON = Button(root, text="AMAZON", image=amazon, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=3, column=10)
pinterest = PhotoImage(file='pinterest.png')
PINTEREST = Button(root, text="PINTEREST", image=pinterest, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=3, column=9)
msnews = PhotoImage(file='msnews.png')
MICROSOFT = Button(root, text="MICROSOFT NEWS", image=msnews, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=6, column=10)
msn = PhotoImage(file='msn.png')
MSN = Button(root, text="MSN MONEY", image=msn, width=100, height=100, bg="steel blue", fg='plum', command=mk).grid(row=6, column=5)


mykwifi = PhotoImage(file='mykwifi.png')
MYKWIFI = Button(root, text="DREAD NAUGHT", image=mykwifi, width=100, height=100, bg="white", fg='plum', command=mk).grid(row=2, column=9)
sahara = PhotoImage(file='sahara.png')
SAHARA_DOWNLOAD = Button(root, text="SAHARA VIDEO DOWNLOAD", image=sahara, width=100, height=100, bg="steel blue", fg='plum', command=SVB).grid(row=2, column=10)

#   ===============================accessories=================================== #
chromedino = Button(root, text="dino game", width=15, height=1, bg="steel blue", fg='plum', command=dino).grid(row=5, column=2) #  done



root.mainloop()


# ###############################################################
# ------------------------------ABOUT THE PROGRAM - ------------------------------                                  #
#    Program name : Sahara Browser     1.0                                                                                    #
#    Program description : browser prototype with a video downloading                                  #
#                                                                                                  function and dreadnaught             # 
#    mzinyoni7@gmail.com, mzinyoni7@outlook.com, +263 771 588 144, 784528370        #
#    Author : MIKE ZINYONI                                                                                                            #
#    Date : 1 April 2019                                                                                                                     #
#                                                                                                                                                           #
#    BRICKS COORPORATION ™                                                                                                   #
# ###############################################################
''')



service_year_report_help = str(''' # ###############################################################
# ------------------------------ABOUT THE PROGRAM - -------------#
#    Program name : Ministry Assistant1.0                         ########################
#    Program description : tkinter app for keeping a publishers ministry data            # 
#    mzinyoni7@gmail.com, mzinyoni7@outlook.com, +263 771 588 144, +263 784528370        #
#    Author : MIKE ZINYONI                                       ########################
#    Date : 28 September 2019                                    #
#                                                                #
#    BRICKS COORPORATION ™                                       #
# ###############################################################



from tkinter import *
root = Tk()
root.title('Ministry Assistant')
root.geometry('1x1+500+0')
root.minsize(400, 600)
root.maxsize(400, 600)
import sqlite3
conn = sqlite3.connect('JW.db')
import time
from time import strftime
month_day = strftime("%d") 
month = strftime("%B")
year = strftime("%Y")
from datetime import date
today = date.today()
insert = 'INSERT INTO ministry(Date,Day,Month,Year,Hours,Literiture,Videos,Returns,Studies,Partner,Ministry_type) VALUES(?,?,?,?,?,?,?,?,?,?,?)'

bgg = PhotoImage(file="JW.png")
Label(root, image=bgg, width=400, height=600).place(x=0, y=0)


### ***************************************** main window menu ************************************
# menu interface for accepting user suggestions
new = 1
url = 'https://mail.google.com/mail/'
def openmail():
    webbrowser.open(url, new=new)


def suggestions(): 
    import tkinter.messagebox
    reply = tkinter.messagebox.askquestion('FEEDBACK',
                                           'Do you wish to send any suggestions for product '
                                            'enhancement. Your continued support is deeply appreciated '
                                             ' Please click yes, yours lovingly the author Mike Zinyoni')
    if reply == 'yes':
        openmail()
# end of menu interface for accepting user suggestions


# menu interface about ministry assistant 1.0

def about_ministry_assistant():
    import tkinter.messagebox
    reply = tkinter.messagebox.askquestion('About Auto Accounting', 'Developed by Mike Zinyoni. MORE INFO?')
    if reply == 'yes':
        tkinter.messagebox.showinfo('Ministry Assistant origins', ''
                                Ministry Assistant was designed and developed by a 
                                Zimbabwean Scholar Mike Zinyoni at the age of 17.
                                Mike is a baptised Jehovah's Witness currently in
                                Bluffhill Congreagation. Mike Zinyoni devotes this
                                work to the following people:
                                * my sister Tanaka who recently became an
                                unbaptised
                                publisher * C Kandoro who encouraged me to pursue
                                programming
                                 * F Gumiremhete & Leon Mubati who encouraged
                                 me to
                                 keep vibrant in the ministry * L Makuwaza,
                                 L kabudura,
                                 C Ngwenya, C Chanetsa, B Mpofu , D Kalunga for
                                 studying
                                 the bible with me. * my mother who helped me
                                 accept the truth
                                 * and to Her + The developers of python 3.7.

                                 This software is not for sale!!!  it is for free
                                 just as I recieved the "truth about jehovah and his
                                 son the truth that is worthy everlasting life for free"
                                  John 3:17.
                                 However Editing the code or removing the Mike
                                 Zinyoni Copyrights is a criminal offence.

                                 Contact Mike Zinyoni for any software solutions
                                 at +263 771 588 144, or +263 784 528 370
                                 mzinyoni7@gmail.com, mzinyoni7@outlook.com

                                 Mike Zinyoni lives with a single mother if
                                 wish to be of any financial assistance please call.

                                 ...All in al to Jehovah be the glory...
                                '')
                    
# end of menu interface about ministry assistant 1.0

# exit menu interface
def exit_root():
    import sys
    sys.exit()

# end of exit menu interface

# date and time interface on menu


import time

from time import strftime
def aaclock():
    weekday = strftime("%A")
    month_day = strftime("%d") 
    month = strftime("%B")
    year = strftime("%Y")
    hour_12  = strftime("%I")
    hour_24 = strftime("%H") 
    minute = strftime("%M") 
    #second  = strftime("%s") #
    #micro_second  = strftime("%f") #
    pm_am = strftime("%p")
    timezone  = strftime("%Z")
    year_day  = strftime("%j")
    year_week  = strftime("%U")
    actual_date =  strftime("%c")
    def showtime():
        import tkinter

        clockroot = Tk()
        clockroot.geometry("450x450")
        clockroot.minsize(400, 350)
        clockroot.maxsize(400, 350)
        clockroot.title("Auto Accounting Date & Time info ☼")
        clockroot.config(bg='white', bd=10)
        
        lbl = Label(clockroot, text='Weekday', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=1, column=1)
        lbl = Label(clockroot, text=weekday, width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=1, column=2)

        
        lbl = Label(clockroot, text='Day', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=2, column=1)
        lbl = Label(clockroot, text=month_day, width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=2, column=2)

                
        lbl = Label(clockroot, text='Month', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=3, column=1)
        lbl = Label(clockroot, text=month, width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=3, column=2)
                
        lbl = Label(clockroot, text='Year', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=4, column=1)
        lbl = Label(clockroot, text=year, width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=4, column=2)
                
        lbl = Label(clockroot, text='Time', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=5, column=1)
        lbl = Label(clockroot, text=hour_12, width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=5, column=2)
        lbl = Label(clockroot, text=pm_am, width='5', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=5, column=3)

                
        lbl = Label(clockroot, text='Time', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=6, column=1)
        lbl = Label(clockroot, text=hour_24, width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=6, column=2)        
        lbl = Label(clockroot, text='24hr', width='5', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=6, column=3)

        lbl = Label(clockroot, text='Minute', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=7, column=1)
        lbl = Label(clockroot, text=strftime("%M"), width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=7, column=2)
        def update():
                    lbl = Label(clockroot, text='Minute', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=7, column=1)
                    lbl = Label(clockroot, text=strftime("%M"), width='15', bg='cyan', fg='black',
                            font=('times new roman', 14), relief='sunken').grid(row=7, column=2)
                    lbl = Label(clockroot, text='Date', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=11, column=1)
                    lbl = Label(clockroot, text=strftime("%c"), width='15', bg='cyan', fg='black',
                                font=('times new roman', 14), relief='sunken').grid(row=11, column=2)

        lbl = Label(clockroot, text='Timezone', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=8, column=1)
        lbl = Label(clockroot, text=timezone, width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=8, column=2)

        lbl = Label(clockroot, text='Day of year', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=9, column=1)
        lbl = Label(clockroot, text=year_day, width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=9, column=2)

        lbl = Label(clockroot, text='Week of year', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=10, column=1)
        lbl = Label(clockroot, text=year_week, width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=10, column=2)

        
        lbl = Label(clockroot, text='Date', width='20', bg='cyan', fg='navy blue',
                           font=('times new roman', 12), relief='groove').grid(row=11, column=1)
        lbl = Label(clockroot, text=actual_date, width='15', bg='cyan', fg='black',
                         font=('times new roman', 14), relief='sunken').grid(row=11, column=2)
        
        lbl = Button(clockroot, text='Update', width='13', bg='plum', fg='aqua',
                         font=('times new roman', 14), relief='sunken', command=update).grid(row=12, column=2)
        
        clockroot.mainloop()
    showtime()

# end of date and time interface on menu
                                    
menu = Menu(root)
root.config(menu=menu)

filerootmenu = Menu(menu)  #  file menu on root window
menu.add_cascade(label="FILES", menu=filerootmenu)
filerootmenu.add_command(label="Exit", command=exit_root)
filerootmenu.add_separator()
filerootmenu.add_command(label="Date and time", command=aaclock)
filerootmenu.add_separator()

helpmenu = Menu(menu)
menu.add_cascade(label="HELP", menu=helpmenu)
helpmenu.add_command(label="About ministry Assistant", command=about_ministry_assistant)
helpmenu.add_separator()
helpmenu.add_command(label="Suggestions", command=suggestions)



### ************************************end of main window menu ************************************

def create_field_service_table():
    conn.execute(''CREATE TABLE IF NOT EXISTS ministry
    (Date PRIMARY KEY NOT NULL,
    Day INT(2) NOT NULL,
    Month VARCHAR(15) NOT NULL,
    Year VARCHAR(4) NOT NULL,
    Hours VARCHAR(1) NOT NULL,
    Literiture VARCHAR(2),
    Videos VARCHAR(2),
    Returns VARCHAR(2),
    Studies VARCHAR(2),
    Partner VARCHAR(20),
    Ministry_type VARCHAR(20) NOT NULL
    );'')
create_field_service_table()


def data_input():
    import tkinter
    win = Tk()
    win.title("today's ministry")
    win.configure(bg='grey', bd=3)
    win.geometry('1x1+500+0')
    win.minsize(400, 600)
    win.maxsize(400, 600)
    Label(win, text='Date', width=20, bg='navy blue', fg='brown', relief='flat', font=('georgia', 12)).grid(row=0)
    Label(win, text='Day', width=20, bg='navy blue', fg='brown', relief='flat', font=('georgia', 12)).grid(row=1)
    Label(win, text='Month', width=20, bg='navy blue', fg='brown', relief='flat', font=('georgia', 12)).grid(row=2)
    Label(win, text='Year', width=20, bg='navy blue', fg='brown', relief='flat', font=('georgia', 12)).grid(row=3)
    Label(win, text='Hours', width=20, bg='navy blue', fg='brown', relief='flat', font=('georgia', 12)).grid(row=4)
    Label(win, text='Literiture', width=20, bg='navy blue', fg='brown', relief='flat', font=('georgia', 12)).grid(row=5)
    Label(win, text='Videos', width=20, bg='navy blue', fg='brown', relief='flat', font=('georgia', 12)).grid(row=6)
    Label(win, text='Return visits', width=20, bg='navy blue', fg='brown', relief='flat', font=('georgia', 12)).grid(row=7)
    Label(win, text='Bible studies', width=20, bg='navy blue', fg='brown', relief='flat', font=('georgia', 12)).grid(row=8)
    Label(win, text='Partner', width=20, bg='navy blue', fg='brown', relief='flat', font=('georgia', 12)).grid(row=9)
    Label(win, text='Ministry type', width=20, bg='navy blue', fg='brown', relief='flat',
          font=('georgia', 12)).grid(row=10)
    Label(win, text=today, width=20, bg='aqua', fg='purple',
          relief='flat', font=('georgia', 12)).grid(row=0, column=1)
    Label(win, text=month_day, width=20, bg='aqua', fg='purple',
          relief='flat', font=('georgia', 12)).grid(row=1, column=1)
    Label(win, text=month, width=20, bg='aqua', fg='purple',
          relief='flat', font=('georgia', 12)).grid(row=2, column=1)
    Label(win, text=year, width=20, bg='aqua', fg='purple',
          relief='flat', font=('georgia', 12)).grid(row=3, column=1)
    num_list = []
    for i in range(0, 16):
        num_list.append(i)
    hours = StringVar(win)
    hour_entry = OptionMenu(win, hours, *num_list)
    hour_entry.configure(width=8, bg='blue', fg='black', font=('times new roman', 10))
    hour_entry.grid(row=4, column=1)
    studies = StringVar(win)
    studies_entry = OptionMenu(win, studies, *num_list)
    studies_entry.configure(width=8, bg='blue', fg='black', font=('times new roman', 10))
    studies_entry.grid(row=8, column=1)
    for i in range(17, 30):
        num_list.append(i)    
    rvs = StringVar(win)
    rvs_entry = OptionMenu(win, rvs, *num_list)
    rvs_entry.configure(width=8, bg='blue', fg='black', font=('times new roman', 10))
    rvs_entry.grid(row=7, column=1)
    for i in range(31, 101):
        num_list.append(i)
    literiture = StringVar(win)
    literiture_entry = OptionMenu(win, literiture, *num_list)
    literiture_entry.configure(width=8, bg='blue', fg='black', font=('times new roman', 10))
    literiture_entry.grid(row=5, column=1)
    videos = StringVar(win)
    videos_entry = OptionMenu(win, videos, *num_list)
    videos_entry.configure(width=8, bg='blue', fg='black', font=('times new roman', 10))
    videos_entry.grid(row=6, column=1)
    partner = Entry(win, width=20, bg='white', fg='black',font=('times new roman', 10),
                    relief='sunken')
    partner.grid(row=9, column=1)
    min_type_list = ['Cart', 'Street work', 'House to house', 'Telephone', 'Studies only']
    min_type = StringVar(win)
    min_type_entry = OptionMenu(win, min_type, *min_type_list)
    min_type_entry.configure(width=8, bg='plum', fg='black', font=('times new roman', 10))
    min_type_entry.grid(row=10, column=1)
    def submit_data():
        try:
            h_ours = int(hours.get())
            l_iteriture = int(literiture.get())
            v_ideos = int(videos.get())
            r_vs = int(rvs.get())
            s_tudies = int(studies.get())
            p_artner = str(partner.get())
            m_in_type = str(min_type.get())
            input_data =[(today),(month_day),(month),(year),(h_ours),(l_iteriture),(v_ideos),
                         (r_vs),(s_tudies),(p_artner),(m_in_type)]

            if len(input_data) == 11:
                from tkinter import messagebox
                try:
                    conn.execute(insert, input_data)
                    tdae = (today)
                    Tdae = str(tdae)
                    success = ('''You have successfully submitted infomation for field
                                  service for the day''', str(today))
                    failure = ('''System failed to accept data entered, please check the following:
                                1) Whether you have not already entered data for today's ministry
                                2) Fill in all entry spaces if not applicable pick "0"
                                 for the drop down menu's or type "none" on the partner
                                 entry space
                               ''')
                    conn.commit()
                    tkinter.messagebox.showinfo('Successful data entry', success)
                except:
                    tkinter.messagebox.showerror('Successful data entry', failure)
            else:
                failure = str('Invalid infomation entered. Please enter enter two zeros'
                              'where there is absent data')
                tkinter.messagebox.showerror('Invalid data entry', failure)
        except:
            from tkinter import messagebox
            tkinter.messagebox.showerror('Incomplete', 'Please fillin all entry spaces andoption menus')

            
    def clear_all_win():
        partner.delete(0, END)

    

    def exit_win():
        from tkinter import messagebox
        ex = tkinter.messagebox.askquestion('Exit confirmation', 'Do you truly want to exit?')
        if ex == 'yes':
            win.destroy()
    Button(win, text='Submit info', width=10, relief='groove', bg='purple', fg='lime',
           font=('impact', 12), command=submit_data).place(x=10, y=330)
    Button(win, text='Clear all', width=10, relief='groove', bg='yellow', fg='blue',
           font=('impact', 12), command=clear_all_win).place(x=110, y=330)
    Button(win, text='Exit', width=10, relief='groove', fg='purple', bg='red',
           font=('impact', 12), command=exit_win).place(x=210, y=330)
    win.mainloop()
            
    def clear_all_win():
        min_type_entry.delete(0, END)
        videos_entry.delete(0, END)
        literiture_entry.delete(0, END)
        rvs_entry.delete(0, END)
        partner_entry.delete(0, END)
        studies_entry.delete(0, END)
        hour_entry.delete(0, END)
    
            
    Button(win, text='Submit info', width=10, relief='groove', bg='purple', fg='lime',
           font=('impact', 12), command=submit_data).place(x=10, y=300)
    Button(win, text='Clear all', width=10, relief='groove', bg='green', fg='blue',
           font=('impact', 12), command=clear_all_win).place(x=110, y=300)
    def exit_win():
        ex = tkinter.messagebox.askquestion('Exit confirmation', 'Do you truly want to exit?')
        if ex == 'yes':
            win.destroy()
    Button(win, text='Exit', width=10, relief='groove', bg='purple', fg='lime',
           font=('impact', 12), command=exit_win).place(x=210, y=300)
    win.mainloop()

def show_all_data():
    all_data = conn.execute(''SELECT Date,Day,Month,Year,Hours,Literiture,Videos,Returns,Studies,
                            Partner,Ministry_type FROM ministry'')
    for row in all_data:
        print('Date                             :', row[0])
        print('DAY                              :', row[1])
        print('Month                            :', row[2])
        print('Year                             :', row[3])
        print('Hours                            :', row[4])
        print('Literiture                       :', row[5])
        print('Video Showings                   :', row[6])
        print('Returns visits                   :', row[7])
        print('Bible studies                    :', row[8])
        print('Partner                          :', row[9])
        print('Ministry type                    :', row[10])
        print('*******************************************')
    print('_________________________________________________________________________________________')

def service_report():
    import tkinter
    tk = Tk()
    tk.title('Month to display data on')
    tk.configure(bg='steel blue', bd=10)
    tk.geometry('1x1+500+0')
    tk.minsize(400, 150)
    tk.maxsize(400,150)
    def query_month_data():
        #try:
        m_onth = month_to_query.get()
        day_count = []
        hours_count = []
        literiture_count = []
        videos_count = []
        returns_count = []
        studies_count = []
        m_onth = str(month_to_query.get())
        report = conn.execute(''SELECT Day,Year,Hours,Literiture,Videos,Returns,Studies
                              FROM Ministry WHERE Month = ?'', (m_onth,))
        for row in report:
            day_count.append(row[0])
            hours_count.append(int(row[2]))
            literiture_count.append(int(row[3]))
            videos_count.append(int(row[4]))
            returns_count.append(int(row[5]))
            studies_count.append(int(row[6]))
        ''print('days     :', day_count)
        print('hours    :', hours_count)
        print('lit      :', literiture_count)
        print('vids     :', videos_count)
        print('rvs      :', returns_count)
        print('stud     :', studies_count)''
        
                                 
        num_of_days = len(day_count)
        hours_total = sum(hours_count)
        literiture_total = sum(literiture_count)
        videos_total = sum(videos_count)
        returns_total = sum(returns_count)
        try:
            studies_total = sum(studies_count) / len(studies_count)
        except ZeroDivisionError:
            studies_total = int(0)
        
        print('Field service report for the month :', m_onth)
        print('..................................................................')
        print('Total days went out              :', num_of_days)
        print('Hours                            :', hours_total)
        print('Literiture                       :', literiture_total)
        print('Video Showings                   :', videos_total)
        print('Return visits                    :', returns_total)
        print('Bible studies                    :', studies_total)
        print('...................................................................')
        #except:
        #    from tkinter import messagebox
        #    tkinter.messagebox.showerror('Error', 'Sorry an error occurrred')

    Label(tk, text='Pick month  :', bg='brown', fg='yellow', font=('freesans bold', 12),
          relief='flat', width=30).grid(row=1, column=1)
    Button(tk, text='Submit', bg='grey', fg='black', font=('corier new', 12),
           width=9, relief='groove', command=query_month_data).grid(row=2, column=2)
    Button(tk, text='To printable', bg='grey', fg='white', font=('corier new', 12),
           width=9, relief='groove', command=query_month_data).grid(row=3, column=2)
    month__list = conn.execute('SELECT Month FROM ministry')
    month_list = []
    for i in month__list:
        month_list.append(i[0])
    month_to_query = StringVar(tk)
    month_menu = OptionMenu(tk, month_to_query, *month_list)
    month_menu.configure(width=9, bg='plum', fg='black', font=('times new roman', 12))
    month_menu.grid(row=1, column=2)
    tk.mainloop()




def ex():
    conn.close
    exit()
def display():
    Button(root, text='View all', command=show_all_data, relief='ridge', bg='sky blue', fg='green',
           font=('Courier new', 16), height=3, width=16).place(x=10, y=100)
    Button(root, text='Daily report', command=data_input, relief='ridge', bg='sky blue', fg='blue',
           font=('Courier new', 16), height=3, width=16).place(x=10, y=200)
    Button(root, text='monthly Service report', command=service_report, relief='ridge', bg='sky blue',
           fg='black', font=('Courier new', 16), height=3, width=16).place(x=10, y=300)
    welcome = str('*************** WELCOME ***************')
    Label(root, text=welcome, bg='aqua', relief='ridge', fg="white",
          font=('freesansbold', 18, 'bold'), height=3).place(x=0, y=0)
def submit():
    username = (username_entry.get())
    password = (password_entry.get())
    if (username == 'mikezinyoni') and password == 'jw1914':
        display()
    else:
        from tkinter import messagebox
        messagebox.showerror('Wrong credentials', 'Incorrect login details')
        username_entry.delete(0, END)
        password_entry.delete(0, END)
    


Label(root, text='Username', width=20, bg='grey', fg='blue', font=('times new roman', 12),
      relief='flat').grid(row=0)
Label(root, text='Password', width=20, bg='grey', fg='blue', font=('times new roman', 12),
      relief='flat').grid(row=1)
username_entry = Entry(root, width=15, relief='sunken', bg='steel blue',
                       fg='orange', font=('freesans bold', 11))
username_entry.grid(row=0, column=1)
password_entry = Entry(root, width=15, relief='sunken', bg='steel blue',
                       fg='orange', font=('freesans bold', 11), show='*')
password_entry.grid(row=1, column=1)
Button(root, text='Exit', width=3, height=2, relief='groove', bg='red', fg='white', command=ex,
       font=('algerian', 13)).place(x=365, y=0)
Button(root, text='Submit', width=5, height=2, relief='groove', bg='blue',
       fg='white', command=submit,
       font=('algerian', 13)).place(x=312, y=0)

root.mainloop()

# ###############################################################
# ------------------------------ABOUT THE PROGRAM - -------------#
#    Program name : Ministry Assistant1.0                         ########################
#    Program description : tkinter app for keeping a publishers ministry data            # 
#    mzinyoni7@gmail.com, mzinyoni7@outlook.com, +263 771 588 144, +263 784528370        #
#    Author : MIKE ZINYONI                                       ########################
#    Date : 28 September 2019                                    #
#                                                                #
#    BRICKS COORPORATION ™                                       #
# ###############################################################

''')


quadratic_calculator_help = str('''from tkinter import *
from math import sqrt
root = Tk()
root.title('quadratic roots')
root.minsize(400,600)
root.configure(bg='grey', bd=10)
label = Label(root, text='A', width=10, bg='blue', fg='yellow', relief='flat').grid(row=0)
label = Label(root, text='B', width=10, bg='blue', fg='yellow', relief='flat').grid(row=1)
label = Label(root, text='C', width=10, bg='blue', fg='yellow', relief='flat').grid(row=2)
a_a = Entry(root, width=10, bg='white', fg='black', relief='sunken')
a_a.grid(row=0, column=1)
b_b = Entry(root, width=10, bg='white', fg='black', relief='sunken')
b_b.grid(row=1, column=1)
c_c = Entry(root, width=10, bg='white', fg='black', relief='sunken')
c_c.grid(row=2, column=1)
def calc_root():
    a = int(a_a.get())
    b = int(b_b.get())
    c = int(c_c.get())
    #r1 = (-b + (sqrt((b**2) - 4*a*c)))/(2*a)
    disc = float((b**2) - 4 *( a * c))
    rdisc = float(sqrt(disc))
    pos_num = (-b) + rdisc
    neg_num = (-b) - rdisc
    din = 2 * a
    root_1 = pos_num / din
    root_2 = neg_num / din
    x = 'x'
    if a >= 0:
        s1 = '+'
    else:
        s1 = ''
    if c >= 0:
        s2 = '+'
    else:
        s2 = ''
    equ = (a,'x²',s1,b,'x',s2,c)
    equation = str(equ)
    label = Label(root, text=equation, bg='steel blue', fg='pink', relief='ridge').grid(row=3, column=2)
    label1 = Label(root, text='Root 1', bg='lime', fg='black', width=10).grid(row=4)
    root1_label = Label(root, text=root_1, bg='green', fg='brown', relief='groove').grid(row=5)
    label2 = Label(root, text='Root 2', bg='lime', fg='black', width=10).grid(row=4, column=1)
    root2_label = Label(root, text=root_2, bg='green', fg='brown', relief='groove').grid(row=5, column=1)
button = Button(root, text='Combute', bg='aqua', fg='white', command=calc_root).grid(row=3)
root.mainloop()
''')

simple_pyart_help = str('''a = '*'
x = [a]
while len(x) < 10:
    x.append(a)
    print(x)
while len(x) >0:
    x.remove(a)
    print(x)
''')


factorial_calculator = str('''x = int(input('enter num :'))
y = x
d = y
print(y)
while x > 0:
    y = y*x
    print(x)
    x= x-1
print(y/d)

''')

classes_help = str(''' CLASS CREATION
class Dog:
    
    kind = 'canine'

    def __init__(self, name):
        self.name = name

        
d = Dog('Fido')
e = Dog('Buddy')
print('first dog :', str(d))
print('second dog',  e)
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)



CLASS CALLING
x = int(input('enter num :'))
y = x
d = y
print(y)
while x > 0:
    y = y*x
    print(x)
    x= x-1
print(y/d)
''')

IF_ELSE_condition_help =str('''x = int(input('please      :'))
if x in range(70,101):
    print(x,  'A')
elif x in range(60,70):
    print(x,  'B')
elif x in range(50,60):
    print(x,  'C')
elif x in range(40,50):
    print(x,  'D')
elif x in range(30,40):
    print(x,  'E')
elif x in range(0,30):
    print(x,  'U')
''')

spider_plot_help = str('''# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 02:12:54 2019

@author: MIKE
"""

import matplotlib.pyplot as plt
import math
xli = []
yli = []
i = 0
while i < 12.56:
    xli.append(0)
    yli.append((math.cos(i)))
    i = (i + 0.001)
plt.plot(yli, 'k')
plt.plot(xli, 'k')
''')

sorting_algorithms_help = ('''def simple_sort():
    arr = [5,3,8,6,7,2]
    arr.sort()
    print(arr)
def bubble_sort():
    def sort(nums):
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1]= temp

    nums = [5,3,8,7,2]
    sort(nums)

    print(nums)
pos = -1
def binary_search():
    def search(arr, n):
        l = 0
        u = len(arr)-1

        while l <= u:
            mid = (l+u) // 2
            if arr[mid] == n:
                globals()['pos'] = mid
                return True
            else:
              if arr[mid] < n:
                  l = mid+1
              else:
                  u = mid-1
        return False



    arr = [4,7,8,12,45,99]
    n = 70
    if search(arr, n):
        print('Found at', pos+1)
    else:
        print('Not found')

binary_search()



def linear_search():
    pos = -1
    arr = [5,8,4,6,9,2]
    n = 9
    def search(arr, n):
        i = 0
        while i < len(arr):
            if arr[i] == n:
                globals()['pos'] = i
                return True;
            i = i + 1
        return False
    if search(arr, n):
        print('Found at', pos)
    else:
        print('Not found')
''')


access_database_help = str('''
************DML code to create a Table************

CREATE TABLE tblEmployee(EmpID INT NOT NULL PRIMARY KEY,
Name VARCHAR(10) NOT NULL,
HiredDate DATE,
Salary CURRENCY)

************ DML code to link tables by use of foreign keys ************
CREATE TABLE tblTraining
(EmpID INT NOT NULL,
CourseTitle VARCHAR(30)  NOT NULL,
CourseDate DATE NOT NULL,
PRIMARY KEY (EmpID, CourseDate),
FOREIGN KEY (EmpID) REFERENCES tblEmployee(EmpID))

************ DML code to alter schema of a table ************
ALTER TABLE tblEmployee
ADD Department VARCHAR(10)

************ DML code to create an index ************
CREATE INDEX NameIndex ON tblEmloyee(EmpID)

************ DML code to insert data into table ************
INSERT INTO tblEmployee ( EmpID, Name, HiredDate, Salary, Department )
VALUES ('1122', 'Bloggs', '01/01/2000', '18000', 'Technical');

************DML code to update contents of a table  ************
UPDATE tblEmployee SET Salary = Salary*0.9
where Department='IT';

************DML code to delete contents of a table ************
DELETE *
FROM tblEmployee
WHERE Name = 'Bloggs';

************DML code to select ************
SELECT Name, Salary
FROM tblEmployee;

************SQL code to select ************
SELECT LicenseNo, CustomerID, Package, DateOfPurchase
FROM tblSoftware;

************ SQL code to select from table where condition ************
SELECT LicenseNo, CustomerID, Package, Version
FROM tblSoftware
WHERE Version = "2.0";

************ SQL code to select distinct from table************
SELECT DISTINCT CustomerID, ServiceAgreement
FROM tblSoftware;

************SQL code to selct from table where date between, order by ************
SELECT *
FROM tblSoftware
WHERE DateOfPurchase BETWEEN #01/01/1999# AND #28/02/2000#
ORDER BY CustomerID, Package DESC;

************SQL code groupby sm as example ************
SELECT CustomerID, SUM(Price) AS SumOfPrice
FROM tblSoftware
GROUP BY CustomerID;
************ END OF ACCESS DATABASE HELP ************
''')


def logic_gates_help():
    print('''
    *  NOT gate
    *  X →→→►●→→→ X'
    *  The NOT gate is also called the inverter its function is
    *                        a === a'
    *  It inverts the input. 0 === 1.It only takes one input
    *  its number of inputs is 2¹.
    ******************************************************************
    *   AND gate
    *  a ___
    *  b ___█Ɒ→→→  a.b
    *
    *  The AND gate is also called the multiplier its function is
    *                        (a, b) === a.b
    *  It multiplies the input. (1,1) === 1, (0,0)=== 0, (1,0)===0
    *  The number of outputs is two to the power number of inputs
    ******************************************************************
    *   OR gate
    *       ___
    *  a ---)   )
    *        )OR )→→ a+b
    *  b ---)___)
    *
    *  The OR gate is also called the sigma its function is
    *                        (a, b) === a+b
    *  It adds the input. (1,1) === 1, (0,0)=== 0, (1,0)===1
    *  The number of outputs is two to the power number of outputs
    ******************************************************************
    *   NAND gate
    *  a ___
    *  b ___█Ɒ●→→  (a.b)'
    *
    *  The AND gate states multiply then invert its function is
    *                        (a, b) === (a.b)'
    *  It multiplies the input and the inverts the result.
    *  (1,1) === 0, (0,0)=== 1, (1,0)===1
    *  The number of outputs is two to the power number of inputs
    ******************************************************************
    *   NOR gate
    *        ___
    *  a ---)   )
    *        )OR )●→→ (a+b)'
    *  b ---)___)
    *
    *  The NOR gate states add then invert its function is
    *                        (a, b) === (a+b)'
    *  It adds the input and the inverts the result.
    *  (1,1) === 0, (0,0)=== 1, (1,0)===0
    *  The number of outputs is two to the power number of inputs
    ******************************************************************
    *   Exclusive OR XOR
    *         ___
    *  a ---))   )
    *        ))OR )→→ a.b' + a'.b
    *  b ---))___)
    *
    ******************************************************************
    *   Exclusive NOR XNOR
    *         ___
    *  a ---))   )
    *        ))OR )●→→ a'.b' + a'.b
    *  b ---))___)
    *
    ******************************************************************
    ''')

file_ops = str('''
(file = open('ped.txt', 'w')
file.write('hello i did it \n')
file.write('yes i mean it \n')
file.write('with Jah all is possible \n')
file.close()
''
''
file = open('ped.txt', 'r') # how to open readmode connection
print(file.readline()) #  read single line from top
file.close()
''
''
file = open('ped.txt', 'r') # how to open readmode connection
for line in file.readlines():  #how to read line by line
    print(line)
file.close()
''
''
file = open('ped.txt', 'a') # how to open append connection
file.write('\nOh, yah i am a good programmer')
file.close()
''
''
file = open('ped.txt', 'r')
print(file.readlines()[2])  # read an exactline
file.close
''
''
file = open('ped.txt', 'r')
line_of_text = file.readline()
while len(line_of_text) > 0:
    line_of_text = file.readline()
    print(line_of_text)
file.close())
''')


lists_help = str('''
LISTS
To declare a list you use the statement
xli = [] 
1 xli.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

2 xli.extend(yli/ iterable)
Extend the list by appending all the items from the iterable or list.
Equivalent to xli[len(xli):] = iterable/ list.

3 xli.insert(i,x)
Insert an item at a given position. The first argument is the indexof the
element beforewhich to insert, so xli.insert(0, x) inserts at the front of
the list, and xli.insert(len(xli), x) is equivalent to xli.append(x)

4 xli.remove(x)
Remove the first item from the list whose value is equal to x.
It raises a ValueError if there is no such item.

5 xli.pop([i])
Remove the item at the given position i in the list and return it.If no index is
specified xli.pop() removes the last item in the list.

6 xliclear()
Removes all items from list equivalent to del xli[:]

7xliindex(x[,start[,end]])
Return zero-based index in the list of the first item whose value is equal to x.
Raises a ValueError if there is no such item.

The optional arguements start and end are interpreted as in slice notation
and are used to limit the search in a particular subsequence of the list.
The returned index is computed relative to the full sequence rather than
the start arguement

8 xli.count(x)
Return the number of times x appears in the list.

9 xli.sort(key=none, reverse=False)
Sort the items of the list in place(the arguements can be used for sort
customisation)

10 xli.reverse()
Reverse the elements of the list in place.

11  Nested list comprehensions

The initial expression in a list comprehension can be any arbitrary expression,
including another list comprehension.

they can be used to set up two dimensional arrays and matrices.
to access an element you type in its index as a coordinate ie suppose

xli = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
to access the first list you type xli[0]
to access the digit 8 you type xli[2][1]

12 slicing
Slicing is a method of extracting or cutting out a piece of the overall
list. It takes in the following commands suppose we have list xli

xli=['a', 'b','c','d','e','f','g','h']
xli[2:] returns c to h
xli[:2] returns a,b
xli[-2:] returns g,h
xli[:-2] returns a,b,c,d,e,f
xli[2:5] returns c,d,e

13 list statistics (only applicable if x contains integerial data types)
max(xli) largest item of xli
min(xli) smallest item of xli
len(xli) length of xli
sum(xli) sum of all values in xli


python also has modules like

array, queue and statistics for further implementation of these data structures
''')




