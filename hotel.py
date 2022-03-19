from developer import profile
from details import det_win
from rooms import rom_win
from tkinter import *
from customer import cus_win 
class hotelmngsys():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1260x800+0+0")
        lbltil=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("Comic Sans MS",40,"bold"),bg='black',fg='Gold',bd=4,relief=RIDGE)
        lbltil.place(x=0,y=0,width=1260,height=50)
        lblname=Label(self.root,text="-by Harshit",font=("Comic Sans MS",12,"bold"),bg='black',fg='gold')
        lblname.place(x=1100,y=10)
        mnfr=Frame(self.root,bd=6,relief=RIDGE)
        mnfr.place(x=0,y=50,width=1260,height=750)
        lblmenu=Label(mnfr,text="MENU",font=("Comic Sans MS",20,"bold"),bg='black',fg='Gold',bd=4,relief=RIDGE)
        lblmenu.place(x=0,y=0,width=230)
        btnfr=Frame(mnfr,bd=6,relief=RIDGE)
        btnfr.place(x=0,y=50,width=228,height=240)

        cusbt=Button(btnfr,text="CUSTOMER",width=20,font=("Comic Sans MS",14,"bold"),bg='black',fg='Gold',bd=0,cursor='hand1',command=self.cus_det)
        cusbt.grid(row=0,column=0,pady=1)

        robt=Button(btnfr,text="ROOMS",command=self.room_det,width=20,font=("Comic Sans MS",14,"bold"),bg='black',fg='Gold',bd=0,cursor='hand1')
        robt.grid(row=1,column=0,pady=1)

        detbt=Button(btnfr,command=self.det,text="DETAILS",width=20,font=("Comic Sans MS",14,"bold"),bg='black',fg='Gold',bd=0,cursor='hand1')
        detbt.grid(row=2,column=0,pady=1)

        repbt=Button(btnfr,command=self.dev_det,text="Developer Details",width=20,font=("Comic Sans MS",14,"bold"),bg='black',fg='Gold',bd=0,cursor='hand1')
        repbt.grid(row=3,column=0,pady=1)

        outbt=Button(btnfr,command=self.exitnow,text="EXIT",width=20,font=("Comic Sans MS",14,"bold"),bg='black',fg='Gold',bd=0,cursor='hand1')
        outbt.grid(row=4,column=0,pady=1)

    def cus_det(self):
        self.newwindow=Toplevel(self.root)
        self.app=cus_win(self.newwindow)
    def room_det(self):
        self.newwindow=Toplevel(self.root)
        self.app=rom_win(self.newwindow)        
    def det(self):
        self.newwindow=Toplevel(self.root)
        self.app=det_win(self.newwindow)
    def exitnow(self):
        self.root.destroy()
    def dev_det(self):
        self.newwindow=Toplevel(self.root)
        self.app=profile(self.newwindow)        
    


if __name__=="__main__":
    root=Tk()
    obj=hotelmngsys(root)
    root.mainloop()
