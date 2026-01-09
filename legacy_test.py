#project final


import tkinter
from tkinter import *
from tkinter import ttk
import os
import mysql.connector as c


#login and register----------------------------------------------------------------------


def register():
    global register_screen
    register_screen = Toplevel(menu)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen,
    text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen,
    textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen,
    text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen,textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10,
    height=1, command = register_user).pack()

def register_a():
    global register_screen_a
    register_screen_a = Toplevel(menu)
    register_screen_a.title("Register")
    register_screen_a.geometry("300x250")
    global username_a
    global password_a
    global username_entry_a
    global password_entry_a
    username_a = StringVar()
    password_a = StringVar()
    Label(register_screen_a, text="Please enter details below").pack()
    Label(register_screen_a, text="").pack()
    username_lable = Label(register_screen_a,
    text="Username * ")
    username_lable.pack()
    username_entry_a = Entry(register_screen_a,textvariable=username_a)
    username_entry_a.pack()
    password_lable = Label(register_screen_a,
    text="Password * ")
    password_lable.pack()
    password_entry_a = Entry(register_screen_a,textvariable=password_a, show='*')
    password_entry_a.pack()
    Label(register_screen_a, text="").pack()
    Button(register_screen_a, text="Register", width=10,
    height=1, command = register_admin).pack()

def login():
    global login_screen
    login_screen = Toplevel(menu)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen,
    textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen,textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10,height=1, command = login_verify).pack()

def login_admin():
    global login_screen_a
    login_screen_a = Toplevel(menu)
    login_screen_a.title("Login")
    login_screen_a.geometry("300x250")
    Label(login_screen_a, text="Please enter details below to login").pack()
    Label(login_screen_a, text="").pack()
    global username_verify_a
    global password_verify_a
    username_verify_a = StringVar()
    password_verify_a = StringVar()
    global username_login_entry_a
    global password_login_entry_a
    Label(login_screen_a, text="Username * ").pack()
    username_login_entry_a = Entry(login_screen_a,textvariable=username_verify_a)
    username_login_entry_a.pack()
    Label(login_screen_a, text="").pack()
    Label(login_screen_a, text="Password * ").pack()
    password_login_entry_a = Entry(login_screen_a,textvariable=password_verify_a, show= '*')
    password_login_entry_a.pack()
    Label(login_screen_a, text="").pack()
    Button(login_screen_a, text="Login", width=10,height=1, command = login_verify_admin).pack()

def register_user():
    register
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "a")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="Registration Successful!",
    fg="green", font=("calibri", 11)).pack()
    register_screen.after(1500,lambda:register_screen.destroy())

def register_admin():
    username_info_a = username_a.get()
    password_info_a = password_a.get()
    file = open(username_info_a, "a")
    file.write(username_info_a + "\n")
    file.write(password_info_a)
    file.close()
    username_entry_a.delete(0, END)
    password_entry_a.delete(0, END)
    Label(register_screen_a, text="Registration Successful!",
    fg="green", font=("calibri", 11)).pack()
    register_screen_a.after(1500,lambda:register_screen_a.destroy())

def login_verify():
    username = username_verify.get()
    password = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    list_of_files = os.listdir()
    if username in list_of_files:
        file1 = open(username, "r")
        verify = file1.read().splitlines()
        if password in verify:
            login_screen.destroy()
            homepage()
        else:
            password_not_recognised()
    else:
        user_not_found()

def login_verify_admin():
    username_a = username_verify_a.get()
    password_a = password_verify_a.get()
    username_login_entry_a.delete(0, END)
    password_login_entry_a.delete(0, END)
    list_of_files = os.listdir()
    if username_a in list_of_files:
        file1 = open(username_a, "r")
        verify = file1.read().splitlines()
        if password_a in verify:
            homepage_admin()
            login_screen_a.destroy()
        else:
            password_not_recognised_admin()
    else:
        user_not_found_admin()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",command=delete_password_not_recognised).pack()

def password_not_recognised_admin():
    global password_not_recog_screen_admin
    password_not_recog_screen_admin = Toplevel(login_screen_a)
    password_not_recog_screen_admin.title("Success")
    password_not_recog_screen_admin.geometry("150x100")
    Label(password_not_recog_screen_admin, text="Invalid Password ").pack()
    Button(password_not_recog_screen_admin, text="OK",command=delete_password_not_recognised_admin).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def user_not_found_admin():
    global user_not_found_screen_admin
    user_not_found_screen_admin = Toplevel(login_screen_a)
    user_not_found_screen_admin.title("Success")
    user_not_found_screen_admin.geometry("150x100")
    Label(user_not_found_screen_admin, text="User Not Found").pack()
    Button(user_not_found_screen_admin, text="OK",command=delete_user_not_found_screen_admin).pack()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_password_not_recognised_admin():
    password_not_recog_screen_admin.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_user_not_found_screen_admin():
    user_not_found_screen_admin.destroy()


# User tasks -------------------------------------------------------------------------

def gps():
    new_window2 = Toplevel() # Use Toplevel() directly
    new_window2.geometry("1000x900")
    # You need a command here, otherwise this button does nothing
    b4 = Button(new_window2, text="Add Map", command=lambda: print("Map button clicked")) 
    b4.pack()

def c_list():
    new_window3 = Toplevel()
    new_window3.geometry("1000x900")
    
    # FIXED: Added 'command' to these buttons (You need to define the functions view_cl and add_cl)
    b6 = Button(new_window3, text="View contact list", bg='#ADD8E6', height=10, width=40, command=lambda: print("Link to view_cl function"))
    b6.place(x=100, y=60)
    
    b7 = Button(new_window3, text="Add a contact", bg='#ADD8E6', height=10, width=40, command=lambda: print("Link to add_cl function"))
    b7.place(x=100, y=300)
    
    # FIXED: Removed space in table name and added IF NOT EXISTS
    datasql("CREATE TABLE IF NOT EXISTS Contact_List (name varchar(30) not null, contact_no bigint)")

def elist():
    global new_window4
    new_window4 = Toplevel()
    new_window4.geometry("1000x900")
    
    b6 = Button(new_window4, text="VIEW EMERGENCY LIST", command=view_ec, height=10, width=40, bg='#ADD8E6')
    b6.place(x=400, y=0)
    
    be = Button(new_window4, text="ADD EMERGENCY LIST", command=econtact_list, height=10, width=40, bg='#ADD8E6')
    be.place(x=400, y=200)
    
    # FIXED: Removed space in table name "Emergency_List"
    datasql("CREATE TABLE IF NOT EXISTS Emergency_List (name varchar(30) not null, contact_no bigint)")

def view_ec():
    con = c.connect(host='localhost', user='root', passwd='1234', database='MedPlus')
    cursor = con.cursor()
    # FIXED: Added Underscore to table name
    query = "SELECT * FROM Emergency_List"
    
    # Clear previous widgets before showing new ones (optional but recommended)
    for widget in new_window4.winfo_children():
        if isinstance(widget, ttk.Label):
            widget.destroy()

    try:
        cursor.execute(query)
        data = cursor.fetchall()
        
        if not data:
            ttk.Label(new_window4, text="No data found", background="black", foreground="white").pack(side=BOTTOM)
        else:
            for i in data:
                print(i)
                ttk.Label(new_window4, text=f"Name: {i[0]}, Number: {i[1]}").pack(side=BOTTOM)
    except c.Error as err:
        print(f"Error: {err}")
        ttk.Label(new_window4, text="Error fetching data", background="red", foreground="white").pack(side=BOTTOM)
    
    cursor.close()
    con.close()

def econtact_list():
    global name
    global num
    new_window5 = Toplevel()
    new_window5.geometry("1000x900")
    
    bn = Button(new_window5, text="Insert contact name: ", bg='#ADD8E6')
    bn.place(x=200, y=0)
    
    name = Entry(new_window5, width=40, bg='#ADD8E6')
    name.place(x=200, y=100)
    
    bnu = Button(new_window5, text="Insert contact number: ", bg='#ADD8E6')
    bnu.place(x=200, y=200)
    
    num = Entry(new_window5, width=40)
    num.place(x=200, y=300)
    
    bs = Button(new_window5, text="Submit", command=sub, bg='#ADD8E6')
    bs.place(x=200, y=400)

def sub():
    cname = name.get()
    cnum = num.get()
    
    # FIXED: Using parameters (%s) handles the quotes automatically and prevents errors
    query = "INSERT INTO Emergency_List (name, contact_no) VALUES (%s, %s)"
    datasql(query, (cname, cnum))
    
    print(f"Added {cname} to database.") # Confirmation in console

#homepages-------------------------------------------------------------


def homepage():
    new_window1 = tkinter.Toplevel()
    new_window1.geometry("1000x900")
    bg2=PhotoImage(file="pills.png")
    canvas2 = Canvas(new_window1, width = 200,height = 200)
    canvas2.pack(fill = "both", expand = True)
    canvas2.create_image( 0, 0, image = bg2,anchor ="nw")
    b1 = Button(new_window1,text="MAP",height="10",width="40",command=gps, bg='#ADD8E6')
    b1.place(x=400,y=0)
    b2 = Button(new_window1,text="CONTACTS OF HOSPITALS",height=10,width=40,command=c_list, bg='#ADD8E6')
    b2.place(x=400,y=200)
    b3 = Button(new_window1,text="EMERGENCY CONTACTS",height=10,width=40,command=elist, bg='#ADD8E6')
    b3.place(x=400,y=400)
    datasql("CREATE TABLE adminpass (name CHAR(30), id INT(10) PRIMARY KEY NOT NULL, password VARCHAR(20))")

def homepage_admin():
    new_window2 = tkinter.Toplevel()
    new_window2.geometry("1000x900")
    bg2=PhotoImage(file="pills.png")
    canvas2 = Canvas(new_window2, width = 200,height = 200)
    canvas2.pack(fill = "both", expand = True)
    canvas2.create_image( 0, 0, anchor ="nw")
    a1 = Button(new_window2,text="ADD A HOSPITAL ADDRESS",height="10",width="40",command=add_record_hospital, bg='#ADD8E6')
    a1.place(x=200,y=0)
    a2 = Button(new_window2,text="DELETE A HOSPITAL NAME",height=10,command=delete_record_hospital,width=40, bg='#ADD8E6')
    a2.place(x=200,y=200)
    a3 = Button(new_window2,text="MODIFY A HOSPITAL NAME",height=10,command=modify_record_hospital,width=40, bg='#ADD8E6')
    a3.place(x=200,y=400)
    a4 = Button(new_window2,text="ADD A HOSPITAL CONTACT",height="10",width="40",command=add_record_contact, bg='#ADD8E6')
    a4.place(x=600,y=0)
    a5 = Button(new_window2,text="DELETE A HOSPITAL CONTACT",height=10,command=delete_record_contact,width=40, bg='#ADD8E6')
    a5.place(x=600,y=200)
    a6 = Button(new_window2,text="MODIFY A HOSPITAL CONTACT",height=10,command=modify_record_contact,width=40, bg='#ADD8E6')
    a6.place(x=600,y=400)
    a7 = Button(new_window2,text="DELETE A USER",height=7,command=delete_user,width=40, bg='#ADD8E6')
    a7.place(x=400,y=600)

    
#admin tasks------------------------------------------------------------------


def delete_record_hospital():
    new_window6 = tkinter.Toplevel()
    new_window6.geometry("1000x900")
    bg2=PhotoImage(file="pills.png")
    canvas3 = Canvas(new_window6, width = 200,height = 200)
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, anchor ="nw")
    rec = Label(new_window6,text = "Enter Hospital ID to be deleted: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 60)
    hid = Text(new_window6,height=10,width=40).place(x=400,y=60)

def add_record_hospital():
    new_window7 = tkinter.Toplevel()
    new_window7.geometry("1000x900")
    bg2=PhotoImage(file="pills.png")
    canvas3 = Canvas(new_window7, width = 200,height = 200)
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, anchor ="nw")
    rec1 = Label(new_window7,text = "Enter Hospital Name to be added: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 60)
    h_name =  Text(new_window7,height=10,width=40).place(x=400,y=60)
    rec2 = Label(new_window7,text = "Enter Hospital Addres to be added: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 300)
    h_add =  Text(new_window7,height=10,width=40).place(x=400,y=300)

def modify_record_hospital():
    new_window8 = tkinter.Toplevel()
    new_window8.geometry("1000x900")
    bg2=PhotoImage(file="pills.png")
    canvas3 = Canvas(new_window8, width = 200,height = 200)
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, anchor ="nw")
    rec1 = Label(new_window8,text = "Enter Hospital ID to be modified: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 60)
    hid = Text(new_window8,height=10,width=40).place(x=400,y=60)
    rec2 = Label(new_window8,text = "Enter modified name: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 300)
    h_name = Text(new_window8,height=10,width=40).place(x=400,y=300)
    rec3 = Label(new_window8,text = "Enter modified address: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 540)
    h_add = Text(new_window8,height=10,width=40).place(x=400,y=540)

def delete_record_contact():
    new_window9 = tkinter.Toplevel()
    new_window9.geometry("1000x900")
    bg2=PhotoImage(file="pills.png")
    canvas3 = Canvas(new_window9, width = 200,height = 200)
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, anchor ="nw")
    rec = Label(new_window9,text = "Enter Hospital ID to be deleted: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 60)
    hid = Text(new_window9,height=10,width=40).place(x=400,y=60)

def add_record_contact():
    new_window10 = tkinter.Toplevel()
    new_window10.geometry("1000x900")
    bg2=PhotoImage(file="pills.png")
    canvas3 = Canvas(new_window10, width = 200,height = 200)
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, anchor ="nw")
    rec1 = Label(new_window10,text = "Enter Hospital Name to be added: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 60)
    h_name =  Text(new_window10,height=10,width=40).place(x=400,y=60)
    rec2 = Label(new_window10,text = "Enter Hospital contact to be added: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 300)
    h_add =  Text(new_window10,height=10,width=40).place(x=400,y=300)

def modify_record_contact():
    new_window11 = tkinter.Toplevel()
    new_window11.geometry("1000x900")
    bg2=PhotoImage(file="pills.png")
    canvas3 = Canvas(new_window11, width = 200,height = 200)
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, anchor ="nw")
    rec1 = Label(new_window11,text = "Enter Hospital ID to be modified: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 60)
    hid = Text(new_window11,height=10,width=40).place(x=400,y=60)
    rec2 = Label(new_window11,text = "Enter modified contact: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 300)
    h_name = Text(new_window11,height=10,width=40).place(x=400,y=300)

def delete_user():
    new_window12 = tkinter.Toplevel()
    new_window12.geometry("1000x900")
    bg2=PhotoImage(file="pills.png")
    canvas3 = Canvas(new_window12, width = 200,height = 200)
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, anchor ="nw")
    rec1 = Label(new_window12,text = "Enter User ID to be deleted: ",bg='#ADD8E6',height=10,width=40).place(x = 100,y = 60)
    hid = Text(new_window12,height=10,width=40).place(x=400,y=60)


#---------------------------------------------------------------
 
def admin():
    datasql("create table Admins (username varchar(30) not null,password varchar(30)")

def menu():
    global menu
    menu = Tk()
    menu.title('Med plus')
    menu.geometry("1000x1000")
    bg=PhotoImage(file="image0.png")
    canvas1 = Canvas( menu, width = 200,height = 200)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg,anchor ="nw")
    bu1=Button(menu,text="Login(User)", height="2", width="30", command = login,bg='#ADD8E6')
    bu1.place(x=150,y=50)
    bu2=Button(menu,text="Register(User)", height="2", width="30", command=register,bg='#ADD8E6')
    bu2.place(x=450,y=50)
    bu3=Button(menu,text="Login(Admin)", height="2", width="30", command = login_admin,bg='#ADD8E6')
    bu3.place(x=150,y=200)
    bu4=Button(menu,text="Register(Admin)", height="2", width="30", command=register_a,bg='#ADD8E6')
    bu4.place(x=450,y=200)
    menu.mainloop()


#sql-------------------------------------------------------------------------------------


def datasql(query):
    con = c.connect(host='localhost', user='root', passwd='1234', database='MedPlus')
    cursor = con.cursor()
    try:
        cursor.execute(query)
        con.commit()
    except:
        con.rollback()
    cursor.close()
    con.close()



menu()
