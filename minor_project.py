#import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect(r'/home/justanotherlad/Desktop/bill_db.db')
print("Database created/ OPENED Successfully")

window=Tk()

def disp():
	ls=[]
	cursor=conn.execute("SELECT * FROM ELECTRICITY_BILL")
	for rows in cursor:
		ls.append(rows[0])
		ls.append(rows[1])
		ls.append(rows[2])
	n1=float(e1.get()) 
	n2=float(e2.get()) 
	n3=float(e3.get()) 
	m1=n1-ls[0] #ritam and swastik's units for this month
	m2=n2-ls[1]	#neel and dhriti's units for this month
	m3=n3-ls[2]	#deep's units for this month

	tot_units=float(e5.get())
	roomwise=m1+m2+m3
	common=tot_units-roomwise

	tot_bill=float(e4.get())
	Common=(tot_bill/tot_units) * common
	RitSwas=(tot_bill/tot_units) * m1
	NeelDhriti=(tot_bill/tot_units) * m2
	Deep=(tot_bill/tot_units) * m3

	messagebox.showinfo("Bill Amounts","Swastik: Rs. %d \n Ritam: Rs. %d \n Nilargha: Rs. %d \n Dhritiman: Rs. %d \n Sourjyadip: Rs. %d \n "%(RitSwas/2 + Common/5,RitSwas/2 + Common/5, NeelDhriti/2 + Common/5,NeelDhriti/2 + Common/5,Deep+Common/5 ))
	conn.execute("UPDATE ELECTRICITY_BILL SET SWASTIKRITAM=?, NEELDHRITI=?, DEEP=?",(n1,n2,n3))
	print("Database Updated Successfully")

	conn.commit()
	conn.close()


window.geometry('600x1000')

window.title("Electricity Bill for Abode J303")

lbl1=Label(window,text="Current Reading for Swastik & Ritam: ",font=("Times New Roman",12))
lbl1.grid(column=0,row=0)
#lbl1.pack()
e1=Entry(window,bd=5)
e1.grid(column=1,row=0)

#e1.pack()


lbl2=Label(window,text="Current Reading for Nilargha & Dhritiman: ",font=("Times New Roman",12))
lbl2.grid(column=0,row=1)
#lbl2.pack()
e2=Entry(window,bd=5)
e2.grid(column=1,row=1)

#e2.pack()

lbl3=Label(window,text="Current Reading for Sourjyadip: ",font=("Times New Roman",12))
lbl3.grid(column=0,row=2)
#lbl1.pack()
e3=Entry(window,bd=5)
e3.grid(column=1,row=2)

#e3.pack()


lbl4=Label(window,text="Total Bill Amount this month(in Rs): ",font=("Times New Roman",12))
lbl4.grid(column=0,row=3)
#lbl1.pack()
e4=Entry(window,bd=5)
e4.grid(column=1,row=3)

#e3.pack()

lbl5=Label(window,text="Total Units Consumed: ",font=("Times New Roman",12))
lbl5.grid(column=0,row=4)
#lbl1.pack()
e5=Entry(window,bd=5)
e5.grid(column=1,row=4)

#e3.pack()

bt=Button(window,text="Calculate",fg="red",bg="orange",command=disp)
bt.grid(column=1,row=6)



window.mainloop()
