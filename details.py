from time import strftime
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq
import random as ran

class det_win():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x550+110+190")
        #============================
        lbltil=Label(self.root,text="HOTEL AND ROOM DETAILS",font=("Comic Sans MS",18,"bold"),bg='black',fg='Gold',bd=4,relief=RIDGE)
        lbltil.place(x=0,y=0,width=1150,height=50)
        #===========================================
        lfl=LabelFrame(self.root,bd=2,relief=RIDGE,text='Add New Room',font=("Comic Sans MS",12,"bold"),padx=2)
        lfl.place(x=5,y=50,width=520,height=350)
#floor====================
        flr=Label(lfl,text='Floor: ',font=("Comic Sans MS",12),padx=2,pady=6)
        flr.grid(row=0,column=0)
        self.var_flr=StringVar()
        fl=ttk.Entry(lfl,width=15,textvariable=self.var_flr,font=("Comic Sans MS",12)).grid(row=0,column=1,sticky="w")
#room number==============
        flr=Label(lfl,text='Room Number: ',font=("Comic Sans MS",12),padx=2,pady=6)
        flr.grid(row=1,column=0)
        self.var_no=StringVar()
        fl=ttk.Entry(lfl,width=15,textvariable=self.var_no,font=("Comic Sans MS",12)).grid(row=1,column=1,sticky="w")
#room type===================
        flr=Label(lfl,text='Room Type : ',font=("Comic Sans MS",12),padx=2,pady=6)
        flr.grid(row=2,column=0)
        self.var_type=StringVar()
        comborom=ttk.Combobox(lfl,font=("Comic Sans MS",12),textvariable=self.var_type,state="readonly")
        comborom['values']=("Single","Double","Luxury")
        comborom.current(0)
        comborom.grid(row=2,column=1)
#buttons=======================
        btn_frm=Frame(lfl,bd=2,relief=RIDGE)
        btn_frm.place(x=0,y=250,width=412,height=40)

        btnadd=Button(btn_frm,text='ADD',command=self.add_data,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=0,padx=5)

        btnup=Button(btn_frm,text='Update',command=self.update,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=1,padx=5)

        btndel=Button(btn_frm,text='Delete',command=self.del_data,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=2,padx=5)

        btnres=Button(btn_frm,text='Reset',command=self.resetfu,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=3,padx=5)
#Table frame======================
        tf=LabelFrame(self.root,bd=2,relief=RIDGE,text='Show Room Details',font=("Comic Sans MS",12,"bold"),padx=2)
        tf.place(x=530,y=55,width=600,height=350)

        scrbrx=ttk.Scrollbar(tf,orient=HORIZONTAL)
        scrbry=ttk.Scrollbar(tf,orient=VERTICAL)

        self.room_table=ttk.Treeview(tf,column=('floor','roomno','roomtype'),xscrollcommand=scrbrx.set,yscrollcommand=scrbry.set)
        scrbrx.pack(side=BOTTOM,fill=X)
        scrbry.pack(side=RIGHT,fill=Y)

        scrbrx.config(command=self.room_table.xview)
        scrbry.config(command=self.room_table.yview)

        self.room_table.heading('floor',text="Floor")
        self.room_table.heading('roomno',text="Room No.")
        self.room_table.heading('roomtype',text="Room Type")
        
        self.room_table['show']="headings"

        self.room_table.column('floor',width=100)
        self.room_table.column('roomno',width=100)
        self.room_table.column('roomtype',width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

#add_data===========================
    def add_data(self):
       if (self.var_flr.get()=="" or self.var_type.get()==""):
        messagebox.showerror("Error","All fields are required",parent=self.root)
       else:
          try:
            conn=sq.connect("Hotelmnt.db")
            c=conn.cursor()
            sql="""INSERT INTO details VALUES(?,?,?)"""
            c.execute(sql,(self.var_flr.get(),self.var_no.get(),self.var_type.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","NEW ROOM ADDED SUCCESSFULLY",parent=self.root)
          except:
            messagebox.showwarning("Warning","Something went wrong:{str(es)}",parent=self.root)
#fetch data=========================
    def fetch_data(self):
        conn=sq.connect("Hotelmnt.db")
        c=conn.cursor()
        c.execute("""SELECT * FROM details""")
        rows=c.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close()
#get cursor=================
    def get_cursor(self,events=""):
        cursor_row=self.room_table.focus()
        contents=self.room_table.item(cursor_row)
        row=contents["values"]
        
        self.var_flr.set(row[0]),
        self.var_no.set(row[1]),
        self.var_type.set(row[2])
#update=========================
    def update(self):
        if (self.var_flr.get()=="" or self.var_type.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=sq.connect("Hotelmnt.db")
            c=conn.cursor()
            c.execute("UPDATE details SET Floor=(?),Type=(?) WHERE Roomno=(?)",(self.var_flr.get(),self.var_type.get(),self.var_no.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Room Details Updated Sucessfully",parent=self.root)
#delete===========================
    def del_data(self):
        del_data=messagebox.askyesno("HOTEL MANAGEMENT SYSTEM","Do you wanna delete this Room Detail?",parent=self.root)
        if del_data>0:
            conn=sq.connect("Hotelmnt.db")
            c=conn.cursor()
            sql="DELETE FROM details WHERE Roomno = (?)"
            c.execute(sql,(str(self.var_no.get()),))
        else:
            if not del_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
#reset func==========================
    def resetfu(self):
        self.var_no.set(""),
        self.var_flr.set(""),
        self.var_type.set("")

if __name__=="__main__":
    root=Tk()
    obj=det_win(root)
    root.mainloop()


