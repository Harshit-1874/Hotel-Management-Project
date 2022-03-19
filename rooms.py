from time import strftime
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq
import random as ran

class rom_win():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x550+110+190")
        #variables==============================
        self.var_con=StringVar()
        self.var_in=StringVar()
        self.var_out=StringVar()
        self.var_type=StringVar()
        self.var_no=StringVar()
        self.var_meal=StringVar()
        self.var_nod=StringVar()
        self.var_tax=StringVar()
        self.var_sub=StringVar()
        self.var_tot=StringVar()
        #==========================================
        lbltil=Label(self.root,text="ROOM BOOKING",font=("Comic Sans MS",18,"bold"),bg='black',fg='Gold',bd=4,relief=RIDGE)
        lbltil.place(x=0,y=0,width=1150,height=50)
        #===========================================
        lfl=LabelFrame(self.root,bd=2,relief=RIDGE,text='RoomBooking Details',font=("Comic Sans MS",12,"bold"),padx=2)
        lfl.place(x=5,y=50,width=425,height=490)
        #contact
        cust_con=Label(lfl,text='Customer Contact: ',font=("Comic Sans MS",12),padx=2,pady=6)
        cust_con.grid(row=0,column=0)
        cus_con=ttk.Entry(lfl,width=15,textvariable=self.var_con,font=("Comic Sans MS",12)).grid(row=0,column=1,sticky="w")
        #fetch data Button======================
        btnfetch=Button(lfl,command=self.fetch_con,text='Fetch_Data',font=("Comic Sans MS",10),bg='black',fg='gold',width=8)
        btnfetch.place(x=310,y=2)
        #Check_in
        cust_in=Label(lfl,text='Check_in Date: ',font=("Comic Sans MS",12),padx=2,pady=6)
        cust_in.grid(row=1,column=0)
        cus_in=ttk.Entry(lfl,width=22,textvariable=self.var_in,font=("Comic Sans MS",12)).grid(row=1,column=1)
        #Check_out
        cust_out=Label(lfl,text="Check_out Date: ",font=("Comic Sans MS",12),padx=2,pady=6)
        cust_out.grid(row=2,column=0)
        cus_out=ttk.Entry(lfl,width=22,textvariable=self.var_out,font=("Comic Sans MS",12)).grid(row=2,column=1)
       #room combobox
        room=Label(lfl,text='Room Type : ',font=("Comic Sans MS",12),padx=2,pady=6)
        room.grid(row=3,column=0)
        #=============================
        comborom=ttk.Combobox(lfl,font=("Comic Sans MS",12),textvariable=self.var_type,width=12,state="readonly")
        comborom['values']=("Single","Double","Luxury")
        comborom.current(0)
        comborom.grid(row=3,column=1,sticky="w")
        #get room data======================
        btnfetch=Button(lfl,text='Get Rooms',command=self.get_room,font=("Comic Sans MS",10),bg='black',fg='gold',width=8)
        btnfetch.place(x=310,y=120)    
        #room_available
        avai=Label(lfl,text='Available Room: ',font=("Comic Sans MS",12),padx=2,pady=6)
        avai.grid(row=4,column=0)
        #===================
        #conn=sq.connect("Hotelmnt.db")
        #c=conn.cursor()
        #q="""SELECT Roomno FROM  details WHERE Type = (?)"""
        #c.execute(q,(self.var_type.get(),))
        #rows=c.fetchall()
        #rows=tuple(rows)
        #====================
        #comboro=ttk.Combobox(lfl,font=("Comic Sans MS",12),textvariable=self.var_no,width=22,state="readonly")
        #comboro["values"]=rows
        #comboro.current(0)
        #comboro.grid(row=4,column=1)
        #avroom=ttk.Entry(lfl,width=22,textvariable=self.var_no,font=("Comic Sans MS",12)).grid(row=4,column=1)
        #meal
        meals=Label(lfl,text='Meals : ',font=("Comic Sans MS",12),padx=2,pady=6).grid(row=5,column=0)
        meal=ttk.Entry(lfl,width=22,textvariable=self.var_meal,font=("Comic Sans MS",12)).grid(row=5,column=1)
        #days
        days=Label(lfl,text='No. Of Days : ',font=("Comic Sans MS",12),padx=2,pady=6).grid(row=6,column=0)
        day=ttk.Entry(lfl,width=22,textvariable=self.var_nod,font=("Comic Sans MS",12)).grid(row=6,column=1)
        #PaidTax
        paid=Label(lfl,text='Taxes Paid: ',font=("Comic Sans MS",12),padx=2,pady=6).grid(row=7,column=0)
        tax=ttk.Entry(lfl,width=22,textvariable=self.var_tax,font=("Comic Sans MS",12)).grid(row=7,column=1)
        #Sub_Tot
        subto=Label(lfl,text='Sub Total: ',font=("Comic Sans MS",12),padx=2,pady=6).grid(row=8,column=0)
        subtot=ttk.Entry(lfl,width=22,textvariable=self.var_sub,font=("Comic Sans MS",12)).grid(row=8,column=1)
        #address
        Total=Label(lfl,text='Total : ',font=("Comic Sans MS",12),padx=2,pady=6).grid(row=9,column=0)
        tota=ttk.Entry(lfl,width=22,textvariable=self.var_tot,font=("Comic Sans MS",12)).grid(row=9,column=1)
        #BillButton====================================
        btnbill=Button(lfl,text='BILL',command=self.total,font=("Comic Sans MS",8),bg='black',fg='gold',width=8).grid(row=10,column=0,padx=5,sticky="w")

        #Buttons========================================
        
        btn_frm=Frame(lfl,bd=2,relief=RIDGE)
        btn_frm.place(x=0,y=420,width=412,height=40)

        btnadd=Button(btn_frm,text='ADD',command=self.add_data,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=0,padx=5)

        btnup=Button(btn_frm,text='Update',font=("Comic Sans MS",12),bg='black',fg='gold',width=8,command=self.update).grid(row=0,column=1,padx=5)

        btndel=Button(btn_frm,command=self.del_data,text='Delete',font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=2,padx=5)

        btnres=Button(btn_frm,command=self.resetfu,text='Reset',font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=3,padx=5)
        #Tableframe===================
        tf=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search System',font=("Comic Sans MS",12,"bold"),padx=2)
        tf.place(x=435,y=280,width=860,height=250)

        ad=Label(tf,text='Search By : ',font=("Comic Sans MS",12),bg='red',fg='white').grid(row=0,column=0)
        self.ser_var=StringVar()

        comboser=ttk.Combobox(tf,textvariable=self.ser_var,font=("Comic Sans MS",12),width=20,state="readonly")
        comboser['values']=('Contact','room_no')
        comboser.current(0)
        comboser.grid(row=0,column=1,padx=2)
        self.tex_ser=StringVar()

        serby=ttk.Entry(tf,textvariable=self.tex_ser,width=20,font=("Comic Sans MS",12)).grid(row=0,column=2,padx=2)

        btnser=Button(tf,text='Search',command=self.search,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=3,padx=2)

        btnshwb=Button(tf,text='Show All',command=self.fetch_data,font=("Comic Sans MS",12),bg='black',fg='gold',width=8).grid(row=0,column=4,padx=2)
        #==================Show Data Table=========================
        det_frm=Frame(tf,bd=2,relief=RIDGE)
        det_frm.place(x=0,y=50,width=700,height=175)

        scrbrx=ttk.Scrollbar(det_frm,orient=HORIZONTAL)
        scrbry=ttk.Scrollbar(det_frm,orient=VERTICAL)

        self.room_table=ttk.Treeview(det_frm,column=('contact','indate','outdate','roomtype','available','meal','noofdays'),xscrollcommand=scrbrx.set,yscrollcommand=scrbry.set)
        scrbrx.pack(side=BOTTOM,fill=X)
        scrbry.pack(side=RIGHT,fill=Y)

        scrbrx.config(command=self.room_table.xview)
        scrbry.config(command=self.room_table.yview)

        self.room_table.heading('contact',text="Contact")
        self.room_table.heading('indate',text="Check-in")
        self.room_table.heading('outdate',text="Check-out")
        self.room_table.heading('roomtype',text="Room-Type")
        self.room_table.heading('available',text="Room-No")
        self.room_table.heading('meal',text="Meals")
        self.room_table.heading('noofdays',text="No_of_Days")
        

        self.room_table['show']="headings"

        self.room_table.column('contact',width=100)
        self.room_table.column('indate',width=100)
        self.room_table.column('outdate',width=100)
        self.room_table.column('roomtype',width=100)
        self.room_table.column('available',width=100)
        self.room_table.column('meal',width=100)
        self.room_table.column('noofdays',width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
#======================add button function
    def add_data(self):
        if (self.var_con.get()=="" or self.var_in.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=sq.connect("Hotelmnt.db")
                c=conn.cursor()
                sql="""INSERT INTO room VALUES(?,?,?,?,?,?,?)"""
                c.execute(sql,(self.var_con.get(),self.var_in.get(),self.var_out.get(),self.var_type.get(),self.var_no.get(),self.var_meal.get(),self.var_nod.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","ROOM ALOTTED",parent=self.root)
            except:
                messagebox.showwarning("Warning","Something went wrong:{str(es)}",parent=self.root)
#fetch to table=========================
    def fetch_data(self):
        conn=sq.connect("Hotelmnt.db")
        c=conn.cursor()
        c.execute("""SELECT * FROM room""")
        rows=c.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close()
#GET CURSOR==================================
    def get_cursor(self,events=""):
        cursor_row=self.room_table.focus()
        contents=self.room_table.item(cursor_row)
        row=contents["values"]
        
        self.var_con.set(row[0]),
        self.var_in.set(row[1]),
        self.var_out.set(row[2]),
        self.var_type.set(row[3]),
        self.var_no.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_nod.set(row[6])
#Update Button===================================
    def update(self):
        if (self.var_con.get()=="" or self.var_in.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=sq.connect("Hotelmnt.db")
            c=conn.cursor()
            c.execute("UPDATE room SET check_in=(?),check_out=(?),room_type=(?),room_no=(?),meal=(?),noofdays=(?) WHERE Contact=(?)",(self.var_in.get(),self.var_out.get(),self.var_type.get(),self.var_no.get(),self.var_meal.get(),self.var_nod.get(),self.var_con.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Room Details Updated Sucessfully",parent=self.root)

#delete button===========================
    def del_data(self):
        del_data=messagebox.askyesno("HOTEL MANAGEMENT SYSTEM","Do you wanna delete this Room Detail?",parent=self.root)
        if del_data>0:
            conn=sq.connect("Hotelmnt.db")
            c=conn.cursor()
            sql="DELETE FROM room WHERE Contact = (?)"
            c.execute(sql,(str(self.var_con.get()),))
        else:
            if not del_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
#reset button===============================
    def resetfu(self):
        self.var_con.set(""),
        self.var_in.set(""),
        self.var_out.set(""),
        self.var_no.set(""),
        self.var_meal.set(""),
        self.var_nod.set(""),
        self.var_tax.set(""),
        self.var_sub.set(""),
        self.var_tot.set("")
    def get_room(self):
        conn=sq.connect("Hotelmnt.db")
        c=conn.cursor()
        q="""SELECT Roomno FROM  details WHERE Type = (?)"""
        c.execute(q,(self.var_type.get(),))
        rows=c.fetchall()
        rows=tuple(rows)
        #====================
        comboro=ttk.Combobox(self.root,font=("Comic Sans MS",12),textvariable=self.var_no,width=22,state="readonly")
        comboro["values"]=rows
        comboro.current(0)
        comboro.place(x=150,y=235)
        
#all data fetch====================================================
    def fetch_con(self):
        if self.var_con.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=sq.connect("Hotelmnt.db")
            c=conn.cursor()
            q=("SELECT Name FROM customer WHERE mobile = (?)")
            v=(self.var_con.get(),)
            c.execute(q,v)
            row=c.fetchone()
            if row==None:
                messagebox.showerror("Error","This number is not registered",parent=self.root)
            else:
                conn.commit()
                conn.close()

                sdf=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                sdf.place(x=455,y=55,width=300,height=180)
                
                lblnm=Label(sdf,text="Name : ",font=("Comic Sans MS",12,"italic"),bd=4)
                lblnm.place(x=0,y=0)
                lbln=Label(sdf,text=row,font=("Comic Sans MS",12,"italic"))
                lbln.place(x=90,y=0)
#gender===================================
                conn=sq.connect("Hotelmnt.db")
                c=conn.cursor()
                q=("SELECT gender FROM customer WHERE mobile = (?)")
                v=(self.var_con.get(),)
                c.execute(q,v)
                row=c.fetchone()

                lblnm=Label(sdf,text="Gender : ",font=("Comic Sans MS",12,"italic"),bd=4)
                lblnm.place(x=0,y=30)
                lbln=Label(sdf,text=row,font=("Comic Sans MS",12,"italic"))
                lbln.place(x=90,y=30)
#email=========================================
                conn=sq.connect("Hotelmnt.db")
                c=conn.cursor()
                q=("SELECT email FROM customer WHERE mobile = (?)")
                v=(self.var_con.get(),)
                c.execute(q,v)
                row=c.fetchone()

                lblnm=Label(sdf,text="Email : ",font=("Comic Sans MS",12,"italic"),bd=4)
                lblnm.place(x=0,y=60)
                lbln=Label(sdf,text=row,font=("Comic Sans MS",12,"italic"))
                lbln.place(x=90,y=60)
#adress===========================================
                conn=sq.connect("Hotelmnt.db")
                c=conn.cursor()
                q=("SELECT adress FROM customer WHERE mobile = (?)")
                v=(self.var_con.get(),)
                c.execute(q,v)
                row=c.fetchone()

                lblnm=Label(sdf,text="Address : ",font=("Comic Sans MS",12,"italic"),bd=4)
                lblnm.place(x=0,y=90)
                lbln=Label(sdf,text=row,font=("Comic Sans MS",12,"italic"))
                lbln.place(x=90,y=90)
#refno==================================================
                conn=sq.connect("Hotelmnt.db")
                c=conn.cursor()
                q=("SELECT ref FROM customer WHERE mobile = (?)")
                v=(self.var_con.get(),)
                c.execute(q,v)
                row=c.fetchone()

                lblnm=Label(sdf,text="Reference : ",font=("Comic Sans MS",12,"italic"),bd=4)
                lblnm.place(x=0,y=120)
                lbln=Label(sdf,text=row,font=("Comic Sans MS",12,"italic"))
                lbln.place(x=90,y=120)
    def total(self):
        indate=self.var_in.get()
        outdate=self.var_out.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        self.var_nod.set(abs(outdate-indate).days)
        if(self.var_meal.get()=="breakfast"or"Breakfast" and self.var_type.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_nod.get())
            q4=float((q1+q2)*q3)
            tax="Rs. "+str("%.2f"%(q4*0.05))
            ST="Rs. "+str("%.2f"%(q4))
            TT="Rs. "+str("%.2f"%((q4)+(q4*0.05)))
            self.var_tax.set(tax)
            self.var_sub.set(ST)
            self.var_tot.set(TT)
        elif(self.var_meal.get()=="lunch"or"Lunch" and self.var_type.get()=="Luxury"):
            q1=float(400)
            q2=float(700)
            q3=float(self.var_nod.get())
            q4=float((q1+q2)*q3)
            tax="Rs. "+str("%.2f"%(q4*0.05))
            ST="Rs. "+str("%.2f"%(q4))
            TT="Rs. "+str("%.2f"%((q4)+(q4*0.05)))
            self.var_tax.set(tax)
            self.var_sub.set(ST)
            self.var_tot.set(TT)
        elif(self.var_meal.get()=="dinner"or"Dinner" and self.var_type.get()=="Luxury"):
            q1=float(350)
            q2=float(700)
            q3=float(self.var_nod.get())
            q4=float((q1+q2)*q3)
            tax="Rs. "+str("%.2f"%(q4*0.05))
            ST="Rs. "+str("%.2f"%(q4))
            TT="Rs. "+str("%.2f"%((q4)+(q4*0.05)))
            self.var_tax.set(tax)
            self.var_sub.set(ST)
            self.var_tot.set(TT)
        elif(self.var_meal.get()=="breakfast"or"Breakfast" and self.var_type.get()=="Single"):
            q1=float(300)
            q2=float(250)
            q3=float(self.var_nod.get())
            q4=float((q1+q2)*q3)
            tax="Rs. "+str("%.2f"%(q4*0.05))
            ST="Rs. "+str("%.2f"%(q4))
            TT="Rs. "+str("%.2f"%((q4)+(q4*0.05)))
            self.var_tax.set(tax)
            self.var_sub.set(ST)
            self.var_tot.set(TT)
        elif(self.var_meal.get()=="Lunch"or"lunch" and self.var_type.get()=="Single"):
            q1=float(400)
            q2=float(250)
            q3=float(self.var_nod.get())
            q4=float((q1+q2)*q3)
            tax="Rs. "+str("%.2f"%(q4*0.05))
            ST="Rs. "+str("%.2f"%(q4))
            TT="Rs. "+str("%.2f"%((q4)+(q4*0.05)))
            self.var_tax.set(tax)
            self.var_sub.set(ST)
            self.var_tot.set(TT)

        elif(self.var_meal.get()=="Dinner"or"dinner" and self.var_type.get()=="Single"):
            q1=float(350)
            q2=float(250)
            q3=float(self.var_nod.get())
            q4=float((q1+q2)*q3)
            tax="Rs. "+str("%.2f"%(q4*0.05))
            ST="Rs. "+str("%.2f"%(q4))
            TT="Rs. "+str("%.2f"%((q4)+(q4*0.05)))
            self.var_tax.set(tax)
            self.var_sub.set(ST)
            self.var_tot.set(TT)
        elif(self.var_meal.get()=="Dinner"or"dinner" and self.var_type.get()=="Double"):
            q1=float(350)
            q2=float(500)
            q3=float(self.var_nod.get())
            q4=float((q1+q2)*q3)
            tax="Rs. "+str("%.2f"%(q4*0.05))
            ST="Rs. "+str("%.2f"%(q4))
            TT="Rs. "+str("%.2f"%((q4)+(q4*0.05)))
            self.var_tax.set(tax)
            self.var_sub.set(ST)
            self.var_tot.set(TT)
        elif(self.var_meal.get()=="Lunch"or"lunch" and self.var_type.get()=="Double"):
            q1=float(400)
            q2=float(500)
            q3=float(self.var_nod.get())
            q4=float((q1+q2)*q3)
            tax="Rs. "+str("%.2f"%(q4*0.05))
            ST="Rs. "+str("%.2f"%(q4))
            TT="Rs. "+str("%.2f"%((q4)+(q4*0.05)))
            self.var_tax.set(tax)
            self.var_sub.set(ST)
            self.var_tot.set(TT)
        elif(self.var_meal.get()=="Breakfast"or"breakfast" and self.var_type.get()=="Double"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_nod.get())
            q4=float((q1+q2)*q3)
            tax="Rs. "+str("%.2f"%(q4*0.05))
            ST="Rs. "+str("%.2f"%(q4))
            TT="Rs. "+str("%.2f"%((q4)+(q4*0.05)))
            self.var_tax.set(tax)
            self.var_sub.set(ST)
            self.var_tot.set(TT)
#search system===================================
    def search(self):
        conn=sq.connect("Hotelmnt.db")
        c=conn.cursor()
        c.execute("SELECT * FROM room WHERE "+str(self.ser_var.get())+"= "+str(self.tex_ser.get()))
        rows=c.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
        
        
        




if __name__=="__main__":
    root=Tk()
    obj=rom_win(root)
    root.mainloop()


