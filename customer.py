from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq
import random as ran
class cus_win():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x550+110+190")
        #===========Variables================
        self.var_ref=StringVar()
        x=ran.randint(1000,10000)
        self.var_ref.set(str(x))

        self.name_var=StringVar()
        self.moth_var=StringVar()
        self.gend_var=StringVar()
        self.code_var=StringVar()
        self.num_var=StringVar()
        self.mail_var=StringVar()
        self.dress_var=StringVar()

        lbltil=Label(self.root,text="ADD CUSTOMER DETAIL",font=("Comic Sans MS",18,"bold"),bg='black',fg='Gold',bd=4,relief=RIDGE)
        lbltil.place(x=0,y=0,width=1150,height=50)
        #=========================================
        lfl=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',font=("Comic Sans MS",12,"bold"),padx=2)
        lfl.place(x=5,y=50,width=425,height=490)
        #=========================================
        cust_ref=Label(lfl,text='Customer Reference: ',font=("Comic Sans MS",12),padx=2,pady=6)
        cust_ref.grid(row=0,column=0)
        cus_ref=ttk.Entry(lfl,width=22,textvariable=self.var_ref,font=("Comic Sans MS",12),state="readonly").grid(row=0,column=1)
        #customer name
        cust_name=Label(lfl,text='Customer Name: ',font=("Comic Sans MS",12),padx=2,pady=6)
        cust_name.grid(row=1,column=0)
        cus_name=ttk.Entry(lfl,width=22,textvariable=self.name_var,font=("Comic Sans MS",12)).grid(row=1,column=1)
        #mother name
        moth_name=Label(lfl,text="Mother's Name: ",font=("Comic Sans MS",12),padx=2,pady=6)
        moth_name.grid(row=2,column=0)
        mot_name=ttk.Entry(lfl,width=22,textvariable=self.moth_var,font=("Comic Sans MS",12)).grid(row=2,column=1)
        #gender combobox
        gender=Label(lfl,text='Gender : ',font=("Comic Sans MS",12),padx=2,pady=6)
        gender.grid(row=3,column=0)
        combogen=ttk.Combobox(lfl,textvariable=self.gend_var,font=("Comic Sans MS",12),width=22,state="readonly")
        combogen['values']=('Male','Female','Others')
        combogen.current(0)
        combogen.grid(row=3,column=1)


        #postcode
        post=Label(lfl,text='Postcode: ',font=("Comic Sans MS",12),padx=2,pady=6)
        post.grid(row=4,column=0)
        code=ttk.Entry(lfl,width=22,textvariable=self.code_var,font=("Comic Sans MS",12)).grid(row=4,column=1)
        #number
        mobile=Label(lfl,text='MObile Number: ',font=("Comic Sans MS",12),padx=2,pady=6).grid(row=5,column=0)
        numb=ttk.Entry(lfl,width=22,textvariable=self.num_var,font=("Comic Sans MS",12)).grid(row=5,column=1)
        #email
        email=Label(lfl,text='Email : ',font=("Comic Sans MS",12),padx=2,pady=6).grid(row=6,column=0)
        mail=ttk.Entry(lfl,width=22,textvariable=self.mail_var,font=("Comic Sans MS",12)).grid(row=6,column=1)
        #address
        ad=Label(lfl,text='Residential Address: ',font=("Comic Sans MS",12),padx=2,pady=6).grid(row=7,column=0)
        adre=ttk.Entry(lfl,width=22,textvariable=self.dress_var,font=("Comic Sans MS",12)).grid(row=7,column=1)
        #===============Buttons====================
        btn_frm=Frame(lfl,bd=2,relief=RIDGE)
        btn_frm.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frm,text='ADD',command=self.add_data,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=0,padx=5)

        btnup=Button(btn_frm,text='Update',command=self.update,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=1,padx=5)

        btndel=Button(btn_frm,text='Delete',command=self.del_data,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=2,padx=5)

        btnres=Button(btn_frm,text='Reset',command=self.resetfu,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=3,padx=5)
        
       #==================================Tableframe===================
        tf=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search System',font=("Comic Sans MS",12,"bold"),padx=2)
        tf.place(x=435,y=50,width=860,height=490)


        ad=Label(tf,text='Search By : ',font=("Comic Sans MS",12),bg='red',fg='white').grid(row=0,column=0)

        self.ser_var=StringVar()

        comboser=ttk.Combobox(tf,textvariable=self.ser_var,font=("Comic Sans MS",12),width=20,state="readonly")
        comboser['values']=('mobile','ref')
        comboser.current(0)
        comboser.grid(row=0,column=1,padx=2)
        self.tex_ser=StringVar()

        serby=ttk.Entry(tf,textvariable=self.tex_ser,width=20,font=("Comic Sans MS",12)).grid(row=0,column=2,padx=2)

        btnser=Button(tf,text='Search',command=self.search,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=3,padx=2)

        btnshwb=Button(tf,text='Show All',command=self.fetch_data,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=4,padx=2)

        #=============showData=====================
        det_frm=Frame(tf,bd=2,relief=RIDGE)
        det_frm.place(x=0,y=50,width=700,height=350)

        scrbrx=ttk.Scrollbar(det_frm,orient=HORIZONTAL)
        scrbry=ttk.Scrollbar(det_frm,orient=VERTICAL)

        self.cust_table=ttk.Treeview(det_frm,column=('ref','Name','mothername','gender','post','mobile','email','adress'),xscrollcommand=scrbrx.set,yscrollcommand=scrbry.set)
        scrbrx.pack(side=BOTTOM,fill=X)
        scrbry.pack(side=RIGHT,fill=Y)

        scrbrx.config(command=self.cust_table.xview)
        scrbry.config(command=self.cust_table.yview)

        self.cust_table.heading('ref',text="Refer.No")
        self.cust_table.heading('Name',text="Name")
        self.cust_table.heading('mothername',text="Mother's Name")
        self.cust_table.heading('gender',text="Gender")
        self.cust_table.heading('post',text="PostCode")
        self.cust_table.heading('mobile',text="Phone Number")
        self.cust_table.heading('email',text="E-mail ID")
        self.cust_table.heading('adress',text="Address")

        self.cust_table['show']="headings"

        self.cust_table.column('ref',width=100)
        self.cust_table.column('Name',width=100)
        self.cust_table.column('mothername',width=100)
        self.cust_table.column('gender',width=100)
        self.cust_table.column('post',width=100)
        self.cust_table.column('mobile',width=100)
        self.cust_table.column('email',width=100)
        self.cust_table.column('adress',width=100)

        
        self.cust_table.pack(fill=BOTH,expand=1)
        self.cust_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if (self.num_var.get()=="" or self.moth_var.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=sq.connect("Hotelmnt.db")
                c=conn.cursor()
                sql="""INSERT INTO customer VALUES(?,?,?,?,?,?,?,?)"""
                c.execute(sql,(self.var_ref.get(),self.name_var.get(),self.moth_var.get(),self.gend_var.get(),int(self.code_var.get()),int(self.num_var.get()),self.mail_var.get(),self.dress_var.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data Entered",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong:{str(es)}",parent=self.root) 
                      
    def fetch_data(self):
        conn=sq.connect("Hotelmnt.db")
        c=conn.cursor()
        c.execute("""SELECT * FROM customer""")
        rows=c.fetchall()
        if len(rows)!=0:
            self.cust_table.delete(*self.cust_table.get_children())
            for i in rows:
                self.cust_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    def get_cursor(self,events=""):
        cursor_row=self.cust_table.focus()
        contents=self.cust_table.item(cursor_row)
        row=contents["values"]
        
        self.var_ref.set(row[0]),
        self.name_var.set(row[1]),
        self.moth_var.set(row[2]),
        self.gend_var.set(row[3]),
        self.code_var.set(row[4]),
        self.num_var.set(row[5]),
        self.mail_var.set(row[6]),
        self.dress_var.set(row[7])

    def update(self):
        if (self.num_var.get()=="" or self.moth_var.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=sq.connect("Hotelmnt.db")
            c=conn.cursor()
            c.execute("UPDATE customer SET Name=(?),mothername=(?),gender=(?),post=(?),mobile=(?),email=(?),adress=(?) WHERE ref=(?)",(self.name_var.get(),self.moth_var.get(),self.gend_var.get(),int(self.code_var.get()),int(self.num_var.get()),self.mail_var.get(),self.dress_var.get(),self.var_ref.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Details Updates Sucessfully",parent=self.root)

    def del_data(self):
        del_data=messagebox.askyesno("HOTEL MANAGEMENT SYSTEM","Do you wanna delete this Customer?",parent=self.root)
        if del_data>0:
            conn=sq.connect("Hotelmnt.db")
            c=conn.cursor()
            sql="DELETE FROM customer WHERE ref = (?)"
            c.execute(sql,(str(self.var_ref.get()),))
        else:
            if not del_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def resetfu(self):
        #self.var_ref.set(""),
        self.name_var.set(""),
        self.moth_var.set(""),
        #self.gend_var.set(""),
        self.code_var.set(""),
        self.num_var.set(""),
        self.mail_var.set(""),
        self.dress_var.set("")
        x=ran.randint(1000,10000)
        self.var_ref.set(str(x))
    def search(self):
        conn=sq.connect("Hotelmnt.db")
        c=conn.cursor()
        c.execute("SELECT * FROM customer WHERE "+str(self.ser_var.get())+"= "+str(self.tex_ser.get()))
        rows=c.fetchall()
        if len(rows)!=0:
            self.cust_table.delete(*self.cust_table.get_children())
            for i in rows:
                self.cust_table.insert("",END,values=i)
            conn.commit()
        conn.close()



            



if __name__=="__main__":
    root=Tk()
    obj=cus_win(root)
    root.mainloop()
    
