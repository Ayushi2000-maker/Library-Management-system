from tkinter import *
import os
import tkinter.messagebox
import database
root=Tk()
root.title("my library management")
root.configure(bg='black')
root.geometry("400x550+200+200")
def get_row(event):
    pass
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    
def register_user():
    user_entry1=user_entry.get()
    password_entry1=password_entry.get()
    file=open(user_entry1,'w')
    file.write(user_entry1+'\n')
    file.write(password_entry1)
    file.close()
    user_entry.delete(0,END)
    password_entry.delete(0,END)
    Label(register_screen,text='registration sucessfully done',bg='black',fg='red').grid()
    
def color(event):
    listing['bg']='white'
def change(event):
    listing['bg']='pink'
def view_command():
    listing.delete(0,END)
    for row in database.view():
        listing.insert(END,row)
def add_command():
    database.insert(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    listing.delete(0,END)
    listing.insert(END,(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get()))
    clear()
def search_command():
    listing.delete(0,END)
    for row in database.search(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get()):
        listing.insert(END,row)
def update_command():
    database.update(select_tuple[0],title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
def delete_command():
    database.delete(select_tuple[0])
    clear()

def pink1(event):
    e1['bg']='pink'
def pink2(event):
    e2['bg']='pink'
def pink3(event):
    e3['bg']='pink'
def pink4(event):
    e4['bg']='pink'
def powderblue1(event):
    e1['bg']='powderblue'
def powderblue2(event):
    e2['bg']='powderblue'
def powderblue3(event):
    e3['bg']='powderblue'
def powderblue4(event):
    e4['bg']='powderblue'

def h():
    global listing
    window=Toplevel(login_screen)
    window.configure(bg='black')
    global e1,e2,e3,e4
    global title_entry
    global author_entry
    global year_entry
    global isbn_entry
    l1=Label(window,text='Title',bg='powder blue',fg='black',width=20,height=2)
    l1.grid(row=0,column=0,sticky='nswe',padx=5,pady=5)
    title_entry=StringVar()
    e1=Entry(window,bg='powder blue',textvariable=title_entry)
    e1.bind('<Enter>',pink1)
    e1.bind('<Leave>',powderblue1)
    e1.grid(row=0,column=1,sticky='nswe',padx=5,pady=5)
    l2=Label(window,text='author',bg='powder blue',fg='black',width=20,height=2)
    l2.grid(row=0,column=2,sticky='nswe',padx=5,pady=5)
    author_entry=StringVar()
    e2=Entry(window,bg='powder blue',textvariable=author_entry)
    e2.grid(row=0,column=3,sticky='nswe',padx=5,pady=5)
    e2.bind('<Enter>',pink2)
    e2.bind('<Leave>',powderblue2)
    l3=Label(window,text='Year',bg='powder blue',fg='black',width=20,height=2)
    l3.grid(row=1,column=0,sticky='nswe',padx=5,pady=5)
    year_entry=StringVar()
    e3=Entry(window,bg='powder blue',textvariable=year_entry)
    e3.bind('<Enter>',pink3)
    e3.bind('<Leave>',powderblue3)
    e3.grid(row=1,column=1,sticky='nswe',padx=5,pady=5)
    l4=Label(window,text='ISBN',bg='powder blue',fg='black',width=20,height=2)
    l4.grid(row=1,column=2,sticky='nswe',padx=5,pady=5)
    isbn_entry=StringVar()
    e4=Entry(window,bg='powder blue',textvariable=isbn_entry)
    e4.bind('<Enter>',pink4)
    e4.bind('<Leave>',powderblue4)
    e4.grid(row=1,column=3,sticky='nswe',padx=5,pady=5)    
    b1=Button(window,text='View all',bg='powder blue',fg='black',width=70,height=5,command=view_command)
    b1.grid(row=2,column=3,sticky='nswe',padx=5,pady=5)
    b3=Button(window,text='search entry',bg='powder blue',fg='black',width=70,height=5,command=search_command)
    b3.grid(row=3,column=3,sticky='nswe',padx=5,pady=5)
    b4=Button(window,text='add entry',bg='powder blue',fg='black',width=70,height=5,command=add_command)
    b4.grid(row=4,column=3,sticky='nswe',padx=5,pady=5)
    b5=Button(window,text='update selected',bg='powder blue',fg='black',width=70,height=5,command=update_command)
    b5.grid(row=5,column=3,sticky='nswe',padx=5,pady=5)
    b6=Button(window,text='delete selected',bg='powder blue',fg='black',width=70,height=5,command=delete_command)
    b6.grid(row=6,column=3,sticky='nswe',padx=5,pady=5)
    b7=Button(window,text='close',bg='powder blue',fg='black',width=70,height=5,command=window.destroy)
    b7.grid(row=7,column=3,sticky='nswe',padx=5,pady=5)
    img=PhotoImage(file='E:\\images\\book2.png')
    l5=Label(window,image=img,bg='pink')
    l5.grid(row=2,columnspan=3,rowspan=6,sticky='nswe',padx=5,pady=5)
    listing = Listbox(window,bg='pink')
    listing.grid(row = 2, column = 0, padx=5,pady=5,columnspan = 3,sticky='nswe')
    listing.bind('<Enter>',color)
    listing.bind('<Leave>',change)
    listing.bind('<<ListboxSelect>>',get_row)
    for i in range(8):
        window.grid_rowconfigure(i,weight=1)
    for i in range(4):
        window.grid_columnconfigure(i,weight=1)
    # Keep window open until closed.
    window.mainloop()
def g():
    global register_screen
    register_screen=Toplevel(root)
    global user_entry
    global password_entry
    register_screen.title("register information")
    register_screen.configure(bg='black',width=130,height=120,relief=RAISED)
    l1=Label(register_screen,text='Please enter details below ',bg='black',fg='red',relief=RAISED,font='Calibri 23 bold',width=30,bd=4)
    l1.grid(row=0)
    l2=Label(register_screen,text='Username',bg='black',fg='white')
    user_entry=Entry(register_screen,textvariable=txt)
    user_entry.grid(row=2)
    l2.grid(row=1)
    l2=Label(register_screen,text='Password',bg='black',fg='white')
    password_entry=Entry(register_screen,textvariable=txt1,show='*')
    password_entry.grid(row=4)
    l2.grid(row=3)
    button4=Button(register_screen,text='register',bg='black',fg='red',command=register_user)
    button4.grid(row=5)
    register_screen.mainloop()
def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    username_info.delete(0,END)
    password_info.delete(0,END)
    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            button4=Button(login_screen,text='login done successfully',bg='black',fg='red',command=login_verify,width=10)
            button4.grid(row=6,sticky='nswe')
            h()
        else:
            password_not_found()
    else:
        user_not_recognised()
        
def password_not_found():
    tkinter.messagebox.showinfo('wrong password','enter right password')
    login_screen.destroy()
def user_not_recognised():
    tkinter.messagebox.showinfo('wrong user name','enter correct name')
    login_screen.destroy()
def f():
    global username_verify
    global password_verify
    username_verify=StringVar()
    password_verify=StringVar()
    global username_info
    global password_info
    global login_screen
    login_screen=Toplevel(root)
    login_screen.title("login details")
    l1=Label(login_screen,text='Please enter Login Details ',bg='black',fg='red',relief=RAISED,font='Calibri 20 bold')
    l1.grid(row=0,sticky='nswe')
    Label(login_screen,text='Username',bg='black',fg='white',width=10).grid(row=1,sticky='nswe')
    username_info=Entry(login_screen,textvariable=username_verify)
    username_info.grid(row=2,sticky='nswe')
    l2=Label(login_screen,text='password',bg='black',fg='white',width=10)
    password_info=Entry(login_screen,textvariable=password_verify,show='*')
    password_info.grid(row=4,sticky='nswe')
    l2.grid(row=3,sticky='nswe')
    button3=Button(login_screen,text='login',bg='black',fg='white',command=login_verify,width=10)
    button3.grid(row=5,sticky='nswe')
    
    login_screen.mainloop()
def main_screen():
    img=PhotoImage(file='E:\\images\\book.png')
    l=Label(root,image=img,bg='black')
    l.grid(sticky='nswe')
    
    l1=Label(root,text='Welcome to the library',fg='white',bg='black',font='calibri 35 bold',width=20,height=2)
    l1.grid(sticky='',row=0,padx=5,pady=5)
    Label(l,text='Do You Want to ?',height=2,bg='black',fg='white', font='Roboto 15 italic').grid(sticky='nswe',row=1)
    root.grid_rowconfigure(0,weight=1)
    root.grid_columnconfigure(0,weight=1)
    button1=Button(l,text='login',bg='grey',fg='black',font='arial 15 bold',width=15,height=2,command=f)
    button1.grid(sticky='nswe',row=4,padx=5,pady=5)
    button2=Button(l,text='register',bg='grey',fg='black',font='arial 15 bold',width=10,height=2,command=g)
    button2.grid(sticky='nswe',row=5,padx=5,pady=5)
    root.mainloop()
txt=StringVar()
txt1=StringVar()
main_screen()
