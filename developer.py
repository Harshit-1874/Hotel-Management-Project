from time import strftime
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq
import random as ran

class profile():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("400x300+190+190")
        #========================
        lfl=LabelFrame(self.root,bd=2,relief=RIDGE,text='Developer Details',font=("Comic Sans MS",12,"bold"),padx=2,bg="cyan")
        lfl.place(x=5,y=5,width=390,height=290)
        #========================
        flr=Label(lfl,text='Name : Harshit Aggarwal ',font=("Comic Sans MS",12),padx=2,pady=0,bg="cyan")
        flr.grid(row=0,column=0,sticky="w")
        #=========================
        flr=Label(lfl,text='Age : 17 ',font=("Comic Sans MS",12),padx=2,pady=0,bg="cyan")
        flr.grid(row=1,column=0,sticky="w")
        #========================
        flr=Label(lfl,text='E-mail : haggarwal505@gmail.com ',font=("Comic Sans MS",12),padx=2,pady=0,bg="cyan")
        flr.grid(row=2,column=0,sticky="w")
        #======================================
        flr=Label(lfl,text="Contact : 7973539086 ",font=("Comic Sans MS",12),padx=2,pady=0,bg="cyan")
        flr.grid(row=3,column=0,sticky="w")
        #==========================
        



if __name__=="__main__":
    root=Tk()
    obj=profile(root)
    root.mainloop()


